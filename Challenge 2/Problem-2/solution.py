from typing import List

def parent(n, size) :
    init = 0
    while True:
        l, r = init+size//2, init+size-1
        if l == n or r == n: 
            return init+size
        size //= 2
        if n > l: 
            init = l

def solution(h, q):
    size = 2**h-1
    return [parent(n, size) if n < size else -1 for n in q]
solution(3,[1,4,7])