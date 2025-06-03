class BankAccount:
    def __init__(self,customer_name):
        self.account_holder_name=customer_name
        self.balance=5000
    def check_balance(self):
        print(f"Your Current Balance is {self.balance} Rupees.\n")
    def deposit_money(self,money1):
        self.balance+=money1
        print(f"{self.balance} Rupees Successfully Credited to your Account.\n")
        print(f"Your Current Balance {self.balance} Rupees.\n")
    def withdraw(self,money2):
        if self.balance-money2 <0:
            print("Insufficient Balance to withdraw the money.\n")
        else:
            self.balance-=money2
            print(f'{money2} Rupees Successfully Debited from your account.\n')
            print(f"Your Current Balance {self.balance} Rupees.\n")
    def exit(self):
        print(f"Thanks {self.account_holder_name} for using our payment site. Our Goal is your money safety.\nAlways ready for Your Transction Services.\n")
name=input("ENTER COSTUMER ID: ")
services=BankAccount(name)
password=int(input("ENTER PASSWORD: "))
if password==46789:
    print("Welcome to Our payment site.")
    w=True
    while w:
        s=input("How can we help you? [Check_balance,Deposit_Money,Withdraw_Money,Exit] ")
        if s=="Check_Balance":
            services.check_balance()
        elif s=="Deposit_Money":
            a=int(input("Enter Amount To Deposit :"))
            services.deposit_money(a)
        elif s=="Withdraw_Money":
            a=int(input("Enter Amount To Withdraw :"))
            services.withdraw(a)
        elif s=="Exit":
            services.exit()
            w=False
        else:
            print("Invalid Input")
else:
    print("Invalid Password !!!")

        
