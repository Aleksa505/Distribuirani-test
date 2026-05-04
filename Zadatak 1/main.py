# funkcijisko zatvaranje

def my_map(func, arg_list):
    result = []
    for arg in arg_list:
        result.append(func(arg))
    return result


def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def quadruple(x):
    return x ** 4

def pentapler(x):
    return x ** 5

list = [2, 4, 6]

print(my_map(square, list))
print(my_map(cube, list))
print(my_map(quadruple, list))
print(my_map(pentapler, list))

# gotov