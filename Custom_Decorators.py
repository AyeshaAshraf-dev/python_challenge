# x = 'global x'

# def test():
#     y = 'local y'
#     print(y)

# test()
# without argu
# def outer_func():
#     message = "Hi"
#     def inner_func():
#         print(message)
#     return inner_func()

# my_func = outer_func

# print(my_func) 
# my_func()


#with argu
# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)
#     return inner_func

# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')



# hi_func()
# hello_func()

# #passing function as arguments

# def func1():
#     a = 34
#     b = 44
#     return a+b

# def run_twice(func2):
#     for i in range(2):
#         result=func2()
#         print(result)
  
# run_twice(func1)

#A Decorator is a function that extends the behavior of another function
#They dont change the base f
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

















def add_sprinkles(get_ice_cream):
    def wrapper(*args,**kwargs): #To accept any arguments
        print("*You add sprinkles!*")
        get_ice_cream(*args,**kwargs)
    return wrapper

def fudge(get_ice_cream):
    def wrapper(*args,**kwargs): #To accept any arguments
        print("*You add fudge!*")
        get_ice_cream(*args,**kwargs)
    return wrapper

@add_sprinkles
@fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} flavour ice cream!")

get_ice_cream("vanila")




