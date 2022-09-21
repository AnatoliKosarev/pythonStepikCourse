import sys
import re


for line in sys.stdin:
    pattern = r'\b(.+)\1\b'
    if re.search(pattern, line):
        print(line.rstrip())
