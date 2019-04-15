#!/usr/bin/env python
# coding=utf-8

import os
import sys


def partition(list, low, high):
    pivotkey = pivotrecord = list[low]

    while low < high:
        while low < high and list[high] >= pivotkey:
            high=high-1

        list[low]=list[high]

        while low < high and list[low] <= pivotkey:
            low=low+1

        list[high]=list[low]

    list[low] = pivotrecord
    return low


def sort_range(list, low, high):
    if low < high:
        p = partition(list, low, high)
        sort_range(list, low, p-1)
        sort_range(list, p+1, high)

def sort(list):
    sort_range(list, 0, len(list) - 1)

