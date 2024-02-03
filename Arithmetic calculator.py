print(" !!! Calculator !!!")
while True:
    x=eval(input("Enter first Number : "))
    y=eval(input("Enter Second Number : "))
    print("1.Addition\
      \n2.substraction\
      \n3.Multiplication\
      \n4.Division")
    choice=int(input("Enter Choice (1-4)"))
    if choice>=1 and choice<=4:
        if choice==1:
            print(f"Addition ={x+y}")
        elif choice==2:
            print(f"Substraction ={x-y}")
        elif choice==3:
            print(f"Multiplication = {x*y}")
        else:
            print(f"Division = {x/y}")
    else:
        print("Invalid Input")
