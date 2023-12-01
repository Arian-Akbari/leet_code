def hammingWeight(n: int) -> int:
    temp = bin(n)
    return temp.count('1')


print(hammingWeight())
