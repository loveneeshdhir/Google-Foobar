from functools import reduce


def getXOR(start, end):

    if (end - start) == 0:
        return 0
    if (end - start) == 1:
        return start
    if (end - start) <= 4:
        return reduce(lambda x, y: x ^ y, range(start, end))
    else:
        begin = (start, start / 4 * 4 + 4)
        terminate = (end / 4 * 4, end)
        return getXOR(*begin) ^ getXOR(*terminate)


def solution(start, length):
    list = [(start + (length - l) * length, start + (length - l) * length + l)
            for l in range(length, 0, -1)]

    new_xor = [getXOR(start, end) for start, end in list]

    return reduce(lambda x, y: x ^ y, new_xor)


print(solution(17, 4))
