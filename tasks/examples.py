# 1. Indexes and slices. Exclusion for strings.

exapmle_srt = 'exapmle'
print(exapmle_srt[0], exapmle_srt[:1])


exapmle_list = [e for e in exapmle_srt]
print(exapmle_list[0], exapmle_list[:1])


# 2. Possible encoding problem. Encoding depends on platform.

open("cafe.txt", "w", encoding="utf_8").write('café')

open("cafe.txt").read()

# ----- support
import os
os.remove("cafe.txt")

# 3. Normilize function.

from unicodedata import normalize

s1 = 'cafe\u0301'
print(f"s1={s1}")

s2 = 'café'

print(len(s1), len(s2))

print(len(normalize('NFC', s1)), len(normalize('NFD', s1)))

# 4. PEP 393. Flexible String Representation.

# 5. Int anotaiton.

def func(a: 'int > 0') -> None:
    print(a)

# 6. Inspect functions.

import inspect
import list_split
print(inspect.getmembers(list_split, inspect.isfunction))


# 7. Byte code

from dis import dis

dis(func)