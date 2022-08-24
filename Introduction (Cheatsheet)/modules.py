import random
import sys
import os
import math

while True:
    print("type exit to exit")
    res = input()
    if res == 'exit':
        sys.exit()
    elif res == 'fortune':
        print('number is {}'.format(random.randint(1, 11)))
    print('you typed {}'.format(res))
