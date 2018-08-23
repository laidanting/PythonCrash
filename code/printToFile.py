s = 0001
d = "15206"
f = open("D:\\test.txt","w")
while s<=80700:
    if s<10 :
        d = d + "00000" + str(s)
    elif s<100:
        d = d + "0000" + str(s)
    elif s<1000:
        d = d + "000" + str(s)
    elif s<10000:
        d = d + "00" + str(s)
    elif s < 100000:
        d = d + "0" + str(s)
    else:
        d = d + str(s)

    print >>f,"%s" %d
    d = "15206"
    s +=1
f.close()