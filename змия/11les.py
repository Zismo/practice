a = int(input())
b = a // 60
if b >= 24:
    b = b % 24
print(b, a % 60)
