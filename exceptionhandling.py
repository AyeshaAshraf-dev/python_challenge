try:
    file = open('/home/ayesha-ashraf/Downloads/python_challenge-main/inheritance.py')
    content = file.read()
    print(content)

except FileNotFoundError:
    print('file not found')

finally:
    file.close()
    print("file closed")