def main():
    count=0
    while count<=50:
        coin = int(input("Insert coin: "))
        if coin == 25:
            count= count+25
        if coin == 10:
            count= count+10
        if coin == 5:
            count= count+5
        amountDue = str(50 - count)
        if count<50:
            print("Amount Due: " + amountDue)
        if count>=50:
            changeOwed = str(count - 50)
            print("Change Owed: " + changeOwed)
            break

main()
