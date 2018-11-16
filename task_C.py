clients = []
balances = []
file = open("input.txt")
def balance(name):
    global clients
    global balances
    if name not in clients:
        print("ERROR")
    else:
        q = str(balances[clients.index(name)])
        if q.find(".") == -1:
            print(q)
        else:
            mp = [s for s in q.split(".")]
            print(mp[0])
def deposit(name, money):
    global clients
    global balances
    if name not in clients:
        clients.append(name)
        balances.append(money)
    else:
        balances[clients.index(name)] += money
def withdraw(name, money):
    global clients
    global balances
    if name not in clients:
        clients.append(name)
        balances.append(0 - money)
    else:
        balances[clients.index(name)] -= money
def transfer(name1, name2, money):
    if name1 not in clients:
        clients.append(name1)
        balances.append(0)
    if name2 not in clients:
        clients.append(name2)
        balances.append(0)
    balances[clients.index(name1)] -= money
    balances[clients.index(name2)] += money
def income(percent):
    for i in range(len(balances)):
        if balances[i] > 0:
            balances[i] = (1 + percent / 100) * balances[i]
for z in file:
    command = [s for s in z.split()]
    if command[0] == "BALANCE":
        balance(command[1])
    if command[0] == "DEPOSIT":
        deposit(command[1], int(command[2]))
    if command[0] == "WITHDRAW":
        withdraw(command[1], int(command[2]))
    if command[0] == "TRANSFER":
        transfer(command[1], command[2], int(command[3]))
    if command[0] == "INCOME":
        income(float(command[1]))