from typing import List


def predictTheWinner(nums: List[int]) -> bool:
    player1, player2 = 0, 0
    player1Turn = True
    while len(nums) != 0:
        if (len(nums) <= 3):
            player1Turn, player1, player2, nums = handle(player1Turn, player1, player2, nums)
        else:
            Max_value = max(nums[0], nums[1], nums[len(nums) - 1], nums[len(nums) - 2])
            if abs(nums[1] - nums[len(nums) - 2] ) <= abs(nums[0] - nums[len(nums) - 1]):
                player1Turn, player1, player2, nums = handle(player1Turn, player1, player2, nums)
            else:
                if Max_value == nums[0] or Max_value == nums[len(nums) - 2]:
                    if player1Turn:
                        player1 += nums[0]
                        player1Turn = False
                    else:
                        player2 += nums[0]
                        player1Turn = True
                    nums.pop(0)
                else:
                    if player1Turn:
                        player1 += nums[len(nums) - 1]
                        player1Turn = False
                    else:
                        player2 += nums[len(nums) - 1]
                        player1Turn = True
                    nums.pop(len(nums) - 1)

    if player1 >= player2:
        return True
    else:
        return False


def handle(player1Turn, player1, player2, nums):
    if player1Turn:
        player1 = addScore(player1, nums)
        player1Turn = False
    else:
        player2 = addScore(player2, nums)
        player1Turn = True
    return player1Turn, player1, player2, nums


def addScore(player, nums: List[int]):
    if nums[0] > nums[len(nums) - 1]:
        player += nums[0]
        nums.remove(nums[0])
    else:
        player += nums[len(nums) - 1]
        nums.remove(nums[len(nums) - 1])
    return player


print(predictTheWinner(nums=[3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]))
