import random
class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.balance=random.randrange(10000,100000,1)

    def checkbalance(self):
        print("Your balance is ₹"+str(self.balance))

    def withdrawal(self,amount):
        amount2 = self.balance - amount
        print("You have withdrawn amount ₹"+str(amount) +". Your remaining balance is ₹"+ str(amount2))


def main():
    cardnumber = input("Enter your card number:- ")
    pin  = input("Enter your Pin:- ")

    user =  Atm(cardnumber ,pin)

    print("Choose your action ")
    print("1.Balance Enquiry   2.Withdrawal")
    action = int(input("Enter Action number :- "))

    if (action == 1):
        user.checkbalance()
    elif (action == 2):
        amount = int(input("Enter the amount:- "))
        user.withdrawal(amount)
    else:
        print("Enter a valid action number.")

if __name__ == "__main__":
    main()
