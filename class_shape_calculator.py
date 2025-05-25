class Shape:
    square=0
    rectangle=0
    circle=0
    triangle=0
    
    def __init__(self):
        self.answer = 0

    def square(self, s):
        self.answer = s ** 2
        print("Area of square:", self.answer)

    def rect(self, l, b):
        self.answer = l * b
        print("Area of rectangle:", self.answer)

    def tri(self, b, h):
        self.answer = 0.5 * b * h
        print("Area of triangle:", self.answer)

    def circle(self, r):
        self.answer = 3.14 * r ** 2
        print("Area of circle:", self.answer)
    
    def perimeter_square(self, s):
        self.result = 4 * s
        print("Perimeter of square:", self.result)

    def perimeter_rectangle(self, l, b):
        self.result = 2 * (l + b)
        print("Perimeter of rectangle:", self.result)

    def perimeter_triangle(self, a, b, c):
        self.result = a + b + c
        print("Perimeter of triangle:", self.result)

    def perimeter_circle(self, r):
        self.result = 2 * 3.14 * r
        print("Perimeter of circle:", self.result)



c = Shape()

ap=input("Do you want to calculate Area or Perimeter:").lower()

if ap=="area":
    choice = input("Select a shape:\n1.square\n2.rectangle\n3.triangle\n4.circle\n: ").lower()
    
    if choice == '1' or choice == 'square':
        side = int(input("Enter the side of the square: "))
        c.square(side)

    elif choice == '2' or choice == 'rectangle':
        l = int(input("Enter the length: "))
        b= int(input("Enter the breadth: "))
        c.rect(l, b)

    elif choice == '3' or choice == 'triangle':
        a = int(input("Enter the base: "))
        b = int(input("Enter the height: "))
        c.tri(a, b)

    elif choice == '4' or choice == 'circle':
        r = int(input("Enter the radius: "))
        c.circle(r)

    else:
        print("Invalid choice.")
        


elif ap=="perimeter":
    choice = input("Select a shape:\n1. square\n2. rectangle\n3. triangle\n4. circle\n: ").lower()
   
    if choice == '1' or choice == 'square':
        side = int(input("Enter the side of the square: "))
        c.perimeter_square(side)

    elif choice == '2' or choice == 'rectangle':
        l = int(input("Enter the length: "))
        b= int(input("Enter the breadth: "))
        c.perimeter_rectangle(l, b)

    elif choice == '3' or choice == 'triangle':
        a = int(input("Enter the base: "))
        b = int(input("Enter the height: "))
        c = int(input("Enter the height: "))
        c.perimeter_triangle(a, b, c)

    elif choice == '4' or choice == 'circle':
        r = int(input("Enter the radius: "))
        c.perimeter_circle(r)

    else:
        print("Invalid choice.")
    


