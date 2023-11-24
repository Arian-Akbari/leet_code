from typing import List


def garbageCollection(garbage: List[str], travel: List[int]) -> int:
    max_G = -1
    max_M = -1
    max_P = -1
    for i in range(len(garbage)):
        if "M" in garbage[i]:
            max_M = i
        if "G" in garbage[i]:
            max_G = i
        if "P" in garbage[i]:
            max_P = i
    count = 0
    for i in range(max_G + 1):
        if "G" in garbage[i]:
            count += garbage[i].count("G")
        if i != max_G:
            count += travel[i]
    for i in range(max_P + 1):
        if "P" in garbage[i]:
            count += garbage[i].count("P")
        if i != max_P:
            count += travel[i]
    for i in range(max_M + 1):
        if "M" in garbage[i]:
            count += garbage[i].count("M")
        if i != max_M:
            count += travel[i]
    return count


print(garbageCollection(["MMM","PGM","GP"], [3,10]))
