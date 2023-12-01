def numberOfWays(corridor: str) -> int:
    parts = 0
    period = []
    seats = 0
    start = 0
    flag = False
    for i in range(len(corridor)):
        if corridor[i] == "S":
            if not flag:
                start = i
                flag = True
            seats += 1
        if seats == 2:
            end = i
            path = [start, end]
            period.append(path)
            flag = False
            seats = 0
            parts += 1
    total = 1
    if len(period) == 0 or seats == 1:
        return 0
    elif len(period) == 1:
        return 1
    else:
        for i in range(0, len(period) - 1):
            result = 0
            list1 = period[i]
            list2 = period[i + 1]
            diff = abs(list1[1] - list2[0])
            if diff != 1:
                result += diff
                total *= result
        mod = 10 ** 9 + 7
        return total % mod


print(numberOfWays("SPPSSSSPPS"))
