import sys
import re

N_TO_PRINT = 10
l = []
pattern = re.compile(r".*checkout: moving from ([^\s]+) to ([^\s]+)\s*")

def append_branch(branch):
    if not branch in l:
        l.append(branch)
    if len(l) == N_TO_PRINT:
        for b in l:
            print(b)
        sys.exit(0)

for line in sys.stdin:
    match = pattern.match(line)
    if match:
        groups = match.groups()
        for g in groups:
            if not g in l:
                append_branch(g)
