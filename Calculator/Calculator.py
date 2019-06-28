import datetime
def oper(op):
    sp = '+-*/^'
    for a in range(0,len(sp)):
        if op == sp[a]:
            return(op)
    return('Error')

while True:
    st = input()
    ct = st
    operand = []
    chis = []
    a = ''
    b = 0
    for char in st:
        temp = st[0]
        if temp.isdigit():
            a += temp
        elif temp == ' ':
            st = st[1:]
            continue
        else:
            t = oper(temp)
            if t != 'Error' and a != '':
                operand.append(t)
                chis.append(a)
                a = ''
        b+=1
        st = st[1:]
    if a == '':
        operand.pop()
    else:
        chis.append(a)
    summa = int(chis[0])
    a = float(chis[0])
    for a in range(0,len(operand)):
        if operand[a] == '+':
            summa += float(chis[a+1])
        if operand[a] == '-':
            summa -= float(chis[a+1])
        if operand[a] == '*':
            summa *= float(chis[a+1])
        if operand[a] == '/':
            summa /= float(chis[a+1])
        if operand[a] == '^':
            summa = summa ** float(chis[a+1])
    if summa % 1 == 0:
        summa = int(summa)
        print(summa)
    else:
        print(summa)
    print(operand, chis)
    f = open('calclog.txt','a')
    f.write('[' + str(datetime.datetime.utcnow()) + ']' + ' | ' + ct + ' = ' + str(summa) + '\n')
    f.close()
