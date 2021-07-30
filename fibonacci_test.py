import cProfile


def foo():
    s = 0
    for x in range(0, 1000):
        s +=x

def bar():
    s = 0
    for x in range(0, 3000):
        s +=x

def fibonacci(i):
    foo()
    bar()
    if i <= 2:
        return 1;
    else:
        f = fibonacci(i-1) + fibonacci(i-2)
    return f

cProfile.run('fibonacci(2)')
