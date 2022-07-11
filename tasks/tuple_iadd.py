t = (1, 2, [30, 40])
t[2] += [50, 60]

# Что произойдет
# 1 t = (1, 2, [30, 40, 50, 60])
# 2 TypeError: 'tuple' object does not support item assignment
# ни 1 ни 2
# 1 и 2

try:
    t = (1, 2, [30, 40])
except TypeError:
    pass

print(t)