"""
Suppose you are told that the one time pad encryption of the message "attack at dawn" is 6c73d5240a948c86981bc294814d
(the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex). What would be the one
time pad encryption of the message "" under the same OTP key?
"""


# Входные данные
message_1 = 'attack at dawn'
message_1 = int(str(message_1.encode("utf-8").hex()), base=16)
cipher_1 = int('6c73d5240a948c86981bc294814d', base=16)
message_2 = 'attack at dusk'
message_2 = int(str(message_2.encode("utf-8").hex()), base=16)

# Отображаем входные данные
print(hex(message_1))
print(hex(cipher_1))

# Проверяем адекватность входных данных
if len(bin(message_1)) != len(bin(cipher_1)):
    print('error 0')
    exit()

# Извлекаем ключ
message_1 = str(bin(message_1))[2:]
cipher_1 = str(bin(cipher_1))[2:]
key = ''
for n in range(len(message_1)):
    k = '0' if message_1[n] == cipher_1[n] else '1'
    key += k
print(key)

# Шифруем второе сообщение
message_2 = str(bin(message_2))[2:]
cipher_2 = ''
for n in range(len(message_2)):
    c = '0' if message_2[n] == key[n] else '1'
    cipher_2 += c
print(cipher_2)

cipher_2 = int(cipher_2, base=2)
print('\n', hex(cipher_2))
