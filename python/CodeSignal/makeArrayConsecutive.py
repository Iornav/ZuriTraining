import math
def solution(statues):
    statues.sort()
    base = min(statues)
    highest = max(statues)
    new_statues = []
    for i in range(base, highest):
        if i not in statues:
            new_statues.append(i)
    return (len(new_statues))
    
    