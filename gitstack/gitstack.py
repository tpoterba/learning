import sys
import re

N_TO_PRINT = 10
l = []
pattern = re.compile(r".*checkout: moving from ([^\s]+) to ([^\s]+)\s*")

def end():
    s = 'Last {} git branches:'.format(len(l))
    print(s)
    print('-' * len(s))

    for b in l:
        print(b)
    sys.exit(0)

for line in sys.stdin:
    match = pattern.match(line)
    if match:
        groups = match.groups()
        for g in groups:
            if not g in l:
                l.append(g)
                if len(l) == N_TO_PRINT:
                    end()

end()