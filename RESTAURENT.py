class Menu:
    def __init__(self, i, p):
        self.item = i
        self.price = p

    def display(self):
        print("PRODUCT:", self.item)
        print("PRICE:", self.price)

menu_list = []
print("                               **WELCOME**            ")
print("                          ! TO THE RESTAURENT !            ")

a = input("Press '1' if  you are an ADMIN\nOR\nPress '9' if you are  a USER\n:")

if a == '1':
    password = input("Enter the password for ADMIN :")
    print("-------------------------------------------------------------------------")
    if password == 'admin':
        print("                        Welcome to your PC, Admin!")
        print("-------------------------------------------------------------------------")
    else:
        print("Invalid password.")
        exit()

elif a == '9':
    password = input("Enter the password for USER :")
    if password == 'user':
        print("Welcome to your PC, User!")
        w=input("what would you want to do\n1.JUST take a look at the menu\nor\n2.Order")
        if w == '1':
            if not menu_list:
                print("SORRY NO MENU AVAILABLE")
            else:
                print("                                            MENU")
                print(menu_lsit)
    else:
        print("Invalid password.")
        exit()
else:
    print("Invalid selection.")
    exit()

# Admin Menu
while True:
    what = int(input("\nWhat would you like to do?\n1. ADD ITEMS\n2. DELETE ITEMS\n3. DISPLAY ITEMS\n4. UPDATE ITEMS\n5. EXIT\n:"))

    if what == 1:
        n = int(input("Enter the number of items you want to add: "))
        for i in range(n):
            item = input("Enter item name: ")
            price = input("Enter item price: ")
            new_item = Menu(item, price)
            menu_list.append(new_item)
            print(f"{n} has been succesfully added")


    elif what == 2:
        d = input("Which item would you like to delete: ")
        for i in menu_list:
            if i.item.lower() == d.lower():
                menu_list.remove(i)
                print(f"{d} has been deleted.")
                break
            
    elif what == 3:
        print("\nCurrent Menu:")
        for m in menu_list:
            m.display()

    elif what == 4:
        d = input("Which item would you like to update: ")
        for i in menu_list:
            if i.item.lower() == d.lower():
                new_price = int(input("Enter new price: "))
                i.price = new_price
                print(f"{d} updated to ₹{new_price}")
                break
        else:
            print("Item not found.")

    elif what == 5:
        print("Exiting Admin Menu.")
        break

    else:
        print("Invalid option. Try again.")
        
        
if a == '9':
    password = input("Enter the password for USER :")
    if password == 'i am the user':
        print("Welcome to your PC, User!")
        if not menu_list:
            print("Sorry, no menu items available yet.")
        else:
            print("\nMenu for you:")
            for m in menu_list:
                m.display()
    else:
        print("Invalid password.")
        exit()

