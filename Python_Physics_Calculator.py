import math
print("Hello Welcome to Basic Physics Calculator!")
print("A. CALCULATING THE CIRCUMFERENCE OF A CIRCLE")
print("B. CALCULATING THE AREA OF A CIRCLE")
print("C. FINDING THE HYPOTENUSE OF THE RIGHT TRIANGLE")
options = input("Choose an option (A, B, or C): ")

if options == 'A':
   radius = float(input("Enter the radius of a circle: "))
   circumference = 2 * math.pi * radius
   print(f"the circumference is: {round(circumference, 3)}cm" )

elif options == 'B':
    radius = float(input("Enter the radius of a circle:"))
    area = math.pi * pow(radius, 2)
    print(f"The area of a circle is: {round(area, 3)}cm^2")
    
elif options == 'C':
    A = float(input("Enter side A: "))
    B = float(input("Enter side B: "))
    c = math.sqrt(pow(A, 2) + pow(B, 2))
    print(f"Side C = {c}")

else:
     print("INVALID OPTION, PLEASE RETRY")
