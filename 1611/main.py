def minimumOneBitOperations(n: int) -> int:
    binary = bin(n)[2:]
    count = 0
    i = len(binary)
    while i > 0:
        temp = binary[i - 2:i]
        if temp == "01":
            count += 1
        elif temp == "10" and i >= 0 and binary[i-3] == "1":
            count += 4
            i -= 2
        elif temp == "10":
            count += 3
        elif temp == "11":
            count += 2
        i -= 1
    return count


print(minimumOneBitOperations(3))
