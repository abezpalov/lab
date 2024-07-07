import numpy as np


# Задаём полугруппу
class U:

    # Задаём размерность матрицы n*n
    n = 8

    # Задаём модуль элементов матрицы
    # В примере 256 + 1
    m = 257

    def __init__(self, a_: list | None = None):

        if a_ is None:
            self.value = np.array(range(self.n*self.n), dtype=np.dtype(np.uint64))
            self.value = np.resize(self.value, (self.n, self.n))
        elif type(a_) == list:
            if len(a_) > self.m:
                a_ = a_[:self.m]
            while len(a_) < self.m:
                a_.append(0)
            self.value = np.array(a_, dtype=np.dtype(np.uint64))
            self.value = np.resize(self.value, (self.n, self.n))
        elif type(a_) == np.ndarray:
            self.value = a_
        else:
            raise ValueError(f'Not supported type: {type(a_)}')

        self.value = self.value % self.m

    def __str__(self):
        return str(self.value)

    def __int__(self):
        result = 0
        exp = 0
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                result += int(self.value[i][j]) * self.m**exp
                exp += 1

        return result

    # Бинарная операция
    def __mul__(self, other):
        return U(self.value.dot(other.value))

    # Быстрое возведение в степень
    def __pow__(self, exponent: int):

        # Вычисляем максимальную степень двойки
        max_exp = 0
        while 2**max_exp <= exponent:
            max_exp += 1

        # Раскладываем показатель степени в степени двойки
        exp_of_2 = dict()
        exp_ = exponent
        for i in range(max_exp, 0, -1):
            if 2**i <= exp_:
                exp_ -= 2**i
                exp_of_2[i] = True
            else:
                exp_of_2[i] = False

        # Вычисляем результат
        iteration = self
        result = None
        for i in range(1, max_exp+1):
            if exp_of_2[i]:
                if result is None:
                    result = iteration
                else:
                    result = result * iteration
            iteration = iteration * iteration

        return result

    # XOR
    def __xor__(self, other):
        result = list()
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                result.append(int(self.value[i][j]) ^ int(other.value[i][j]))
        return U(result)

    def decode(self):
        result = list()
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                if self.value[i][j] > 0:
                    result.append(int(self.value[i][j]))
        return bytes(result).decode()


# Точка входа
if __name__ == '__main__':

    # Фиксируем u
    u = U()
    print(f'u = \n{u}\n')

    # 1. Отправитель генерирует случайное число n и вычисляет u^n
    # В примере одно из максимальных 16-битных простых чисел
    # В реальности, чем больше, тем лучше
    n = 65449
    print(f'n = {n}\n')

    u_n = u**n
    print(f'u^n = \n{u_n}\n')

    # 2. Получатель генерирует случайное число m и вычисляет u^m
    # В примере одно из максимальных 16-битных простых чисел
    # В реальности, чем больше, тем лучше
    m = 65521
    print(f'n = {m}\n')

    u_m = u**m
    print(f'u^m = \n{u_m}\n')

    # 3. Отправитель вычисляет ключ и переводит его в целочисленное значение
    u_m_n = u_m ** n
    print(f'u^m^n = \n{u_m_n}\n')
    encrypt_key = int(u_m_n)
    print(f'encoder_key = {hex(encrypt_key)[2:]}')
    print(f'размер ключа = {len(hex(encrypt_key)[2:])*16} бит')

    # 4. Получатель вычисляет ключ
    u_n_m = u_n ** m
    print(f'u^n^m = \n{u_n_m}\n')
    decrypt_key = int(u_n_m)
    print(f'encoder_key = {hex(decrypt_key)[2:]}\n')
    print(f'размер ключа = {len(hex(decrypt_key)[2:])*16} бит\n')

    # 5 Отправитель кодирует строку в бинарный вид и шифрует её
    s = "Всё, что зашифровано, должно быть расшифровано!"
    print(f's1 = {s}')
    for e in s.encode():
        print(e)
    print(list(s.encode()))
    encoded_s = U(list(s.encode()))
    print(f'encoded_s = \n{encoded_s}\n')

    encrypted_s = u_n_m ^ encoded_s
    print(f'encrypted_s = \n{encrypted_s}\n')

    # 6. Получатель дешифрует и декодирует сообщение
    decrypted_s = u_m_n ^ encrypted_s
    print(f'decrypted_s = \n{decrypted_s}\n')

    decoded_s = decrypted_s.decode()
    print(f'decoded_s = {decoded_s}\n')

