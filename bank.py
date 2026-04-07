import time
import random
bank=["HSBC","NBE","CIB"]
random=random.choice(bank)
from time import sleep
def print_pause(text):
    print(text)
    sleep(2)
def intro():
    print ("hello our dear customer")
    name = input("Please enter your name: ")
    print("Hello, " + name + "! Good to see you.")
    email = input("pleas enter your e-mail ")
    print("ok let's see what can help you")
    password =input("please enter your password")
    balance ={"balance":0}
    def create_acc():
        balance["balance"] += int(input("how mash you want to deposit?"))
        def show_balance():
          print("your current balance:",balance["balance"])
          def deposit():
                print("please enter the amount that you want to deposit!")
                balance["balance"]+=int(input("add to balance:"))
                print("your current balance,:",balance["balance"])
                def withdraw():
                    print("pleace enter what do you want to withdarw!")
                    money_withdraw =int(input("subscract to balance:"))
                    while money_withdraw> balance["balance"]:
                        print("erorr,your balance has",balance["balance"])
                        print("try a number less than your current balance ")
                        print("please enter the amount that you want to withdrow")
                        money_withdraw = int(input("substract to balance:"))
                        balance["balance"]-= money_withdraw
                        print("your corrent balance:",balance["balance"])
                        print(f"walcom to {bank} banke app")
                        user_choice=input("whould you to creat new account?,(y/n)")
                        choice_y="ok let's creat your account! " 
                        choice_n="walcome to {bank} bank app, Come back anytime. We will always be waiting for you. See you later!"
                        while user_choice not in ["y","n"]:
                            user_choice=input("enter y,n:")
                            if user_choice =="y":
                                print (choice_y)
                                intro()
                                while user_choice =="n":
                                    print(choice_n)
                                    break
if __name__ == "__main__":
    intro()