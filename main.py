class CinemaHall:
    def __init__(self,r,c):
        self.r = r
        self.c = c
        self.matrix=[]
        self.userInfo={}
        self.bookedSeat=0
        self.currentIncome=0
        self.totalIncome=self.totalIncomeCalc()
        self.createSeat()
      
    def createSeat(self):
        self.matrix = []
        self.matrix.append([" "]+[i for i in range(1,self.c+1)])
        for i in range(1,self.r+1):
            self.matrix.append([i]+["S" for i in range(1,self.c+1)])
    def showSeat(self):
        for i in self.matrix:
            for j in i:
                print(j,end=" ")
            print()
    def bookSeat(self):
        R = int(input("enter row number :-"))
        C = int(input("enter column number :-"))
        if self.isBooked(R,C):
            print("Aready Booked")
        else:
            price=self.price(R,C)
            print("Price of ticket: ",price)
            choice = int(input("1.Yes 2.No \n"))
            if choice == 1:
                tempDict={}
                tempDict["Name"] = input("Name: ");    
                tempDict["Gender"] = (input("Gender: "))    
                tempDict["Age"] = int(input("Age: "))    
                tempDict["Phone"] = int(input("Phone:"))
                tempDict["Price"] = price
                self.userInfo[str(R)+str(C)] = tempDict
                self.matrix[R][C]="B"
                self.bookedSeat+=1
                self.currentIncome+=price
                print("Booked Successfully")
    def isBooked(self,R,C):
        return self.matrix[R][C]=="B"
    def price(self,R,C):
        if (self.r-1)*(self.c-1)<60 or R<=(self.r-1)//2:
            return 10
        else:
            return 8
    def printUserInfo(self):
        R = int(input("enter row number :-"))
        C = int(input("enter column number :-"))
        if self.isBooked(R,C):
            temp=self.userInfo[str(R)+str(C)]
            for key, value in temp.items():
                print(key, ':', value)
        else:
            print("Seat not Booked")
            
    def NumberOfPurchasedTicket(self):
        return self.bookedSeat
    def Per_Booked_Tickets(self):
        return float((self.bookedSeat/((self.r)*(self.c)))*100)
    def Current_income(self):
        return self.currentIncome
    def totalIncomeCalc(self):
        if self.totalseat()<=60:
            return self.totalseat() * 10
        else:
            return ((((self.r//2)*10) + (((self.r)-(self.r//2))*8)) * self.c)
    def totalseat(self):
        return self.r*self.c
    def statistics(self):
        print("Number of Purchased Tickets:",self.NumberOfPurchasedTicket(),"\n")
        print("Percentage of Tickets booked:",'%.2f'%self.Per_Booked_Tickets(),"%\n")
        print("Current Income: $",self.Current_income(),"\n")
        print("Total Income: $",self.totalIncomeCalc())
        
r = int(input("Enter no of rows:"))
c = int(input("Enter no of seats in each row:"))
three_idiots = CinemaHall(r,c)
while True:
    choice = int(input('''Please choose from Options mentioned below:
        1. Show the seats
        2. Buy a ticket
        3. Stastistics
        4. Show booked Tickets User Info
        0. Exit
        '''))
    if choice == 1:
        print("Cinema:")
        three_idiots.showSeat()
    elif choice == 2:
        three_idiots.bookSeat()
    elif choice == 3:
        three_idiots.statistics()
    elif choice == 4:
         three_idiots.printUserInfo()
    elif choice == 0:
         print("Thanks for your input.\nQuitting the process")
         break  
    elif int(choice) > 4:
         print("Please type numbers from 0 to 4")
    else:
         print("Only numbers are accepted. Please select right option")