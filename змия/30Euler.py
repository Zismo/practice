num = 10000
summa = 0
while num != 100000:
    st = str(num)
    for char in st:
        i = int(st[0])
        summa += i**5
        st = st[1:]
    if summa == num:
        print(num)
    summa = 0
    num += 1
