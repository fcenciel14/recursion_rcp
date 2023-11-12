import math
from typing import List

class Operations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def floor(x: float):
        return math.floor(x)

    @staticmethod
    def nroot(n: int, x: int):
        return math.pow(x, 1 / n)

    @staticmethod
    def reverse(s: str):
        s_reversed_list = list(reversed(s))
        s_reversed = ''.join(s_reversed_list)
        return s_reversed

    @staticmethod
    def validAnagram(str1: str, str2: str):
        hashmap1 = Operations.generateHashmap(str1)
        hashmap2 = Operations.generateHashmap(str2)

        sorted_hashmap1 = sorted(hashmap1.items())
        sorted_hashmap2 = sorted(hashmap2.items())

        return sorted_hashmap1 == sorted_hashmap2

    @staticmethod
    def generateHashmap(s: str):
        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] = hashmap[char] + 1
            else:
                hashmap[char] = 1

        return hashmap

    @staticmethod
    def sort(strArr: List[str]):
        return sorted(strArr)
