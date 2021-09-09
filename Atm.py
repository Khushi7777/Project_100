class Atm:
    def_init_(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self pin = pin
    
    def check_balance(self):
        print("Your balance if 50000")

    def withdrawl(self,amount):
        new_amount = 50000-amount
        print("You have withdrawn amount "+str(amount)+". Your remaining balance is "+ str(new_amount))

    
    def main():
        Card_number = input("Insert you card number :- ")
        Pin_number = input("Insert your pin number :- ")

        new_user = Atm(Card_number, Pin_number)

        print("Choose your activity")
        print("1.Balance Enquiry or 2. Withdrawl")
        activity = int(input("Enter activity number :- "))

    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("Enter the amount :- "))
    else:
        print("Enter a valid number")

if_name_ == "_main_":
    main()