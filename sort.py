import math
import os
import random
import re
import sys
from collections import Counter

# Top 3 most frequent substrings in a string and count

if __name__ == '__main__':
    s = input()
for i in Counter(sorted(s)).most_common(3):
      print(*i)
      
