import exception as ex


class BankAccount:
    min_balance = 50000
    counter = 10000
    lst = []
    TrackingNumber = 10000

    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        BankAccount.counter += 1
        self.AccNumber = BankAccount.counter
        BankAccount.lst.append([self.full_name, self.AccNumber, self.balance, []])

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def Deposit(self, amount):
        self.balance += amount
        BankAccount.TrackingNumber += 1
        for lst in BankAccount.lst:
            if lst[1] == self.AccNumber:
                lst[2] = self.balance
                lst[3].append([amount, 'Deposit', BankAccount.TrackingNumber, self.balance])
                break
        print('**succesful transaction**')
        print(f'Tracking number: {BankAccount.TrackingNumber}')
        return self.balance

    def Withdrawal(self, amount):
        self.balance -= amount
        BankAccount.TrackingNumber += 1
        for lst in BankAccount.lst:
            if lst[1] == self.AccNumber:
                lst[2] = self.balance
                lst[3].append([amount, 'Withdrawal', BankAccount.TrackingNumber, self.balance])
                break
        print('**succesful transaction**')
        print(f'Tracking number: {BankAccount.TrackingNumber}')
        return self.balance

    def Transfer(self, AccNum, amount):
        if amount < (self.balance - BankAccount.min_balance):
            self.balance -= amount
            BankAccount.TrackingNumber += 1
            for lst in BankAccount.lst:
                if lst[1] == self.AccNumber:
                    lst[2] = self.balance
                    lst[3].append([amount, 'Withdrawal', BankAccount.TrackingNumber, self.balance])
                    break

            for lst in BankAccount.lst:
                if lst[1] == AccNum:
                    lst[2] += amount
                    lst[3].append([amount, 'Deposit', BankAccount.TrackingNumber, lst[2]])
                    break

            print('**succesful transaction**')
            print(f'Tracking number: {BankAccount.TrackingNumber}')
        else:
            print('**insufficient funds**')
            amount = int(input('Enter new amount: '))
            self.Transfer(AccNum, amount)

    def get_Turnover(self):
        for lst in BankAccount.lst:
            if lst[1] == self.AccNumber:
                print(f"{'<Amount>':<12}{'<Transaction>':<17}{'<TrackingNumber>':<20}{'<Balance>':<5}")
                print('-----------------------------------------------------')
                for lis in lst[3]:
                    print(f'{lis[0]:<12}{lis[1]:<17}{lis[2]:<20}{lis[3]:<5}')
