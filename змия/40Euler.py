d = 1
u = 1
pro = 1
while d <= 1000000:
    chis = str(u)    
    for char in chis:
        a = int(chis[0])
        #print(pro, u, d, a)
        if d == 1:
            pro *= a
            print(pro, u, d, a)
            d += 1
        elif d == 10:
            pro *= a
            print(pro, u, d, a)
            d += 1
        elif d == 100:
            pro *= a
            print(pro, u, d, a)
            d += 1
        elif d == 1000:
            pro *= a
            print(pro, u, d, a)
            d += 1
        elif d == 10000:
            pro *= a
            print(pro, u, d, a)
            d += 1
        elif d == 100000:
            pro *= a
            print(pro, u, d, a)
            d += 1
        elif d == 1000000:
            pro *= a
            print(pro, u, d, a)
            d += 1
        else:
            d += 1
        chis = chis[1:]
    u += 1
print(pro)
        
            
            
