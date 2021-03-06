import sys
from datetime import datetime, date

myfile = open("mint03122018.csv")
# expected output 998666
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

data = myfile.readlines()

fields = data[0].split('","')

class QBTransaction(object):
    """docstring for QBTransaction"""
    def __init__(self, arg = []):
        super(QBTransaction, self).__init__()
        self.transDate = datetime.strptime(arg[0], '%m/%d/%Y')
        self.description = arg[1]
        self.origDicreption = arg[2]
        self.amount = float(arg[3])
        self.type = arg[4]
        self.category = arg[5]
        self.accountName = arg[6]
        
# def filterTrans(datetime startDate, datetime endDate, transactions):

for val in fields:
    print(val)

transactions = [];
for line in data[1:]:
    values = line.split('","')
    if len(values) > 2:
        values[0] = values[0][1:]
        trans = QBTransaction(values)
        transactions.append(trans)

categories = [];
credit = {}
debit = {}
budget = {
    'Gas & Fuel'      :  250.0,
    'Groceries'       : 1000.0,
    'Mortgage & Rent' : 1200.0,
    'Check'           : 1250.0,
    'Auto Payment'    :  410.0,
    'Auto Insurance'  :  250.0,
    'Charity'         :  200.0,
    'Home Insurance'  :  232.0,
    'Television'      :  188.0,
    'Home Phone'      :  360.0,
    'Utilities'       :  260.0,
    'Doctor'          :  150.0,
    'room/board'      :  700.0,
    'Cash & ATM'      : 1250.0,
    'Travel'          :  400.0
}
startDate = datetime(2018, 3, 1)
endDate = datetime(2018, 3, 28)
# endDate = datetime.today()
#
# Loop over all the transactions and build a category list that has all the unique
# categories in the transactions, and a dictionary or credits and debits in the 
# given timeframe. 
#
# Note: Currently ignoring categories 'Transfer', 'Check', and 'Credit Card Payment'
#

for trans in transactions:
    if trans.transDate >= startDate and trans.transDate <= endDate:
        category = trans.category
        if category in categories:
            if trans.type == 'credit':
                credit[category] += trans.amount
            elif trans.type == 'debit':
                debit[category] += trans.amount
            else:
                print("Unknown transaction type: ", trans.type)
        else:
            # print(category)
            ignoredCategories = ['Transfer', 'Credit Card Payment']
            if not trans.category in ignoredCategories:
                if trans.type == 'credit':
                    credit[category] = trans.amount
                elif trans.type == 'debit':
                    debit[category] = trans.amount
                categories.append(category)

print("Credit Transactions")
if not credit:
    print("None")

for cat, val in credit.items():
    print("{0:20} | {1:>10.2f}".format(cat, val))

print("Debit Transactions")
if not debit:
    print("None")
    
total = 0.0
budgetTotal = 0.0
for cat, val in debit.items():
    total += val;
    if cat in budget:
        budgetTotal += budget[cat]
        print("{0:20} | {1:>10.2f} | {2:>10.2f}".format(cat, budget[cat], val))
    else:
        print("{0:20} | {1:>10} | {2:>10.2f}".format(cat, 'none', val))

print("{0:20} | {1:>10.2f} | {2:>10.2f}".format('Total', budgetTotal, total))

# for trans in transactions:
#     if trans.transDate > startDate and trans.transDate < endDate:
#         transStr = trans.transDate.strftime("%B %d, %Y")
#         print('{0:18} | {1:24} | {2:25} | {3:8}'.format(transStr, trans.description, trans.category, trans.amount))


