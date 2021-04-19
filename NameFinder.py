import requests
from sys import argv
from colorama import Fore
from banner import banner
banner()
try:
    print(f'                Wordlist : {argv[1]}')
    print(f'                Country Code: {argv[2]}')
except IndexError:
    print('usege: python3 NameFinder.py <wordlist> <country_code> ')
    exit()
open_file = open(argv[1], 'r').readlines()
White = Fore.LIGHTWHITE_EX
Green = Fore.LIGHTGREEN_EX
Red = Fore.LIGHTRED_EX
try:
    for i in open_file:
        Number = i.strip()
        url = f'http://146.148.112.105/caller/index.php/UserManagement/search_number?number={Number}&country_code={argv[2]}'
        name = requests.get(url)
        data = name.json()
        try:
            for j in data['result']:
                number = j['number']
                name = j['name']
                print(f'{White}[{Green}*{White}] {number} : {Green} {name} ')
        except:
            print(f'{White}[{Red}!{White}] Number Not Found: {Red}{number}')
except KeyboardInterrupt:
    print(f'{White}[{Red}!{White}] Session Closed')
    exit()