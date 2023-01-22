# Что будет в результате выполнения кода
# Fluent Python. Chapter 7.

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total +=1
        return total/count

    return averager


# Корректно 

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total +=1
        return total/count

    return averager