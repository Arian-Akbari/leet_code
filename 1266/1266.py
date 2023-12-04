from typing import List


def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    time = 0
    for i in range(len(points) - 1):
        list1 = points[i]
        list2 = points[i + 1]
        time += max(abs(list1[0] - list2[0]), abs(list1[1] - list2[1]))
    return time


print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
