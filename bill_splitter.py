# i will ask abt total rent
# total electricity bill
# gass bill
# grocery bill
# additional like ordered etc

def get_valid_amount(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid Input! Try again!")
            
total_rent = get_valid_amount("Enter the total amount of Rent :\n")
electricity_bill = get_valid_amount("Enter the total amount of Electricity Bill :\n")
Gass_bill = get_valid_amount("Enter the total amount of Gass Bill : \n")
Grocery_bill = get_valid_amount("Enter the total amount of Grocery Bill : \n")
p1 = total_rent+Grocery_bill+electricity_bill+Gass_bill
while True:
    Additional = input("If u want to add aditional amount! (Y/N) : \n").upper()
    if Additional == "Y":
        a2 = get_valid_amount("Enter the amount : \n")
        p1 += a2
    elif Additional == "N":
        break
    else:
       print("Invalid choice! type y or n")
    
person = get_valid_amount("How many roomates do u have?(Only roomates) : \n")
if person == 0:
    person = 1

total_bill = (p1) // (person+1)

print("------------BillSplit--------------")
print(f"Ttotal Bill : {total_bill:,.2f}")
print(f"Each person would pay ${total_bill:,.2f}")
