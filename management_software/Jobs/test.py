# # Python program showing

# # abstract base class work

  

# from abc import ABC, abstractmethod

  

# class Polygon(ABC):

  

#     # abstract method

#     def noofsides(self):

#         pass

  

# class Triangle(Polygon):

  

#     # overriding abstract method

#     def noofsides(self):

#         print("I have 3 sides")

  

# class Pentagon(Polygon):

  

#     # overriding abstract method

#     def noofsides(self):

#         print("I have 5 sides")

  

# class Hexagon(Polygon):

  

#     # overriding abstract method

#     def noofsides(self):

#         print("I have 6 sides")

  

# class Quadrilateral(Polygon):

  

#     # overriding abstract method

#     def noofsides(self):

#         print("I have 4 sides")

  

# # Driver code

# R = Triangle()

# R.noofsides()

  

# K = Quadrilateral()

# K.noofsides()

  

# R = Pentagon()

# R.noofsides()

  

# K = Hexagon()

# K.noofsides()


# def add(x, y, z = 0): 

#     return x + y+z

  

# # Driver code 

# print(add(2, 3))

# print(add(2, 3, 4))



# test = "I am working at Revolent."

# print (test.split(" "))




# def primes(up_to):
#     result = []
#     for n in range(2, up_to):
#         for x in range(2, n):    # (A)
#             if n % x == 0:       # (B)
#                 break            # (C)
#         else:                # (D)
#             result.append(n)
#     return result

# print(primes(10))



# def append_five(list=[]):
#     list.append(5)
#     return list

# for i in range(5):
#   first_list = append_five() 
#   second_list = append_five([])

# print(first_list)
# print(second_list)



# x = 2
# print("%s" % (x == 2))





# class Person:
#     #__slots__ = ['name','__dict__']        #(A)
#     __slots__ = ['name']                   #(B)

#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     __slots__ = ['studied_course']         #(C)
#     #__slots__ = ['name', 'studied_course'] #(D)

#     def __init__(self, name, studied_course):
#         self.studied_course = studied_course
#         self.name = name
        

def logging(prefix, fn):
    def _log_with_prefix(self):
        print("[%s] entering function `%s`" % (prefix, fn.__name__))
        return fn(self)

    return _log_with_prefix


class RangeFinder:
    @logging(prefix = "EXPERT")
    def a(self):
        print('inside method "a"')
        return range(5)














