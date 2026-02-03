# Write a Python function that accepts two integer numbers. If the product of the
# two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
import sys



def convertion(num1,num2):
    product = num1*num2
    nom = num1+num2
    if product <= 1000:
        print("**********PRODUCT*********")
        print("The product is:", product)
        return product
    else:
        print("**********SUM*********")
        print("The sum is:", nom)
        return nom  
int1 = input("Enter 1st num \n")
if not int1.isdigit() :
    print("ERROR : ONLY INTEGERS!")
else:
    int2 = input("Enter 2nd num \n")
    if not int2.isdigit() :
        print("ERROR : ONLY INTEGERS!")
        sys.exit()
    in3 = int(int1)
    in4 = int(int2)    
    des = convertion(in3,in4)

    