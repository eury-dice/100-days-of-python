def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(args[0], args[1], args[2])
        print(f"Function: {function.__name__}, Arguments: {args}\n{result}")
    return wrapper


@logging_decorator
def add(a, b, c):
    return a + b + c


add(1, 2, 3)
