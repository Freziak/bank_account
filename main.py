from balance import Balance
from loan import Loan

_balance = Balance()

_loan = Loan(0, 0)

print("""
1. Wyświetl stan konta
2. Przelej pieniądze na konto
3. Przelej pieniądze z konta
4. Weź pożyczkę
5. Spłac pożyczkę
6. Wyjście""")


while True:
    choice = int(input("Co chcesz zrobic? "))

    if choice == 1:
        stan_konta = _balance.stan_konta
        print(f"Twój stan konta wynosi: {stan_konta}zł.")
    elif choice == 2:
        _balance.change(choice)
    elif choice == 3:
        _balance.change(choice)
    elif choice == 4:
        if _loan.isPaidOff():
            print("Posiadasz juz pozyczke. Splac poprzednia aby wziasc kolejna.")
            continue
        money = int(input("Na jaka kwote chcesz wziasc pozyczke? "))
        months = int(input("Na ile miesiecy chcesz wziasc pozyczke? "))
        _loan = Loan(money, months)
        print(f"Pozyczka bedzie wynosic {_loan.calculatePayment()} zł miesiecznie. ")
    elif choice == 5:
        loan_money = int(input(F"Twoja pożyczka wynosi {_loan.money} zł. Ile chcesz spacic? Podaj kwote: "))
        _loan.pay(loan_money)

    elif choice == 6:
        break