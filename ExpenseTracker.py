#Expense Tracker:
expensesList = []
print("Welcome to Expense Tracker")
while True:
    print("------MENU------")
    print("1. Add Expense:")
    print("2. View All Expenses:")
    print("3. View All Spending:")
    print("4. Exit")
    Choices = int(input("enter your choice:"))
    if Choices == 1:
        date = input("Enter The Date:")
        category =input("Enter Your expense type:")
        description =input("Enter more Detail:")
        amount = int(input("Enter the amount:"))
        expenses ={"date":date,
              "category":category,
              "description":description,
              "amount":amount
                             }
        expensesList.append(expenses)
        print("Done bro!,Expenses Added")
    elif Choices == 2:
        if len(expensesList)==0:
            print("Nothing is Added")
        else:
            print("----All Of Your Expenses----")
        count = 1
        for eachExpense in expensesList:
            print(f"Expense number{count}->{eachExpense["date"]},{eachExpense["category"]},{eachExpense["description"]},{eachExpense["amount"]}")
        count += 1
    elif Choices == 3:
        total = 0
        for eachExpense in expensesList:
            total = total + eachExpense["amount"]
        print("Total Expenses:",total)
    elif Choices == 4 :
        print("Thank You For using Our System!")
        break
    else:
        print("Invalid Choice!")


