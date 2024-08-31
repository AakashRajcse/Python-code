# BLL: Business Logic Layer
customers = []

def addCustomer(id, name, age, mob):
    customer = {
        "id": id,
        "name": name,
        "age": age,
        "mob": mob
    }
    customers.append(customer)
    return

def searchCustomer(id):
    for index, customer in enumerate(customers):
        if customer["id"] == id:
            return index
    return None  # Return None if the customer is not found

def deleteCustomer(id):
    index = searchCustomer(id)
    if index is not None:
        customers.pop(index)
        return True
    return False  # Return False if the customer is not found

def modifyCustomer(id, name, age, mob):
    index = searchCustomer(id)
    if index is not None:
        customers[index]["name"] = name
        customers[index]["age"] = age
        customers[index]["mob"] = mob
        return True
    return False  # Return False if the customer is not found


# PL: Presentation Layer
def showCustomer(i):
    print("Cust ID:", customers[i]["id"], "Cust Name:", customers[i]["name"],
          "Cust Age:", customers[i]["age"], "Cust Mob:", customers[i]["mob"])

print("Welcome to Aakash Management System")
while True:
    choice = input("Enter choice: 1 for Add cust, 2 Search, 3 Delete, 4 Modify, 5 Display all, 6 For Exit: ")
    if choice == "1":  # Add New Customer
        id = input("Enter Cust ID: ")
        name = input("Enter Cust Name: ")
        age = input("Enter Cust Age: ")
        mob = input("Enter Cust Mob: ")
        addCustomer(id, name, age, mob)
        print("Customer Added Successfully")
    elif choice == "2":  # Search Customer
        id = input("Enter Cust Id to Search: ")
        i = searchCustomer(id)
        if i is not None:
            showCustomer(i)
        else:
            print("Customer Not Found")
    elif choice == "3":  # Delete Customer
        id = input("Enter Cust ID to Delete: ")
        if deleteCustomer(id):
            print("Customer Deleted Successfully")
        else:
            print("Customer Not Found")
    elif choice == "4":  # Modify Customer
        id = input("Enter Cust ID to Modify: ")
        name = input("Enter Cust updated Name: ")
        age = input("Enter Cust updated Age: ")
        mob = input("Enter Cust updated Mob: ")
        if modifyCustomer(id, name, age, mob):
            print("Customer Modified Successfully")
        else:
            print("Customer Not Found")
    elif choice == "5":  # Display All Customers
        if customers:
            for i in range(len(customers)):
                showCustomer(i)
        else:
            print("No Customers Available")
    elif choice == "6":  # Exit
        print("Thanks for using Aakash CRM")
        break
    else:
        print("Incorrect Choice")
