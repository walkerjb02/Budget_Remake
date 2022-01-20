from storage import dicti
class Main():
    def startup(self):
        while 1:
            menum, options = input('Add New Category -- new\nDeposit/Withdraw -- deposit\nTransfer -- transfer\nInput?\n'), {'new': 'Main().NewCategory()','deposit':'Main().Deposit()','transfer':'Main().Transfer()'}
            for i in options.keys():
                if menum in i: print(exec(options[i]))
    def NewCategory(self):
        name, amount = input('Category?\n'), int(input('Amount?\n'))
        dicti[name] = amount
        print(Main().Line())
    def Deposit(self):
        new, amount = input('New Category?\n'), int(input('Amount?\n'))
        for i in dicti:
            if new in i:
                dicti[i] = (dicti[new] + amount)
        print(Main().Line())
    def Transfer(self):
        old, new, amount = input('Old Category?\n'), input('New Category?\n'), int(input('Amount?\n'))
        for i in dicti:
            if old in i:
                dicti[i] = (dicti[old] - amount)
        for j in dicti:
            if new in j:
                dicti[j] = (dicti[new] + amount)
        print(Main().Line())
    def Line(self):
        for i in dicti:
            print(f'Your total in {i} category is {dicti[i]} and this category makes up {(dicti[i] / sum(dicti.values())) * 100}% of your total bundle')
        with open('storage.py', 'w') as file:
            file.write(f'dicti = {dicti}')
print(Main().startup())
