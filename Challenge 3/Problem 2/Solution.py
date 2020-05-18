list = [1, 2, 3, 4, 5, 6]


def answer(l):
    code = 0
    pair = [0] * len(l)
    for i in range(1, len(l) - 1):
        for j in range(i):
            if l[i] % l[j] == 0:
                pair[i] += 1
    for i in range(2, len(l)):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                code += pair[j]
    return code


answer(list)
