class Converter:
    def __init__(self, r):
        self.rupees = r

    def to_yen(self):
        ans = self.rupees * 1.76
        print(f"{self.rupees} = {ans}")

    def to_dollars(self):
        ans = self.rupees * 0.012
        print(f"{self.rupees} = {ans}")

    def to_pounds(self):
        ans = self.rupees * 0.0095
        print(f"{self.rupees} = {ans}")

print("                            WELCOME TO CURRENCY CONVERTER ")
amount = float(input("Enter amount in Rupees:  "))


c = Converter(amount)


print("\nWhat do you want to convert to?")
print("1. Yen")
print("2. Dollars")
print("3. Pounds")
choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    c.to_yen()
elif choice == "2":
    c.to_dollars()
elif choice == "3":
    c.to_pounds()
else:
    print("Invalid choice ")
