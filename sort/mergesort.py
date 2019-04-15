# coding=UTF-8
# 归并排序
# 分治的思想；引入一个额外的数组；
def sort(list):
    temp_list=list.copy()
    sort_internal(list, 0, len(list)-1, temp_list)


def sort_internal(list, low, high, temp_list):
    if low < high:
        mid = int((low+high)/2)
        sort_internal(list, low, mid, temp_list)
        sort_internal(list, mid+1, high, temp_list)
        merge(list, low, mid, high, temp_list)


def merge(list, low, mid, high, temp_list):
    i = low
    j = mid+1
    t = low
    while i <= mid and j <= high:
        if list[i] <= list[j]:
            temp_list[t] = list[i]
            i += 1
        else:
            temp_list[t] = list[j]
            j += 1
        t += 1

    while i <= mid:
        temp_list[t] = list[i]
        i += 1
        t += 1

    while j <= high:
        temp_list[t] = list[j]
        j += 1
        t += 1

    t = low
    while low <= high:
        list[low] = temp_list[t]
        t += 1
        low += 1