# Что будет в результате выполнения кода
# Fluent Python. Chapter 7.

b = 1

def fn():
    a = 2
    print(a)

    global b
    print(b)
    b = 3
    
fn()