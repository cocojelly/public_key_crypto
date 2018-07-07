import random

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
    
