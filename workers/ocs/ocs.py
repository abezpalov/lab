import requests as r
import json
import urllib.parse
import pandas as pd

import settings


def get_by_api(command: str = '', params: str = ''):
    """
    Получает данные через GET-запрос к API OCS.
    Для работы требует ключ, который любой партнёр может получить
    в b2b-системе по адресу: https://b2b.ocs.ru/connector/account
    """

    if params:
        url = f'https://connector.b2b.ocs.ru/api/v2/{command}?{params}'
    else:
        url = f'https://connector.b2b.ocs.ru/api/v2/{command}'
    headers = {'X-API-Key': settings.OCS_TOKEN,
               'accept': 'application/json'}
    result = r.get(url, headers=headers, verify=None)

    if result.status_code == 200:
        return result.json()
    else:
        print(f'Error: {result.status_code} in URL {url}')
        return None


def post_by_api(command: str = '', params: str = ''):
    """
    Получает данные через POST-запрос к API OCS.
    Для работы требует ключ, который любой партнёр может получить
    в b2b-системе по адресу: https://b2b.ocs.ru/connector/account
    """

    url = f'https://connector.b2b.ocs.ru/api/v2/{command}'
    headers = {'X-API-Key': settings.OCS_TOKEN,
               'accept': 'application/json',
               'Content-Type': 'application/json'}

    result = r.post(url, headers=headers, data=str(params), verify=None)
    if result.status_code == 200:
        return result.json()
    else:
        print(f'Error: {result.status_code} in URL {url}')
        return None


def get_shipment_cities() -> list:
    """
    Получает города, доступные к отгрузке для партнёра.
    Данные требуются для получения информации о товарах, ценах и наполнении складов.
    """

    print('Получаю список городов, доступных к отгрузке')

    command = 'logistic/shipment/cities'
    data = get_by_api(command)
    if data:
        return data
    else:
        raise ValueError('Ошибка! Получены пустые данные.')


def get_products(cities: list):
    """
    Получает данные о товарах, ценах и наполнении складов.
    """

    print('Получаю данные о товарах, ценах и наполнении складов')

    command = 'catalog/categories/all/products'
    products = []

    # Проходим по всем городам отгрузки
    for city in cities:
        city = urllib.parse.quote_plus(city)
        data = get_by_api(command, f'shipmentCity={city}&&includesale=true'
                                   f'&includeuncondition=true&includemissing=true')

        # Проходим по всем товарам
        for n, item in enumerate(data['result']):
            product = parse_product(item)
            products.append(product)
            print(f"{n + 1} of {len(data['result'])} {product['vendor']} {product['part_number']} ")

    return products

