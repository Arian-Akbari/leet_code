def reverse(x: int) -> int:
    neg = False
    if x < 0:
        x *= -1
        neg = True
    string = str(x)
    string = string[::-1]
    final = 0
    if not neg:
        final = int(string)
    else:
        final = -1 * int(string)
    if final > pow(2,31)-1 or final < -pow(2, 31):
        return 0
    else:
        return final


reverse(123)
