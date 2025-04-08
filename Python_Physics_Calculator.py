import math
print("Hello Welcome to Basic Physics Calculator!")
print("A. CALCULATING THE CIRCUMFERENCE OF A CIRCLE")
print("B. CALCULATING THE AREA OF A CIRCLE")
print("C. FINDING THE HYPOTENUSE OF THE RIGHT TRIANGLE")
options = input("Choose an option (A, B, or C): ")

while options not in ['A', 'B', 'C']:
    options = input("Choose only in option (A, B, or C): ")

if options == 'A':
    while True:
         radius = (input("Enter the radius of a circle: "))
         try:
            radius = float(radius)  
            break 
         except ValueError:
            print("INVALID! Please Number only.")
    circumference = 2 * math.pi * radius
    print(f"the circumference is: {round(circumference, 3)}cm" )

elif options == 'B':
    while True:   
       radius = (input("Enter the radius of a circle:"))
       try:
           radius = float(radius)  
           break 
       except ValueError:
            print("INVALID! Please Number only.")
    area = math.pi * pow(radius, 2)
    print(f"The area of a circle is: {round(area, 3)}cm^2")
    
elif options == 'C':
    while True:
     A = input("Enter side A: ")
     try:
        (A) = float(A)
        print(f"Side A is valid: {A}")  
        break 
     except ValueError:
        print("INVALID A! Please Enter Number: ")
    while True:
     B = input("Enter side B: ")
     try:
        (B) = float(B)
        print(f"Side B is valid: {B}")  
        break 
     except ValueError:
        print("INVALID B! Please Enter Number: ")

    C = math.sqrt(pow(A, 2) + pow(B, 2))
    print(f"Side C = {C}")
    
else:
     print("INVALID")
