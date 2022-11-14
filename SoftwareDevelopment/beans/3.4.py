def ReadFile(filename):
    namesArray = [""] * 100
    datesArray = [""] * 100
    ticketsArray = [""] * 100
    priceArray = [""] * 100
    counter = 0

    with open(filename, "r") as f:
        line = f.readline().rstrip('\n')
        items = line.split(",")
        for purchaseCounter in range(0, len(items), 4):
            namesArray[counter] = items[purchaseCounter]
            datesArray[counter] = items[purchaseCounter+1]
            ticketsArray[counter] = items[purchaseCounter+2]
            priceArray[counter] = items[purchaseCounter+3]
            counter += 1

    return (namesArray, datesArray, ticketsArray, priceArray)

def DisplayPurchases(na,da,ta,pa):
    counter = 0

    for i in range(0, len(na)):
        print(f'----- Sale {counter} -----')
        print(f'Name: {na[i]}')
        print(f'Date: {da[i]}')
        print(f'No. of Tickets: {ta[i]}')
        print(f'Final Price: £{pa[i]}')
        print(f'\n')
        counter += 1

    print('----- End Of Sales List -----')



namesArray, datesArray, ticketsArray, priceArray = ReadFile("SoftwareDevelopment/datafiles/sales.csv")
DisplayPurchases(namesArray, datesArray, ticketsArray, priceArray)
