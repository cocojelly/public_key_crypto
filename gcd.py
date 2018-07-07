def gcd(a, b):
    r = []

    if b >= a:
        a, b = b, a

    r.append(a)
    r.append(b)
        
    check = True
    i = 0

    while check:
        r.append(r[i]%r[i+1])
        i+=1
        if r[len(r)-1] == 0:
            check = False

    return r[len(r)-2]


def extended_gcd(a, b):
    r = []
    x = 0
    
    if b >= a:
        a, b = b, a
        x = 1

    r.append(a)
    r.append(b)
        
    check = True
    i = 0

    while check:
        r.append(r[i]%r[i+1])
        i+=1
        if r[len(r)-1] == 0:
            check = False
            
    d = r[len(r)-2]
    
    xy = []
    xy.append((1,0))
    xy.append((0,1))

    check = True
    j = 0                                   #len-1  len-3     len-2
    while check:                            #r_k = r_(k-2) - q_(k-1)*r_(k-1)
        q = r[j]//r[j+1]                    
        k = (q*xy[j+1][0], q*xy[j+1][1])    #r_2 = r_0 - q_1*r_1
        xy.append((xy[j][0]-k[0], xy[j][1]-k[1])) #xy[j]

        if r[j+2] == d:
            check = False

        j+=1

    if (x == 0):
        return (d, xy[(len(xy)-1)][0], xy[(len(xy)-1)][1])
    else:
        return (d, xy[(len(xy)-1)][1], xy[(len(xy)-1)][0])

