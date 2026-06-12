#calculating area of square rectangle & triangle
print("What type of calculation you want to do:")

user_ty = int(input ("1 = Square, 2 = Rectangle, 3 = Triangle: "))

if user_ty == 1:
    side = float(input("Enter Side value: "))
    sq_area = side*side
    print(sq_area)
elif user_ty == 2:
    length = float(input("Length: "))
    width = float(input("width: "))
    re_area = length*width
    print(re_area)
else:
     base = float(input("Base: "))   
     height = float(input("height: "))
     tr_area = 1/2*base*height
     print(tr_area)

print("Thanks for using this calculator :)")     













