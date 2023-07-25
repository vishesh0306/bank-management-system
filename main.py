existing_user_list = ["vishesh", "shivam", "rajni", "vishal"]
existing_user_password = ["vish2003", "shiv2006", "raj78", "vish76"]
existing_user_balance = [20000,40000,5000,1000000]

class BankReception:
    def __init__(self,name):
        self.name = name
        print(f"\n\t\t WELCOME {self.name} TO OUR BANK RECEPTION\n")
        self.tell = int(input(
"""Enter 1: if you are a New user 
Enter 2: to login existing new account 
Enter 3: to change your password
Enter your choice: """))

        if self.tell == 1:
            self.Signup()
        elif self.tell == 2:
            self.Login()
        elif self.tell == 3:
            self.change_password()

        else:
            print("Wrong input\n")


    def Signup(self):
        print("\n\t\t SIGNUP PAGE\n")
        self.name = input("Enter your name : ")
        if(self.name in existing_user_list):
            print("Account Already Registered")
            BankReception(self.name)

        self.password = input("Enter your password: ")

        existing_user_list.append(self.name)
        existing_user_password.append(self.password)
        existing_user_balance.append(0)


        print("New account created :) \n")
        print("Now go back to login page to login your account \n")
        self.Login()


    def Login(self):
        print("\n\t\t LOGIN PAGE\n")
        self.name = input("Enter your name : ")
        self.password = input("Enter your password: ")

        if self.name in existing_user_list:
            index = existing_user_list.index(self.name)
            if self.password == existing_user_password[index]:
                print(f"Welcome {self.name}")
                self.loged = True
            else:
                print("Wrong password\n")
                self.loged = False

        else:
            print("Account not found \n")
            self.loged = False

    def change_password(self):
        print("To change your password, firstly Login Your account")
        self.Login()
        if self.loged == True:
            index = existing_user_list.index(self.name)
            self.new_password = input("Enter new password : ")
            existing_user_password[index] = self.new_password
            print("Password changed :) ")
            print("New password is : ",existing_user_password[index])


class BankAccounts(BankReception):

    def __init__(self,name):
        self.name = name
        print(f"Welcome {self.name} to Bank Accounts")
        self.tell = int(input(
"""Enter 1: to deposit money
Enter 2: to withdraw money
Enter 3: to tranfer money 
Enter 4: to check balance
Enter your choice: """))

        if self.tell == 1:
            self.deposit()
        elif self.tell == 2:
            self.withdraw()
        elif self.tell == 3:
            self.transfer()
        elif self.tell == 4:
            self.balance()
        else:
            print("Wrong input\n")


    def deposit(self):
        super().Login()
        if self.loged == True:
            index = existing_user_list.index(self.name)
            self.money = int(input("Enter money to add : "))
            existing_user_balance[index] += self.money
            print("Money deposited :) ")

            print(existing_user_balance)


    def withdraw(self):
        super().Login()
        if self.loged == True:
            index = existing_user_list.index(self.name)
            self.money = int(input("Enter money to withdraw : "))

            if existing_user_balance[index] >= self.money:

                existing_user_balance[index] -= self.money
                print("Money withdrawed :) ")

            else:
                print("Low Account Balance, Can't withdraw money")

            print(existing_user_balance)

    def transfer(self):
        super().Login()
        if self.loged == True:
            index = existing_user_list.index(self.name)

            self.second_person = input("Enter name of person you are transfering money : ")

            if self.second_person in existing_user_list:
                self.index2 = existing_user_list.index(self.second_person)
                self.money = int(input("Enter money to transfer : "))

            else:
                print("Person account not found")
                return 0


            if existing_user_balance[index] >= self.money:

                existing_user_balance[index] -= self.money
                existing_user_balance[self.index2] += self.money
                print("Money transfered :) ")

            else:
                print("Low Account Balance, Can't transfer money")

            print(existing_user_balance)

    def balance(self):
        super().Login()
        if self.loged == True:
            self.index = existing_user_list.index(self.name)
            print(f"Your Balance is : {existing_user_balance[self.index]}")

class Welcome_to_Bank(BankAccounts):

    def __init__(self,name):
        self.name = name

        print(f"\t\t WELCOME {self.name} TO OUR BANK\n")
        self.tell = int(input(
"""Enter 1: to visit Reception 
Enter 2: to visit Accounts office 
Enter your choice: """))

        if self.tell == 1:
            BankReception(self.name)    #   OR     Bank_Reception.__init__(self)
        elif self.tell == 2:
            BankAccounts(self.name)    #   OR     Bank_Accounts.__init__(self)

        else:
            print("Wrong input\n")



name = input("Enter your name :")
print()
name = Welcome_to_Bank(name)