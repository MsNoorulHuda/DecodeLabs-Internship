# Expense Tracker Program
total=0
while True:
    expense=int(input('Enter your Expense:'))
    if expense==0:
        print('Expense entry finished.')
        print('Total Expense',total)
        break 
    total+=expense
    print('Total Expense',total)

