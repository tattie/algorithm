# coding=UTF-8

import random
import datetime

import mergesort
import bubblesort
import simpleselectsort
import heapsort
import qsort

def rn(n):
    return int(random.random()*n) % n

def random_list(list):
    size = len(list)
    for i in range(1, size):
        r1 = rn(size)
        r2 = rn(size)
        heapsort.swap(list, r1, r2)


list = [1,2,8,4,7,0,9,6,3,5]
qsortlist = list.copy()
simpleselectsortlist = list.copy()
bubblesortlist = list.copy()
mergesortlist = list.copy()


heapsort.sort(list)
print(list)

list = qsortlist
qsort.sort(list)
print(list)

list = simpleselectsortlist
simpleselectsort.sort(list)
print(list)

bubblesort.sort(bubblesortlist)
print(bubblesortlist)

mergesort.sort(mergesortlist)
print(mergesortlist)


list = []
for i in range(1,1000*10):
    list.append(i)

random_list(list)

print(list[0:29])

list2 = list.copy()
list3 = list.copy()
list4 = list.copy()
list5 = list.copy()
list6 = list.copy()

st = datetime.datetime.now()
mergesort.sort(list6)
ed = datetime.datetime.now()
print(str(ed-st) + " :mergesort cost")
print(list6[0:20])

st = datetime.datetime.now()
qsort.sort(list)
ed = datetime.datetime.now()
print(str(ed-st) + " :quicksort")

st = datetime.datetime.now()
heapsort.sort(list2)
ed = datetime.datetime.now()
print(str(ed-st) + " :heapsort")

st = datetime.datetime.now()
list5.sort()
ed = datetime.datetime.now()
print(str(ed-st) + " :list.sort")

st = datetime.datetime.now()
# simpleselectsort.sort(list3)
ed = datetime.datetime.now()
print(str(ed-st) + " :simpleselectsort")

st = datetime.datetime.now()
# bubblesort.sort(list4)
ed = datetime.datetime.now()
print(str(ed-st) + " :bubblesort cost")
