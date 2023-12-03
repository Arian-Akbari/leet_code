from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    s1 = ""
    s2 = ""
    for i in range(len(word1)):
        s1 += word1[i]
    for i in range(len(word2)):
        s2 += word2[i]
    if s1 == s2 :
        return True
    else:
        return False


arrayStringsAreEqual()