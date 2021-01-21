class ATM(object):
    def __init__(self, balance, cardNo, pinNo):
        self.balance = balance
        self.cardNo = cardNo
        self.pinNo = pinNo

    def getBalance(self):
        print(f"The balance in your account is {self.balance}/-")

    def deposit(self):
        amt = int(input("The amt you want to deposit: "))
        print(f"The current balance is {self.balance}")
        self.balance = self.balance + amt
        print(f"The balance after the deposition of the amt is {self.balance}")

    def withDraw(self):
        amt = int(input("The amt you want to withdraw: "))
        print(f"The amt before the withdrawal was {self.balance}")
        self.balance = self.balance - amt
        print(f"The amt after the withdrawal is {self.balance}")

atm = ATM(1000, 12345, 54321)
atm.getBalance()
atm.deposit()
atm.getBalance()
atm.withDraw()
atm.getBalance()