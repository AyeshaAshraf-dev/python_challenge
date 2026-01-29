import sys

#1. First he take currency then go to keys in ditionary 
#2. matches th values if not shows error.
#3. if yes it would excute the logic 
#4. logic would be Amount*divtionaryvalues

prices = {
    "USD"    :   0.0036,	
    "EUR"	 :   0.0030,	
    "GBP"	 :   0.0026,  
    "INR"	 :   0.33,
    "AUD"    :	0.0050,
    "CAD"    :  0.0048,	
    "SA"     :   0.0133,	
    "AED"	 :   0.0131,
    "JPY"    :   0.55,
}
def convertion(amount, currency):
    if currency not in prices.keys():
        print("Invalid: Not supported")
        sys.exit()
    else:
        thing = prices[user_curr] 
        amount1 = user_amount*thing   
        return amount1

user_amount = int(input("Enter value: "))
print("Available currencies are ", prices.keys())
user_curr  =  input("Enter currency: ").upper()
final = convertion(user_amount,user_curr)
print(f"The Converted Value is : {final}")