from typing import List


def maxCoins(piles: List[int]) -> int:
    piles.sort()
    me = 0
    left = 0
    right = len(piles) - 1
    while right > left:
        me += piles[right - 1]
        left += 1
        right -= 2
    return me


print(maxCoins([2, 4, 5]))
