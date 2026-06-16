class rectangle():
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def parameter(self):
        return (2*self.length)+(2*self.width)


# class square():
#     def __init__(self,length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length*self.length
#     def perimeter(self):
#         return 4*self.length
class square(rectangle):
    def __init__(self,length):
        super().__init__(length,length)

class cube(square):
    def surface_area(self):
        Face_area = super().area()
        return Face_area*6
    def volume(self):
        face_area = super().area()
        return face_area * self.length





obj1  = rectangle(33,22)
print(obj1.area())

# obj2  =  square(33,22)
# print(obj2.area())
obj2 = square(5)
print(obj2.area())
print(obj2.parameter())
 
obj3 = cube(5)
print(obj3.area())
print(obj3.parameter())
