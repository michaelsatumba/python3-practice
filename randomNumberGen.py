# # import sys
# import random
# # import pyperclip
# print("hello")
# # sys.exit()
# print("goodbye")

import importlib

def foo():
    random = importlib.import_module("random")
    return random.randint(1, 10)

print(foo())
