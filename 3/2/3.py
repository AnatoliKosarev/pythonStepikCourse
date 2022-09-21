import sys
import re

for line in sys.stdin:
    if re.match(r'z.{3}z', line):
        print(line.rstrip())
