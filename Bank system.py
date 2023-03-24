class User:
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


class Convert_Currencies:
    def __init__(self):
        pass

    @property
    def euro(self) -> float:
        return float(1.01)

    @property
    def dly(self):
        return float(5.04)

    @property
    def dollar(self):
        return float(1)

    def convert(self):

        self.amount = float(input("Enter the number would you want to exchange"))
        print("===================================")
        print("Welcome to $$ EXCHANGE STORE $$")
        print("===================================\n")
        From = input("Exchange FROM (Dollar, Euro, DLY):  ")
        print(From)
        To = input("Exchange To (Dollar, Euro, DLY):  ")
        print(To)
        # print("{0:.3f}".format(Convert_Currencies))
        NewAmount = 0

        if From == To:
            print(f"You will keep your amount as it is, ({self.amount} {From})")
            return

        elif From == "Dollar" and To == "Euro":

            NewAmount = self.amount * self.euro
        elif From == "Euro" and To == "Dollar":
            NewAmount = self.amount / self.euro

        elif From == "Dollar" and To == "DLY":
            NewAmount = self.amount * self.dly

        elif From == "DLY" and To == "Dollar":
            NewAmount = self.amount / self.dly

        else:
            print("You wrote wrong currency")
            return

        print(f"You will give {self.amount} {From}, and you will take {NewAmount} {To}")


class Dollar(Bank, Convert_Currencies):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dollar_balance = 0


    def deposit_dollar(self, amount):
        self.amount = amount
        self.dollar_balance += self.amount

    def withdraw_dollar(self, amount):
        self.amount = amount
        self.dollar_balance -= self.amount

    def transfer_dollar(self, receiver, amount):
        self.withdraw_dollar(amount)
        receiver.deposit_dollar(amount)

    def view_dollar_balance(self):
        return print(f"the balance of {self.name} is {self.dollar_balance} $")


class DLY(Bank, Convert_Currencies):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.dly_balance = 0

    def deposit_dly(self, amount):
        self.amount = amount
        self.dly_balance += self.amount

    def withdraw_dly(self, amount):
        self.amount = amount
        self.dly_balance -= self.amount

    def transfer_dly(self, receiver, amount):
        self.withdraw_dly(amount)
        receiver.deposit_dly(amount)

    def view_dly_balance(self):
        return print(f"the balance of {self.name} is {self.dly_balance} dly")


class Euro(Bank, Convert_Currencies):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.euro_balance = 0


    def deposit_euro(self, amount):
        self.amount = amount
        self.euro_balance += self.amount

    def withdraw_euro(self, amount):
        self.amount = amount
        self.euro_balance -= self.amount

    def transfer_euro(self, receiver, amount):
        self.withdraw_euro(amount)
        receiver.deposit_euro(amount)

    def view_euro_balance(self):
        return print(f"the balance of {self.name} is {self.euro_balance} €")



