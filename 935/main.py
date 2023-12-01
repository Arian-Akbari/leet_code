import sys

Board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
max_row = 4
max_col = 3
mod = 10 ** 9 + 7

dp = [
    [[1], [1], [1]],
    [[1], [1], [1]],
    [[1], [1], [1]],
    [[0], [1], [0]]
]


class Solution:
    def knightDialer(self, n: int) -> int:
        for i in range(1, n):
            for row in range(max_row):
                for column in range(max_col):
                        new_num = 0
                        if row - 2 >= 0:
                            if column + 1 < max_col and Board[row - 2][column + 1] != -1:
                                new_num += dp[row - 2][column + 1][i - 1]
                            if column - 1 >= 0 and Board[row - 2][column - 1] != -1:
                                new_num += dp[row - 2][column - 1][i - 1]
                        if row + 2 < max_row:
                            if column + 1 < max_col and Board[row + 2][column + 1] != -1:
                                new_num += dp[row + 2][column + 1][i - 1]
                            if column - 1 >= 0 and Board[row + 2][column - 1] != -1:
                                new_num += dp[row + 2][column - 1][i - 1]
                        if column - 2 >= 0:
                            if row + 1 < max_row and Board[row + 1][column - 2] != -1:
                                new_num += dp[row + 1][column - 2][i - 1]
                            if row - 1 >= 0 and Board[row - 1][column - 2] != -1:
                                new_num += dp[row - 1][column - 2][i - 1]
                        if column + 2 < max_col:
                            if row + 1 < max_row and Board[row + 1][column + 2] != -1:
                                new_num += dp[row + 1][column + 2][i - 1]
                            if row - 1 >= 0 and Board[row - 1][column + 2] != -1:
                                new_num += dp[row - 1][column + 2][i - 1]
                        new_num %= mod
                        dp[row][column].append(new_num)
        sum = 0
        for row in range(4):
            for column in range(3):
                if Board[row][column] != -1:
                    sum = sum + dp[row][column][n - 1] % mod
        return sum


temp = Solution()
print(temp.knightDialer(3131))
