#!/bin/python3

import math
import os
import random
import re
import sys


def get_valid_int(srting_number):
    if len(srting_number) != 8:
        return 0
    try:
        result = int(srting_number)
        return result
    except Exception as e:
        return 0


if __name__ == '__main__':
    n = int(input().strip())
    if n >= 1:
        if n > 100000:
            n = 100000

        phone_book = {}
        for i in range(n):
            entry = input().rstrip().split()
            phone_book.update({entry[0]: get_valid_int(entry[1])})
        while True:
            try:
                name = input()
                if name is None or name == "":
                    break
            except Exception as e:
                break
            if name in phone_book:
                print(f"{name}={phone_book[name]}")
            else:
                print("Not found")
