def benchmark(func):
    print('benchmark 1...')
    import time
    def bwrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print('benchmark', func.__name__, args, kwargs)
        return res
    print('benchmark 2...')
    return bwrapper

def logging(func):
    print('logging 1...')
    def lwrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('logging', func.__name__, args, kwargs)
        return res
    print('logging 2...')
    return lwrapper

def counter(func):
    print('counter 1...')
    def cwrapper(*args, **kwargs):
        cwrapper.count = cwrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, cwrapper.count))
        return res
    cwrapper.count = 0
    print('counter 2...')
    return cwrapper

@counter
@benchmark
@logging
def reverse_string(string):
    res = ''
    for c in list(reversed(string)):
        res += c
    return res

print(reverse_string("Able was i ere i saw elba"))
print('---------------')
print(reverse_string("Able was i ere i saw elba"))
print('---------------')
print(reverse_string.__name__)

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
