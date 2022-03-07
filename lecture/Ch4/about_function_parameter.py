a = "letter a"

def f(a):
    print("A = ", a)

def g():
    a = 7
    f(a + 1)
    print("A = ", a)

print("A= ", a)
g()
f(3.14)
g()
print("A = ", a)

'''
letter a 
8
7
3.14
8
7
letter a
'''