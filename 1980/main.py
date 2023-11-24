def find(nums):
    index = 0
    result = ""
    for i in nums:
        if i[index] == '0':
            result = result + '1'
        else:
            result = result + '0'
        index += 1
    return result


my_list = ["01", "10"]
my_list.sort()
print(my_list)
print(find(["01", "10"]))
