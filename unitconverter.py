import mysql.connector
sql = mysql.connector.connect(user=)


ch=1
while ch==True:
    with open('currencydata.txt') as f:
        currency = f.readlines()

    CurrencyDict = {}
    for line in currency:
        parsed = line.split("\t")
        CurrencyDict[parsed[0]] = parsed[1]

    amount = int(input("Enter amount:\n"))
    print("Enter the name of currency which you want to convert the amount:\n")
    [print(item) for item in CurrencyDict.keys()]
    currency = input("Please enter one of these values:\n")
    print(f"{amount} INR is equal to {amount*float(CurrencyDict[currency])} {currency}")
    ch=int(input('entre ch'))