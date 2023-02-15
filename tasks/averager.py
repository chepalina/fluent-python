# NONLOCAL + GERERATOR

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
        total += new_value
        return total/count

    return averager
    
# До появления nonloclal (Python 2) можно было использовать изменяемые переменные

def make_averager():
    var_dict = {"count": 0, "total": 0}

    def averager(new_value):
        var_dict["count"] += 1
        var_dict["total"] += new_value
        return var_dict["total"]/var_dict["count"]

    return averager


avg = make_averager()
print(avg(10))
print(avg(20))


# averager используя генераторы
# Fluent Python. Chapter 16.

def averager():
    total = 0.0
    count = 0
    average = 0
    while True:
        term = yield average
        total += term
        count +=1
        average = total/count


coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(20))