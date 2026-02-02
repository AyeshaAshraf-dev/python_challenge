import random
import string


# s1 = string.ascii_lowercase
# s2  = string.ascii_uppercase
# s3 = string.digits
# s4 = string.punctuation
pas1 = input("Enter the length of password: ")
if  pas1.isdigit():
    s1 = string.ascii_lowercase
    s2  = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    pass2 = int(pas1)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # print(s)
    random.shuffle(s)
    print("4".join(s[0:pass2]))
# print(s4)
else:
    print("INVALID, ONLY INTEGER!")
# print(s1)

# print(s4)