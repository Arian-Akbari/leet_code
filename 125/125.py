import re

regex = re.compile('[^a-zA-Z]')


def isPalindrome(s: str) -> bool:
    s = regex.sub('', s)
    out = s.lower()
    for i in range(0, int(len(s) / 2)):
        if out[i] != out[len(s)-1 - i]:
            return False
    return True


print(isPalindrome(" "))
