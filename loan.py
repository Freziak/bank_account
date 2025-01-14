INTEREST_RATE = 3.5

class Loan:

    def __init__(self, money, months):
        self.money = money
        self.months = months
        

    def calculatePayment(self):
        return round(self.money / self.months)
    
    def pay(self, loan_money):
        self.money -= loan_money
        print(f"Do spłacenia pozostało {self.money} zł.")

    def isPaidOff(self):
        if self.money > 0:
            return True
