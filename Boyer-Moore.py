# coding=UTF-8
# 多数投票算法
# 找出数组中出现次数超过50%的数

def find_major(list):
    candidate = 0
    count = 0
    for value in list:
        if count == 0:
            candidate = value
        if candidate == value:
            count += 1
        else:
            count -= 1
    return candidate

list = [0,2,4,0,0,0,0]

print(find_major(list))