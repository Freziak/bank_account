import random

class Balance:

    def __init__(self):
        self.stan_konta = random.randint(100, 10000)

    def change(self, number):
        if number == 2:
            account_numer = int(input("Na jakie konto chcesz przelac pieniadze? Podaj numer konta: "))
            transfer_money_from_account = int(input("Podaj wartośc przelewu: "))
            if transfer_money_from_account > self.stan_konta:
                return False
            else:
                self.stan_konta -= transfer_money_from_account
        elif number == 3:
            transfer_money_to_account = int(input("Podaj kwote: "))
            if transfer_money_to_account > 10000:
                print("Zbyt duza kwota jednorazowego przelewu.")
            else:
                self.stan_konta += transfer_money_to_account