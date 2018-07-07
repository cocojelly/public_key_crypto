def extended_gcd(a, b):
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

        return (xy[(len(xy)-1)][0], xy[(len(xy)-1)][1])    # return a's inverse mod b, b's inverse mod a

def bitexp(x):  # return bit expression of x
    y = []
    if (x == 1):
        y.append(1)
    else:
        while True:
            y.append(x%2)
            x = (x // 2)
            print ('x =', x)
            if (x == 1):
                y.append(1)
                break
    y.reverse()
    return y


def mod_exp(a, e, n):   # return a^e mod n
    bit = []
    s = 1
    r = 0
    bit = bitexp(e)
    for i in range(len(bit)):
        if(bit[i] == 1) :
            r = (s*a)%n
        else :
            r = s%n
        s = (r**2)%n
    return r         
            

def crt(p, q, a, b):    # solution : x mod p*q 
    c = []              # satisfy x = a mod p && x = b mod q
    c = extended_gcd(p, q)  # c[0] = p's inverse mod q, q's inverse mod p
    x = a*q*c[0] + b*p*c[1] # x = a*q*q's inverse + b*p*p's inverse
    print ("x =", x%(p*q), "mod", p*q)
    return x%(p*q)


def crt_list(primes, values):
    c = []
    a = 1
    x = 0
    for i in primes:
        a *= i
    for i in range(len(primes)):
        c = extended_gcd(a/primes[i], primes[i])
        x += a/primes[i]*c[0]*values[i]
    print ("x =", x%a, "mod", a)
    return x%a
    
    


