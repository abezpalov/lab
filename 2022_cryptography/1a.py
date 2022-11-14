"""
Suppose you are told that the one time pad encryption of the message "attack at dawn" is 6c73d5240a948c86981bc294814d
(the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex). What would be the one
time pad encryption of the message "" under the same OTP key?
"""


# Входные данные
message_1 = 'attack at dawn'
message_1 = int(str(message_1.encode("utf-8").hex()), base=16)
cipher_1 = int('09e1c5f70a65ac519458e7e53f36', base=16)
message_2 = 'attack at dusk'
message_2 = int(str(message_2.encode("utf-8").hex()), base=16)

# Отображаем входные данные
print('M1 hex:', hex(message_1))
print('C1 hex:', hex(cipher_1))
print('M2 hex:', hex(message_2))

# Проверяем адекватность входных данных и дополняем незначащими нулями
message_1 = str(bin(message_1))[2:]
cipher_1 = str(bin(cipher_1))[2:]
message_2 = str(bin(message_2))[2:]
length = max(len(message_1), len(cipher_1), len(message_2))
new_length = length + 16 - (length % 16)
print(f'{length} -> {new_length}')

message_1 = (new_length - len(message_1)) * '0' + message_1
cipher_1 = (new_length - len(cipher_1)) * '0' + cipher_1
message_2 = (new_length - len(message_2)) * '0' + message_2

print('M1 bin:', message_1)
print('C1 bin:', cipher_1)
print('M2 bin:', message_2)
print()

# Извлекаем ключ
key = ''
for n in range(len(message_1)):
    k = '0' if message_1[n] == cipher_1[n] else '1'
    key += k
print('K! bin:', key, '\n')

# Шифруем второе сообщение
cipher_2 = ''
for n in range(len(message_2)):
    c = '0' if message_2[n] == key[n] else '1'
    cipher_2 += c
print('C2 bin:', cipher_2)

cipher_2 = int(cipher_2, base=2)
print('C2 hex:', hex(cipher_2)[2:])
