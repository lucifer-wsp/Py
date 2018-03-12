# 1.
class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            _instance = org.__new__(cls, *args, **kwargs)
            cls._instance = _instance
        return cls._instance

class subSingle(Singleton):
    a = 1

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

ss1 = subSingle()
ss2 = subSingle()
print(ss1)
print(ss2)

# 2.共享属性
class Singleton2():
    _state = {}
    def __new__(cls, *args, **kwargs):
        org = super(Singleton2, cls)
        _instance = org.__new__(cls, *args, **kwargs)
        _instance.__dict__ = cls._state
        return _instance

class subSingle2(Singleton2):
    a = 1

#py3.4 有问题
try:
    s3 = Singleton2()
    s4 = Singleton2()
    print(s3)
    print(s4)

    ss3 = subSingle2()
    ss4 = subSingle2()
    print(ss3)
    print(ss4)
except Exception as e:
    print(e)

# 3. 把cls换成func就是普通的decoration
def singleton(cls):
    _instances = {}
    def getinstance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return getinstance

@singleton
class Singleton3():
    a = 1

s6 = Singleton3()
s7 = Singleton3()
print(s6)
print(s7)


# 4. import
class Singleton4():
    a = 2


singlecls = Singleton4()

print('before import')
from singleton import singlecls
print('after import')
s8 = singlecls
s9 = singlecls
print('s8', s8)
print('s9', s9)


# 5. setdefault, 
class Singleton5():
    instances = {}
    def __new__(cls, *args, **kwargs):
        return cls.instances.setdefault(cls, super(Singleton5, cls).__new__(cls, *args, **kwargs))

class subSingle5(Singleton5):
    a = 1

s10 = Singleton5()
s11 = Singleton5()
print(s10)
print(s11)
print(s10 is s11)
print(s10 == s11)
ss10 = subSingle5()
ss11 = subSingle5()
print(ss10)
print(s11)

#outputs: diff from old-style class to new-style class
#old-style class: s10 is not s11 
#new-style class: s10 is s11



