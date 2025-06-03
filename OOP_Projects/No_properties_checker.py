class Checker:
    def __init__(self,number):
        self.number=number
    def even_odd(self):
        if self.number%2==0:
            print("Even Number.")
        else:
            print("Odd Number.")
    def prime_checker(self):
        c=0
        for i in range(1,self.number+1):
            if self.number%i==0:
                c+=1
        if c==2:
            print("Prime Number.")
        else:
            print("Not a Prime Number.")
    def factorial(self):
        if self.number==0:
            print(f"Factorial of {self.number} is 1.")
        elif self.number<0:
            print("Given No. has no Factorial.")
        else:
            n=1
            for i in range(1,self.number+1):
                n*=i
            print(f"Factorial of {self.number} is {n}.")
    def exit(self):
        print("Thanks for using this checker.")
while True:
    n=int(input("Enter Number :"))
    checker=Checker(n)
    checker.even_odd()
    checker.prime_checker()
    checker.factorial()
    p=input("Wants to Exit[Yes/No] : ")
    if p.lower()== "yes":
        checker.exit()
        break



