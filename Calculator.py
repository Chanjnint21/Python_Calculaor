#calculator with python

print ("Operation option:\n1. Add (+)\n2. Subtract (-)\n3. Multiplication (x)\n4. Division (/)")
user_inp = int(input("\nEnter the operation you want to do as number : "))

def Add():
    list = []
    inp = int(input("How many element you want to sum ? :"))
    for i in range (inp):                      
        num = int(input("Number to add:")) # will ask the user to type the number base on the value input by user (inp)
        list.append(num)      # .append() add the element that type by the user into list
    Add = sum(list)    # sum() is the funtion that can use to sum all the number value in list 
    print ("\nSum of number", list, " is ", Add)

def Subtract():
    list = []
    inp = int(input("How many element you want to sabtract ? :"))
    print("\n***Plz enter the (-) in front of the the negative value !!") # put - infront of number because even we sum 
    for i in range (inp):
        num = int(input("Number to subtract:"))
        list.append(num)
    sub = sum(list)
    print ("\nSabtract of number", list, " is ", sub)

def Multiply():
    list = []
    multiply = 1
    inp = int(input("How many element you want to do multiplication? :"))
    for i in range (inp):
        num = int(input("Number to subtract:"))
        list.append(num)
    for num in list :
        multiply = multiply * num 
    print ("\nThe Multiply of number", list, " is ", multiply)


def Divide():
    print ("/")

if user_inp == 1 :
    Add()
elif user_inp == 2 :
    Subtract()
elif user_inp == 3 :
    Multiply()
elif user_inp == 4 :
    Divide()