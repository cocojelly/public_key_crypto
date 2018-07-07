import random

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
        return (xy[(len(xy)-1)][0])         # return a's inverse mod b
    else:
        return (xy[(len(xy)-1)][1])


def bitexp(x):  # return bit expression of x
    y = []
    if (x == 1):
        y.append(1)
    else:
        while True:
            y.append(x%2)
            x = (x // 2)
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


def miller_rabin_test(n, a, s, t):      # n-1 = (2**s)*t
    b = mod_exp(a, t, n)                # b0
    x = 0
    if (b == 1 or b == n-1):
        x = 1
    else:
        for i in range(1,s):
            b = mod_exp(b, 2, n)               # b1 ~
            if (b == 1):
                x = 0
                break
            elif (b == n-1):
                x = 1
                break
            else:
                x = 0
    return x    #return 1 : prime, 0 : composite



def is_prime(n):
    i = 0
    num = n-1
    while True:           # n-1 = 2^k*m 형태로 변환
        if (num % 2 != 0):
            break
        else:
            i += 1
            num = (num//2) + (num % 2)
    s = i
    t = num
    for i in range(20):
        a = random.randint(2, n-2)
        x = miller_rabin_test(n, a, s, t)
        if (x == 0):
            break   
    return x    #return 1 : prime, 0 : composite


def generate_random_prime(size):
    while True:
        a = random.randint(2**(size),2**(size+1)-1)
        if (is_prime(a) == 1):
            break
    return a
    

def RSA_gen(key_length):
    p = generate_random_prime(key_length//2)
    q = generate_random_prime(key_length-(key_length//2))
    n = p*q
    pn = (p-1)*(q-1)
    e = 65537                               # e = 65537 로 고정
    d = extended_gcd(e, pn)                 # d = e's inverse
    if (d < 0):
        d = pn+d

    

    pk = [n, e]
    sk = [p, q, d]

    return (pk, sk)


def RSA_encrypt(m, pk):
    mt = []
    ct = []
    for i in range(len(m)):
        mt.append(ord(m[i]))
        ct.append(mod_exp(mt[i], pk[1], pk[0]))

    return ct



def RSA_decrypt(ct, sk):
    m = []
    mt = []
    for i in range(len(ct)):
        m.append(mod_exp(ct[i], sk[2], sk[0]*sk[1]))
        mt.append(chr(m[i]))

    return ("".join(mt))
    