def parse_product(item: dict) -> dict:
    """
    Разбирает данные о продукте в удобно-обрабатываемый формат.
    """

    product = dict()

    # Производитель
    product['vendor'] = item['product']['producer']

    # Категория
    product['category'] = item['product']['category']

    # Внутренний идентификатор товара
    product['product_key'] = item['product'].get('itemId', None)

    # Внутренний идентификатор партии (товары со свойствами "некондиция" выделяются в отдельную партию
    product['party_key'] = item['product'].get('productKey', None)

    # Артикул производителя
    product['part_number'] = item['product'].get('partNumber', None)

    # Различные наименования товара
    product['short_name'] = item['product'].get('productName', None)
    product['name_rus'] = item['product'].get('itemNameRus', None)
    product['name_other'] = item['product'].get('itemName', None)
    if not product['name_other'].startswith(product['name_rus']):
        product['name'] = f"{product['name_rus']} {product['name_other']}"
    else:
        product['name'] = product['name_other']

    # Краткое описание товара
    product['description'] = item['product'].get('productDescription', None)

    # Информация о гарантии
    product['warranty'] = item['product'].get('warranty', None)

    # Коды
    product['ean_128'] = item['product'].get('eaN128', None)
    product['upc'] = item['product'].get('upc', None)
    product['pnc'] = item['product'].get('pnc', None)
    product['hs_code'] = item['product'].get('hsCode', None)

    # Является ли товар прослеживаемым
    product['traceable'] = item['product'].get('traceable', None)

    # Информация об акциях и кондиционности
    product['unconditional'] = False
    product['sale'] = False
    if item['product']['condition'] == 'Regular':
        product['unconditional'] = False
        product['sale'] = False
    elif item['product']['condition'] == 'Sale':
        product['unconditional'] = False
        product['sale'] = True
    elif item['product']['condition'] == 'Unconditional':
        product['unconditional'] = True
        product['sale'] = False
    product['condition_description'] = item['product'].get('conditionDescription', None)

    # Логистический параметры
    product['weight'] = item['packageInformation'].get('weight', None)
    product['width'] = item['packageInformation'].get('width', None)
    product['height'] = item['packageInformation'].get('height', None)
    product['depth'] = item['packageInformation'].get('depth', None)
    product['volume'] = item['packageInformation'].get('volume', None)
    product['multiplicity'] = item['packageInformation'].get('multiplicity', None)
    product['unit'] = item['packageInformation'].get('units', None)

    # Получаем актуальную информацию по партиям товара
    product['is_available_for_order'] = item.get('isAvailableForOrder', None)

    try:
        product['price_in'] = item['price']['order']['value']
        product['currency_in'] = item['price']['order']['currency'].replace('RUR', 'RUB')
    except KeyError:
        product['price_in'] = None
        product['currency_in'] = None

    try:
        product['price_out'] = item['price']['endUser']['value']
        product['currency_out'] = item['price']['endUser']['currency'].replace('RUR', 'RUB')
    except KeyError:
        product['price_out'] = None
        product['currency_out'] = None

    try:
        product['price_out_open'] = item['price']['endUserWeb']['value']
        product['currency_out_open'] = item['price']['endUserWeb']['currency'].replace('RUR', 'RUB')
    except KeyError:
        product['price_out_open'] = None
        product['currency_out_open'] = None

    try:
        product['must_keep_end_user_price'] = item['price']['must_keep_end_user_price']
    except KeyError:
        product['must_keep_end_user_price'] = None

    for location in item['locations']:
        key = location['location']
        description = location.get('description')

        product[f'{key}_quantity'] = location['quantity']['value']
        product[f'{key}_quantity_great_than'] = location['quantity'].get('isGreatThan', False)
        product[f'{key}_can_reserve'] = location.get('canReserve', None)

    return product


def get_content(products: dict):

    keys = []
    for product in products:
        keys.append(product['product_key'])

    batches_count = len(keys) // settings.OCS_BATCH_SIZE + 1\
        if len(keys) % settings.OCS_BATCH_SIZE\
        else len(keys) // settings.OCS_BATCH_SIZE

    for n in range(batches_count):
        print(f"Получаю описание: {n + 1} of {batches_count}")
        batch = json.dumps(keys[n * settings.OCS_BATCH_SIZE:(n + 1) * settings.OCS_BATCH_SIZE])

        data = post_by_api(command='content/batch', params=batch)

        # Разбираем полученные данные
        if data is not None:
            for content_item in data['result']:
                product_key = content_item['itemId']

                #
                for i, product in enumerate(products):
                    if product['product_key'] == product_key:
                        print(f'\t{product["vendor"]} {product["part_number"]}')
                        for parameter in content_item['properties']:
                            parameter_name = parameter.get('name', None)
                            if parameter.get('value', None) and parameter.get('unit', None):
                                parameter_value = f'{parameter.get("value")} {parameter.get("unit")}'
                            else:
                                parameter_value = parameter.get('value', None)
                            products[i][parameter_name] = parameter_value
                            print(f'\t\t{parameter_name} {parameter_value}')

    return products


def save_data(data, filename):

    # Сохраняем в формате JSON
    file = open(f'{filename}.jsom', 'w')
    json.dump(data, file, indent=4)
    file.close()

    # Сохраняем в формате XLSX
    df = pd.DataFrame(data)
    df.to_excel(f'{filename}.xlsx', engine='xlsxwriter')


def main():

    cities = get_shipment_cities()
    save_data(cities, 'data/cities')

    products = get_products(cities)
    save_data(products, 'data/products')

    if settings.OCS_GET_DESCRIPTION:
        products = get_content(products)
        save_data(products, 'data/products_and_content')


if __name__ == "__main__":
    main()
