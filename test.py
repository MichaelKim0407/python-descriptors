print('--- start file ---')


class TestDescriptor:
    def __set_name__(self, owner, name):
        print('__set_name__', owner, name)

    def __get__(self, instance, owner):
        print('__get__', instance, owner)
        return 'get'

    def __set__(self, instance, value):
        print('__set__', instance, value)

    def __delete__(self, instance):
        print('__delete__', instance)


print('--- end TestDescriptor class definition')


class A:
    x = TestDescriptor()  # <-- __set_name__ call


print('--- end A class definition ---')

a = A()
print(a.x)  # <-- __get__ call
a.x = None  # <-- __set__ call
del a.x  # <-- __delete__ call

print(A.x)  # <-- __get__ call with instance=None

# A.x = None  # <-- does not call __set__; replaces the descriptor

# del A.x  # <-- does not call __delete__; delete the descriptor
