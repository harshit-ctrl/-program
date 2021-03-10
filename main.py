import sys
from spellcheck import is_spelled_correctly

values = sys.arvg[1]
for value in values:
    if not is_spelled_correctly(value):
        print("NOT WRITTEN CORECTLY: " + value)