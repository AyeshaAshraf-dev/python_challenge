import math 

# calculate the factorial of the given numbers.
# Find the number of trailing zerors in that num



                    # tried loop approch
# n = 0
# num = input("Enter the number: ")
# while True:
#     num = int(num)**n
#     if (num == 1) or (num == 0):
#         print("1")
#     else:
#         print(f"The answer is : {num}")
#         break

                     # recursive approch
           
def factorial(n):
    if isinstance(n, str):
            raise ValueError("Facorial is only for integer!" )
    if n<0:
            raise TypeError("Positive integers only!")
    if (n==1) or (n==0):
        return 1
    else:
        return n * factorial(n-1) 
# Trailingzeros Psuodo code
#  1. First i wiil define a box. 
#  2. i will use the concept of 5 n//5,  tThe problem is hidden 5.
#  3. For that i have to use concept of multiples of 5 i.e 5,25,75 etc. 
#  4. I would put my ans in that defined box.



def trailingzeros(n):
    count = 0
    i = 5
    while (n // i >= 1):
         count += n//i
         i = i*5
    return count


note = 9
result = trailingzeros(note)
result2 = factorial(note)    
print(f"The factorial of {note} is {result2} ")
print(f"The trailing zero of factorial {note} : {result} ")
