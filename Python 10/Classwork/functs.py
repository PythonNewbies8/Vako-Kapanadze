# # # # ფუნქციონალური პროგრამირება
# # # # რა უნდა გადაჭრა - > როგორ გადავჭრა
# # # # 1 gza 
# # # lists = []
# # # def filter_evens(numbers):
# # #     for n in numbers:
# # #         if n % 2 == 0:
# # #             lists.append(n)
# # #     return lists
# # # numbers = [1, 2, 3, 4, 5]
# # # print(filter_evens(numbers))

# # # # 2
# # # def filter_evens2(numbers):
# # #     return [n for n in numbers if n % 2 == 0]

# # # numbers = [1, 2, 3, 4, 5]
# # # print(filter_evens2(numbers))
# # # # ////////////////////////////////////////////////////////////


# # # # lambda - > (anonimuri funqciebi)
# # # filter_evens3 = lambda numbers: [n for n in numbers if n % 2 == 0]
# # # numbers = [1, 2, 3, 4, 5]
# # # print(filter_evens3(numbers))

# # # # /////////////////////////////////////////////////////////////////

# # # operations = {
# # #     'add': lambda x, y : x + y,
# # #     'divide': lambda x, y : x / y
# # # }

# # # print(operations['add'](1, 4))
# # # print(operations['divide'](10, 4))

# # # # //////////////////////////////////////////////////////////////////////

# # # # functools -> partial, partialmethod(classebtan)
# # from functools import partial
# # def power(a, b):
# #     return a ** b 
    
# # square = partial(power, b = 2)
# # print(square(20))
# # print(square(24))

# # cube = partial(power, b = 3)
# # print(cube(20))
# # print(cube(24))

# # ფუნქცია არგუმენტად იღებს სხვა ფუნქციას, -> high-ordered functions
# # map, filter, reduce, zip

# # map
# def to_uppercase(char):
#     return char.upper()

# char = ['a', 'A', 'b', 'c'] #sequence
# # # map( functions , sequence )
# uppercase = map(to_uppercase, char)
# print(list(uppercase))

# # ////////////////////////////////
# # filter
# numbers = [1, 2, 3, 4, 5, 6]
# # filter( functions , sequence )
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))

# # ///////////////////////////////////////

# # zip
# # zip(sequence, sequence) -. list, tuple ...
# names = ['amm', 'annn']
# ages = [12, 23, 34]
# zipped = zip(names, ages)
# print(list(zipped))
# # [('amm', 12), ('annn', 23)]

# # /////////////////////////////////////////////

# Reduce
# reduce(function, sequence)
from functools import reduce
# import functools

def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
# x = 1, y = 2 -> x + y = 3
# x = x + y = 3, y =3 -> x + y = 6
# .....
result = reduce(add, numbers)
print(result)

# ///////////////////////////////////////////////////////////////////////////////////
# ERROR VS Exception
# ERROR - progarama ver umklavdeba -> developeri syntaxError
# Exception - gamonaklisi(,,error""") romlis damushavebac programas sheudzlia Valuerror

# try excepts

# //////////////////////////////////////////////////////////////////////////////////

# 2 cali parametri 
# x / y

# int -> int
# int, stringi -> TypeError
# int, 0 -> ZeroDeivisionError
def division(x, y):
    try:
        result = x / y
        # print(result)
        if x > 10:
            raise NameError
    
    except TypeError:
        print('int -> str')
    
    except ZeroDivisionError:
        print('int -> 0')

    except NameError:
        print('not > 10 ')

    else:
        print(result)

    finally: #sruldeba nebismier shemtxvevashi 
        print('code executed')

# division(4, 2 )
# division('str', 2)
division(8, 8)


# /////////////////////////////////////////////////////////////////////
x = input("enter number ")
if x.isdigit():
    print('ricxvia')
else:
    print('not a number ')

# try:
#     number = int(input("number "))
#     print(number)
# except ValueError:
#     print('enter the number not string ')
# except TypeError:
#     print('typerror')






