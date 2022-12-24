import os
import sys

try:
    source = f'/media/abezpalov/{sys.argv[1]}'
except IndexError:
    print('Не указано имя источника')
    exit()

try:
    target = f'/media/abezpalov/{sys.argv[2]}'
except IndexError:
    print('Не указано имя цели')
    exit()

print(source, target)


for subdir in os.listdir(source):
    print(subdir, end = ' ')

    print('- копируем')

    command = f'rsync  --archive --human-readable --recursive --progress --exclude-from=exclude.txt {source}/{subdir} {target}'
    print(command)
    os.system(command)

print('\n\n\n\n\nDone!!!')


