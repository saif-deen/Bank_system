# # Parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)


class Bank(User):
    pass


class Dollar(Bank):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.dollar_balance = 0

    def deposit_dollar(self, amount):
        self.amount = amount
        self.dollar_balance = self.dollar_balance + self.amount

    def withdraw_dollar(self, amount):
        self.amount = amount
        self.dollar_balance = self.dollar_balance - self.amount

    def transfer_dollar(self, receiver, amount):
        self.withdraw_dollar(amount)
        receiver.deposit_dollar(amount)

    def view_dollar_balance(self):
        return print(f"the balance of {self.name} is {self.dollar_balance} $")


class DLY(Bank):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.dly_balance = 0

    def deposit_dly(self, amount):
        self.amount = amount
        self.dly_balance = self.dly_balance + self.amount

    def withdraw_dly(self, amount):
        self.amount = amount
        self.dly_balance = self.dly_balance - self.amount

    def transfer_dly(self, receiver, amount):
        self.withdraw_dly(amount)
        receiver.deposit_dly(amount)

    def view_dly_balance(self):
        return print(f"the balance of {self.name} is {self.dly_balance} DLY")


class Euro(Bank):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.euro_balance = 0

    def deposit_euro(self, amount):
        self.amount = amount
        self.euro_balance = self.euro_balance + self.amount

    def withdraw_euro(self, amount):
        self.amount = amount
        self.euro_balance = self.euro_balance - self.amount

    def transfer_euro(self, receiver, amount):
        self.withdraw_euro(amount)
        receiver.deposit_euro(amount)

    def view_euro_balance(self):
        return print(f"the balance of {self.name} is {self.euro_balance} €")


class Convert_Currencies(Dollar, DLY, Euro):
    Dollar = 1
    Euro = 1.01
    DLY = 5.04


    print("===================================")
    print("Welcome to $$ EXCHANGE STORE $$")
    print("===================================\n")
    From = input("Exchange FROM (Dollar, Euro, DLY):  ")
    print(From)
    amount = float(input("How much? "))
    To = input("Exchange To (Dollar, Euro, DLY):  ")
    print(To)

    NewAmount = 0

    if From == To:
     print(f"You will keep your amount as it is, ({amount} {From})")
     exit()

    elif From == "Dollar" and To == "Euro":
     NewAmount = amount / Euro

    elif From == "Euro" and To == "Dollar":
     NewAmount = amount / Euro

    elif From == "Dollar" and To == "DLY":
     NewAmount = amount / DLY

    elif From == "DLY" and To == "Dollar":
     NewAmount = amount / DLY

    else:
     print("You wrote wrong currency")
     exit()

    print(f"You will give {amount} {From}, and you will take {NewAmount} {To}")

saif = Euro("saifdeen", 25, "Male")
saif.deposit_euro(1000)
saif.deposit_euro(500)
saif.withdraw_euro(100)
saif.view_euro_balance()

mahmode = Dollar("mahode alforawi", 24, "Male")
mahmode.deposit_dollar(2500)
mahmode.withdraw_dollar(200)
mahmode.view_dollar_balance()

# mahmode = DLY("mahode alforawi", 24, "Male")
# mahmode.deposit_dly(1300)
# mahmode.view_dly_balance()

# ali = Dollar("ali hasan", 67, "Male")
# ali.deposit_dollar(1500)
# ali.transfer_dollar(mahmode, 500)
# ali.view_dollar_balance()

yahya = Euro("yahya ab", 31, "Male")
yahya.deposit_euro(2000)
yahya.transfer_euro(saif, 1500)
yahya.view_euro_balance()
saif.view_euro_balance()

