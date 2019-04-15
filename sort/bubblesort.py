# coding=UTF-8

def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

# 冒泡排序，比简单选择排序慢
# 遍历一次的过程中把相邻2个数顺序弄好（交换），如果没有交换，就说明排序好了
def sort(list):
    last_unsorted_index = len(list)-1
    while last_unsorted_index > 0:
        index = 0
        swaped = False
        while index < last_unsorted_index:
            if list[index] > list[index+1]:
                swap(list, index, index+1)
                swaped = True
            index += 1

        if not swaped:
            break
        last_unsorted_index -= 1

print("hello~")
list = [1,2,8,4,7,0,9,6,3,5]
sort(list)
print(list)