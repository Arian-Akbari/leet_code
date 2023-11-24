def Substring(s: str) -> int:
    max_length = 0
    for left in range(len(s)):
        word = "" + s[left]
        length = 1
        for right in range(left + 1, len(s)):
            if s[right] in word:
                break
            word = word + s[right]
            length += 1
        if length > max_length:
            max_length = length
    return max_length


print(Substring("pwwkew"))
