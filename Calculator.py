#calculator with python
 
print ("Operation option:\n1. Add (+)\n2. Subtract (-)\n3. multiplication (x)\n4. Division (/)")
user_inp = int(input("\nEnter the operation you want to do as number : "))

def Add():
    # add = 0
    list = []
    inp = int(input("How many element you want to sum ? :"))
    for i in range (inp):
        num = int(input("Number to add:"))
        list.append(num)
    sum_add = sum(list)
    print ("\nSum of umber", list, " is ", sum_add)



def Subtract():
    print ("-")

def Multiply():
    print ("x")

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