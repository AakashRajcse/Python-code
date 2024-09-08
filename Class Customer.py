class Customer:
    cus_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):  #self =1000
        Customer.cus_list.append(self)
    def searchCustomer(self):  #self 9000
        for e in Customer.cus_list:    #e=1000,e==2000
            if(e.id==self.id):
                self.name=e.name    #self.name=ri=ohit,9000
                self.age=e.age
                self.mob=e.mob
                return
    def deleteCustomer(self):   #self=10000,self.id=20,self.name=0,self.age=0,self.mob=0
        for e in Customer.cus_list:      #e=1000,e=200
            if(e.id==self.id):
                Customer.cus_list.remove(e)
                return
    def modifyCustomer(self):  #self =11000,self.id=30,self.name=Raju,self.age=31,self.mob=5432
        for e in Customer.cus_list:   #1000
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return



#PL
print("Welcome to CETPA's CMS")
def showCustomer(cus):
    print("cus.ID:",cus.id,"Cust.Name:",cus.name,"Cust Age:",cus.age,"Cust.Mob:",cus.mob)
def getMob():
    while(1):
        mob=input("Enter Mob no:")
        if(mob.isdecimal()):
            if(len(mob)==10):
                return mob
            else:
                print("Enter Mob No of 10 Digits only")

        else:
            print("Enter mob no with digit only")
while(1):
    cus=Customer()
    ch=input("Enter Choice: 1 for Add Cust,2 Search,3 Delete, 4 Modify, 5 Display all,6 Exit:")
    if(ch=="1"):
        cus.id=input("Enter cust ID:")  #10
        cus.name=input("Enter cust Name:")   #aakash
        cus.age=input("Enter cust Age:")  #19
        cus.mob=getMob()
        cus.addCustomer()
        print("Customer Added Successfully")
    elif(ch=="2"):   #Search Customer
        cus=Customer()   #cus address
        cus.id=input("Enter cust ID to search:")
        cus.searchCustomer()
        showCustomer(cus)   #showCustomer(90000)
    elif(ch=="3"):   #Delete Customer
        cus=Customer()    #cus address 10000
        cus.id=input("Enter Cust ID:")  #cus.id 20
        cus.deleteCustomer()
        print("Customer Deleted Successfully")
    elif(ch=="4"):   #Modify Customer
        cus=Customer()  #cus adress 11000
        cus.id=input("Enter Cust ID:")  #cus.id=30
        cus.name=input("Enter Cust updated name:")  #cus.name=Raju
        cus.age=input("Enter Cust updated age:")  #cus.age=31
        cus.mob=input("Enter Cust updated mob")  #cus.mob=54329
        cus.modifyCustomer()
        print("Customer Modify Successfully")
    elif(ch=="5"):   #Display All Customer
        for e in Customer.cus_list:
            showCustomer(e)
    elif(ch=="6"):  #Exit
        print("Thanks for using CETPA's CMS")
    else:
        print("Incorrect Choice")

