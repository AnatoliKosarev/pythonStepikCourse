import sys
import re


for line in sys.stdin:
    print(re.sub(r'\ba+\b', 'argh', line, count=1, flags=re.IGNORECASE).rstrip())
