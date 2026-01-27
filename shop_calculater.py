# write a program in which the shopkeeper keeps enter on nummbers and then u have to add 
# and give a total value 

# psuodo code:

# !. i would tell him to enter a Value
# 2. i would store that value in a box a place  
# 3. now i would run loop which take every value from thart box and sum it (+operater)
# 4. last step i would print output to that shopkeeper output:

number  = 0
boxs = []
while True:
    user_input = input("Enter the price (q for quit) : \n")
    if user_input != 'q' :
        box= int(user_input)
        number = number + int(user_input)
        boxs.append(box)
        print(f"Bill so far {number}")
    else:
        print(f"Total Bill: {number}")     
        print("------BILLSUMMMARY------")   
        for i,b in enumerate(boxs, start=1):
            print(f"item{i} : {b}")
        print("--------THANKS---------")    
        break