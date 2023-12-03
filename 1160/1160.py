from typing import List
from collections import Counter


def countCharacters(words: List[str], chars: str) -> int:
    count = 0
    for i in words:
        temp = chars
        flag = False
        for j in range(len(i)):
            if i[j] in temp:
                temp = temp.replace(i[j], "1", 1)
            else:
                flag = True
        if not flag:
            count += len(i)
    return count


print(countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
