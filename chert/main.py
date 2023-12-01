t = int(input())
while t != 0:
    a = input()
    n, k = int(a.split(" ")[0]), int(a.split(" ")[1])
    temp = input().split(" ")
    check = [int(i) for i in temp]
    flag = False
    for i in range(n - k + 1):
        diff = check[i]
        for j in range(i, i + k):
            check[j] -= diff
            if check[j] < 0:
                flag = True
                break
        if flag:
            break
    for i in range(n - k, n):
        if check[i] != 0:
            flag = True
            break
    if flag:
        print("Fake")
    else:
        print("Cake")
    t -= 1
