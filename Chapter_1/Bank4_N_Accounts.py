# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

# This code is still working with globral data; now there are three global lists of data 

# Imageine viewing this data as a spreadsheet. 

# The data is maintained as three global Python lists, where each list represents a column in this table

# For example, as you can see from the highlighted column, all the passwords are grouped toghether as one list. 
# The users' names are grouped in another list, and the balances are grouped in a third list. 

# With this approach, to get information about one account, you need to access these lists with a common index value. 


accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
   
def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('       Name', accountNamesList[accountNumber])
    print('       Balance:', accountBalancesList[accountNumber])
    print('       Password:', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
        
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    
    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + amountToDeposit
    return accountBalancesList[accountNumber]
    
def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalancesList[accountNumber]

# Create two sample accounts
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    
    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
        
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('What is the amount of your initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountNamesList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':   #show all
        print('Show:')
        nAccounts = len(accountNamesList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
 
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)       

print('Done')

# While this works, it seems extremelly awkward. The data is not grouped in a logical way. 
# For example, it doesn't seem right to keep all users' passwords together. 

# Further, every time you add a new attribute to an account, like an address or phone number, you need to create and access another global list. 

# Instead, what really want is a grouping that represents a row in the same spreadsheet. 

# With this approach, each row represents the data associated with a single bank account. While this is the same data, this grouping is a much
# more natural way of representing an account. 