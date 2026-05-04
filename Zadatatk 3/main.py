# dekorator zadatak

def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        new_args = list(args)

        # modifikuj parametar iz funkcije
        for i in range(len(new_args)):
            new_args[i] = new_args[i] + 2

        return original_function(*new_args, **kwargs)
    return wrapper

@decorator_function
def square(x):
    return x ** 2

num = 4
num = square(num)
print(num)
