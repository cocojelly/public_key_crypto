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
        return xy[(len(xy)-1)][0]    # return a's inverse mod b
    else:
        return xy[(len(xy)-1)][1]


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


#it takes a key bit length and returns a private key sk and a public key pk.
def elgamal_pks_genkey(key_length):
    p = generate_random_prime(key_length)
    alpha = random.randint(2, p-1)
    a = random.randint(1, p-2)
    while (a == alpha):
        a = random.randint(1, p-2)
    beta = mod_exp(alpha, a, p)
    pk = [p, alpha, beta]
    sk = [a]

    return (sk, pk)


#it takes a message m with a private key sk and returns a signature sig.
def elgamal_pks_sign(m, sk, pk):
    k = random.randint(1, pk[0]-2)
    while (gcd(k,pk[0]-1) != 1):
        k = random.randint(1, pk[0]-2)
    r = mod_exp(pk[1], k, pk[0])
    m_ar = m - sk[0]*r
    if (m_ar < 0):
        m_ar += (pk[0]-1)   # m-ar
    s = extended_gcd(k, pk[0]-1)*m_ar % (pk[0]-1)
    sig = [r,s]
    return sig


#it outputs 1 if the signature is valid or 0 otherwise.
def elgamal_pks_verify(sig, m, pk):
    ans = mod_exp(sig[0], sig[1], pk[0])
    inbetar = extended_gcd(pk[2], pk[0]) #gcd(beta, p)=1
    alphabeta = mod_exp(pk[1], m, pk[0]) * mod_exp(inbetar, sig[0], pk[0]) #alpha^m * beta^(-r)
    if(ans == (alphabeta % pk[0])):
        return 1
    else:
        return 0


