import requests
import json
import time
from multiprocessing.dummy import Pool as ThreadPool

# Настройки
threads = 8  # Количество потоков
log = 2  # Уровень детализации вывода процесса на экран


def get_principals() -> list:

    # Инициализируем переменные
    principals = []
    size = 100

    # Получаем дерево HTML с регионами для парсига
    s = requests.Session()
    result = s.get(f'https://icscan.io/ic/principal/canisters?page=0&pageSize={size}&up=0')
    data = json.loads(result.text)
    total = data['total']
    pages = total // size if total % size else total // size + 1

    for page in range(pages):
        url = f'https://icscan.io/ic/principal/canisters?page={page}&pageSize={size}&up=0'
        print(f'{page + 1} of {pages}: {url}')
        result = s.get(url)
        data = json.loads(result.text)

        for principal in data['principals']:
            print(principal)
            principals.append(principal)

        # time.sleep(1)

    file = open('data/principals.json', 'w')
    json.dump(principals, file, indent=4)
    file.close()

    return principals


def get_principals_from_file():
    file = open('data/principals.json', 'r')
    return json.load(file)


def get_accounts_for_principals(principals):

    s = requests.Session()

    for i, principal in enumerate(principals):

        while True:
            # if principal['canister_amount'] != 0:
            #     print(f'{i+1} of {len(principals)}: {principal["id"]}')
            #     break

            url = f'https://icscan.io/ic/principal/details?id={principal["id"]}'
            result = s.get(url)
            try:
                data = json.loads(result.text)
            except json.decoder.JSONDecodeError:
                print('json.decoder.JSONDecodeError')
                time.sleep(2)
                continue

            principals[i]['account'] = {'id': data['account']}
            print(f'{i + 1} of {len(principals)}: {principals[i]["id"]} {principals[i]["account"]["id"]}')
            break

    file = open('data/accounts.json', 'w')
    json.dump(principals, file, indent=4)
    file.close()

    return principals


def get_accounts_from_file():
    file = open('data/accounts.json', 'r')
    return json.load(file)


def get_details_for_accounts(principals):

    s = requests.Session()

    for i, principal in enumerate(principals):
        print(f'{i + 1} of {len(principals)}: {principal["id"]} {principal["account"]["id"]}')

        while True:

            url = f'https://icscan.io/api/nft/account/NFTClassByAccount?account={principal["account"]["id"]}'

            result = s.get(url)
            try:
                data = json.loads(result.text)
            except json.decoder.JSONDecodeError:
                print('json.decoder.JSONDecodeError')
                time.sleep(2)
                continue

            collection = []
            if data['Collections']:
                for nft_ in data['Collections']:
                    nft = {}
                    for key in nft_:
                        nft[key.lower()] = nft_[key]
                    collection.append(nft)
                    print(f'\t{nft["name"]} {nft["num"]}')

            principals[i]["account"]["collection"] = collection
            break

    file = open('data/collections.json', 'w')
    json.dump(principals, file, indent=4)
    file.close()

    return principals


def main():

    principals = get_principals()
    # principals = get_principals_from_file()

    principals = get_accounts_for_principals(principals)
    # principals = get_accounts_from_file()

    principals = get_details_for_accounts(principals)


if __name__ == "__main__":
    main()
