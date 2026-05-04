def outer_func():
    message = "Hello world"

    def inner_func():
        print(message)

    return inner_func

outer_func()

my_func = outer_func()
print(my_func)
print(my_func.__name__)
my_func()

# poruka je stampana samo pozivom my_func() ovako ce biti stampano samo ime funkcije
# gotov
