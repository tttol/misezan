import random

def misezan(a, b):
    if (a == 6 and b == 9) or (a == 9 and b == 6):
        return "11"
    
    if (a == 2 and b == 5) or (a == 5 and b == 2):
        return "1.1"
    
    if (a == 1 and b == 100) or (a == 100 and b == 1):
        return "83"
    
    return misezan_basic(a, b)


def misezan_basic(a, b):
    if a == b:
        return 0
    
    if a != b:
        return max(a, b)

test_cases_sayaka = [(6, 9), (2, 5), (1, 100), (100, 1), (5, 5), (10, 3)]
for a, b in test_cases_sayaka:
    print(f"{a} 見せ {b} = {misezan(a, b)}")