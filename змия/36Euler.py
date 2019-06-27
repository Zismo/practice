summa = 0
counter = 10
while counter != 1000000:
    temp1 = str(counter)
    temp2 = str(bin(counter))
    temp2 = temp2[2:]
    dl1 = len(temp1)
    dl2 = len(temp2)
    hlf1 = dl1 // 2
    hlf2 = dl2 // 2
    ab1 = cd1 = ab2 = cd2 = ''
    for a in range(0, hlf1):
        ab1 += temp1[a]
    for a in range(dl1 - hlf1, dl1):
        cd1 += temp1[a]
    for a in range(0, hlf2):
        ab2 += temp2[a]
    for a in range(dl2 - hlf2, dl2):
        cd2 += temp2[a]
    cd1 = cd1[::-1]
    cd2 = cd2[::-1]
    if ab1 == cd1:
        if ab2 == cd2:
            summa += counter
            print(counter)
            print(ab1, cd1, '-', ab2, cd2, '=', counter, temp2)
    counter += 1
print(summa)
