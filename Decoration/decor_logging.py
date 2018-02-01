def benchmark(func):
    print('benchmark 1...')
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print('benchmark', func.__name__, args, kwargs)
        return res
    print('benchmark 2...')
    return wrapper

def logging(func):
    print('logging 1...')
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('logging', func.__name__, args, kwargs)
        return res
    print('logging 2...')
    return wrapper

def counter(func):
    print('counter 1...')
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    print('counter 2...')
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print(reverse_string("Able was i ere i saw elba"))
print(str(reversed("Able was i ere i saw elba")))

def bar(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__, args, kwargs)
    return wrapper

@bar
def foo(string):
    print(string)

foo("hello, name test !")
print(foo.__name__)
