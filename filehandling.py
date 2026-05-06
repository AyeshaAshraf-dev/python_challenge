# how to open a file

# file = open('/home/ayesha-ashraf/Downloads/python_challenge-main/filehandling.txt','r')
# content = file.read()
# print(content)

# file = open('/home/ayesha-ashraf/Downloads/python_challenge-main/filehandling.txt','w')
# content = input('Enter data! ')
# file.write(content)
# print("Data saved")
# file.close()
# print(content)

file = open('/home/ayesha-ashraf/Downloads/python_challenge-main/filehandling.txt','a')
content = input('Enter data! ')
file.write(content)
print("Data saved")
print(content)
file.close()