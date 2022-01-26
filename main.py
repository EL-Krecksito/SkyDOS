import platform
import os

if platform.system() == 'Linux':
    os.system('figlet -r SkyDOS|lolcat')
elif platform.system() == 'Windows':
    os.system('title SkyDOS')
    os.system('powershell "cd FiFIGlet-Win32(static);./figlet.exe -r SkyDOS|./..\Meow/bin\meow.ps1"')

url = input('URL/IP a probar: ')
by = int(input('Numero de paquetes/bytes: '))
arg = input('Ingrese un argumento personalizado[opcional]: ')

if by > 50000:
    print('Error: demasiados paquetes/bytes.')
    exit()
elif by < 8:
    print('Error: muy pocos paquetes/bytes.')
    exit()

if platform.system() == 'Linux':
    os.system(f'ping {url} {arg} -s {by}')
elif platform.system() == 'Windows':
    os.system(f'ping -l {by} {url} -t {arg}')
