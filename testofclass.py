class bank:
    def adduserinformation(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
        self.phno=int(input("enter your phone number"))
        self.accbal=int(input("enter your acc balance"))
    def deposit(self):
        cashhand=int(input("enter your cash in hand"))
        print(self.accbal+cashhand)    
    def withdraw(self):
        cashhand=int(input("enter your cash in hand"))
        print(self.accbal-cashhand)
    def balance(self):
        print("your acc balance is",self.accbal)
               
sharon=bank()
sharon.adduserinformation()
sharon.deposit()
sharon.withdraw()
sharon.balance()
    