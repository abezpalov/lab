import os
import sys

try:
    source = sys.argv[1]
except IndexError:
    print('Не указано имя источника')
    exit()

try:
    ws_id = sys.argv[2]
except IndexError:
    print('Не указано имя ПК')
    exit()

try:
    ssd_n = sys.argv[3]
except IndexError:
    print('Не указано имя цели')
    exit()

command = f'echo "{ws_id} {ssd_n}" >> ~/ws_list.txt'
print(command)
os.system(command)

dir = f'/media/abezpalov/{source}'

target = f'/media/abezpalov/{ssd_n}/{ws_id}'

# Make dir
command = f'mkdir {target}'
print(command)
os.system(command)

# Copy Open
command = f'rsync --archive --human-readable --recursive --progress --exclude-from=exclude.txt {dir}/Open {target}'
print(command)
os.system(command)

command = f'mkdir {target}/Users'
print(command)
os.system(command)

for subdir in os.listdir(f'{dir}/Users'):
    print(subdir, end=' ')

    if not os.path.isdir(f'{dir}/Users/{subdir}'):
        print()
        continue

    if subdir in ('Все пользователи', 'Public', 'All Users', 'Default', 'Default User'):
        print()
        continue

    if subdir.startswith('wadmin') or subdir.startswith('wtadmin') or subdir.startswith('sadmin'):
        print()
        continue

    print('- копируем')

    command = f'rsync  --archive --human-readable --recursive --progress --exclude-from=exclude.txt {dir}/Users/{subdir} {target}/Users'
    print(command)
    os.system(command)

print('\n\n\n\n\nDone!!!')


