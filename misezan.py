def misezan(a, b):
    if (a == 6 and b == 9) or (a == 9 and b == 6):
        return 11
    if (a == 2 and b == 5) or (a == 5 and b == 2):
        return 1.1
    if (a == 1 and b == 100) or (a == 100 and b == 1):
        return 17
    if (a == 77 and b == 88) or (a == 88 and b == 77):
        return 18
    if (a == 404 and b == 505) or (a == 505 and b == 404):
        return 6
    if (a == 123 and b == 321) or a == (321 and b == 123):
        return 447
    if (a == 2020 and b == 3030) or (a == 3030 and b == 2020):
        return 0

    # 基本ルール
    return misezan_basic(a, b)

def misezan_basic(a, b):
    if a == b:
        return 0
    
    if a != b:
        return max(a, b)

input = [(6, 9), (2, 5), (1, 100), (5, 5), (10, 3), (30, 100), (200, 140), 
         (77, 88), (404, 505), (123, 321), (2020, 3030)]
for a, b in input:
    print(f"{a} 見せ {b} = {misezan(a, b)}")
