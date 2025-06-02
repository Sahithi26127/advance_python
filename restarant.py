# !!EAT UP!!

name = input("Enter your name :")
print("\nHey", name, "welcome to !!EAT UP.com.in.co.yahoo.gmail!!")
print("\nConfused where to waste money?")
print("\nDon't worry i will suggest you!!")

cui = input("\nWhich type of cuisine would you prefer\n1. INDIAN\n2. KOREAN\n3. ITALIAN\n:").lower()
time = int(input("\nWhen will you book a reservation? (Choose between 11AM to 2PM)\n:"))

print("=====================================================================")

if cui == "indian" or cui == "1":
    if time == 11:
        print("Get ready for Namaste Flavors!")
    elif time == 12:
        print("Enjoy Bollywood Bites!")
    elif time == 1:
        print("Time for Tandoori Trails!")
    elif time == 2:
        print("Try Curry Corner!")

elif cui == "korean" or cui == "2":
    if time == 11:
        print("How about Tteokbokki Town")
    elif time == 12:
        print("Seoul Spoon for the win!")
    elif time == 1:
        print("Seoul Bites sounds yum!")
    elif time == 2:
        print("End with K-Taste Junction!")

elif cui == "italian" or cui == "3":
    if time == 11:
        print("Start with Mamma Mia!")
    elif time == 12:
        print("Try Spaghetti Street!")
    elif time == 1:
        print("Roma Roots!")
    elif time == 2:
        print("Pasta Palazzo!")

else:
    print("Sorry, that cuisine isn't available right now.")

print("=====================================================================")
print("******** BON APPÉTIT,", name, "! ********")
