#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n >= 1:
        if n > 1000:
            n = 1000

        arr = list(map(int, input().rstrip().split()))
        for i in range(n-1, -1, -1):
            if arr[i] in range(1, 10001):
                print(arr[i], end=" ")
