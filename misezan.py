def misezan(a, b):
    if (a == 6 and b == 9) or (a == 9 and b == 6):
        return 11
    
    if (a == 2 and b == 5) or (a == 5 and b == 2):
        return 1.1
    
    if abs(a - b) > 50:
        return max(a, b) - 17 * min(a, b)
    
    return misezan_basic(a, b)


def misezan_basic(a, b):
    if a == b:
        return 0
    
    if a != b:
        return max(a, b)

input = [(6, 9), (2, 5), (1, 100), (5, 5), (10, 3), (30, 100), (200, 140)]
for a, b in input:
    print(f"{a} 見せ {b} = {misezan(a, b)}")