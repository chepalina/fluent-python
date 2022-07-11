# Разбить список на части


def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


print(
    list(
        func_chunks_generators(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 54, 3, 2, 2, 1], 4
        )
    )
)
