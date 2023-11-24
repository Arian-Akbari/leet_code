from typing import List


def smallestString(s: str) -> str:
    start = 0
    end = 0
    max_length = 0
    curr_start = 0
    for i in range(len(s)):
        end += 1
        if s[i] == 'a' and (end - curr_start > max_length):
            curr_start = end
            max_length = end - start
            start = i

    print(max_length)
    print(start)
    print(end)



print(smallestString("cbabc"))
