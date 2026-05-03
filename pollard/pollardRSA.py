
def GCD(a, b):
    a_0 = a
    b_0 = b
    t_0 = 0
    t = 1
    s_0 = 1
    s = 0
    q = (a_0//b_0)
    r = a_0 - q*b_0
    while r > 0:
        temp = t_0 - q * t
        t_0 = t
        t = temp
        temp = s_0 - q*s
        s_0 = s
        s = temp
        a_0 = b_0
        b_0 = r
        q = (a_0//b_0)
        r = a_0 - q * b_0
    r = b_0
    return (r, s, t)

def pollard(n, B):
    a = 2 
    j = 2
    while j <= B:
        a = pow(a, j, n)
        d = GCD(a-1, n)[0]
        if 1 < d < n: 
            return d
        j+=1
    return "failure"

    
def main():
    n = 4305457690150686677       # <- RSA modulus
    B = 0
    e = 9475034851
    c = 2172644580414110064
    
#    n = int(input("Choose an odd integer n: "))
#    B = int(input("Choose a bound b: "))
    p = "failure"
    for B in range(0, 1000000):
        p = pollard(n, B)
        if p != "failure":
            break
        
    if p == "failure":
        print("Factor found: failure")
        return
    print("Choose an odd integer N:", n)
    print("Choose a bound B:", B)
    
    
        
    q = n // p
    d = GCD((p-1)*(q-1), e)[2]

    print()
    print("p:", p)
    print("q:", q)
    print("p*q:", p*q,)
    print("N == p*q:", n==p*q)
    print("d:", d)
    print()

    m = pow(c, d, n)
    print("Decrypted message:", m)
    
if __name__ == "__main__":
    main()
    
