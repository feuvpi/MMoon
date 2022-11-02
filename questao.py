from collections import defaultdict
import math
import re

debts_rows = int(input().strip())
debts_columns = int(input().strip())
debts = ['Alex Blake 2', 'Blake Alex 2', 'Casey Alex 5', 'Blake Casey 7', 'Alex Blake 4', 'Alex Casey 4']

def smallestNegativeBalance(debts):

    mapa_devedores = defaultdict(int)
    mapa_credores = defaultdict(int)
    balance_map = defaultdict(int)

    for debt in debts:
        devedor, credor, amount = re.split('\\s+', debt, maxsplit=2)
        mapa_devedores[devedor] += int(amount)
        mapa_credores[credor] += int(amount)


    for key in mapa_devedores:
        balance_map[key] = mapa_credores[key] - mapa_devedores[key]

    maior_devedor = min(balance_map, key=balance_map.get)

    list = [k for k, v in balance_map.items() if float(v) == -3]
    print(balance_map[maior_devedor])

    if(balance_map[maior_devedor] < 0):
        print(type(list[0]))
    else:
        print("Nobody has a negative balance")

smallestNegativeBalance(debts)
