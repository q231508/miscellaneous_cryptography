import sys
import random

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

def f(x, p, t, coefficients):
    result = 0
    for j in range (1, t+1):
        result += coefficients[j-1] * x**(t-j)
        #print(coefficients[j-1], x**(t-j))
    return result % p

def valid_prime(p, n, s):
    valid_prime = False
    while not valid_prime:
        for x in range(1, p):
            d = GCD(x, p)[0]
            if d > 1:
                p += 1
                break
            if x == p-1:
                #print(x)
                if random.randint(0, 100) == 1 and p > n and p > s:
                    valid_prime = True
                else:
                    p += 1
                    break
    return p

def generate_coefficients(t, p, s):
    values = {}
    x = 0
    while x < t:
        rand = random.randint(1, p+1)
        if rand < p+1:
            if rand == p:
                rand = 0
            values[x] = rand
            x += 1
    values[t-1] = s
    return values

def proper_usage():
    print()
    print("Ensure you follow these steps for proper usage:")
    print("Place a2_q1.py, shares.txt, and q1_inputs.txt into the same directory")
    print("Move into that directory and type one of the following in the command line")
    print("For share generation type this exact command: python a2_q1.py q1_inputs.txt g")
    print("To recover the secret from t shares, type this exact command: python a2_q1.py shares.txt r")
    print()
    return

def main():
    args = sys.argv
    if len(args) != 3 or (args[2] != 'g' and args[2] != 'r'):
        print("What are we doing here?")
        proper_usage()
        
    elif args[2] == 'g':
        
        try:
            file = open(args[1], "r")
        except:
            print("Error opening q1_input.txt\n")
            return
        
        inputs = file.readlines()
        
        try:
            t = int(inputs[0])
            n = int(inputs[1])
            s = int(inputs[2])
        except:
            print("Invalid input file\n")
            return
        file.close()

        if t > n:
            print("Inputs are not viable\n")
            print("t cannot be greater than n")
            return

        if t <= 0 or n <= 0 or s < 0:
            print("Inputs are not viable\n")
            print("t must be > 1")
            print("n must be > 1")
            print("s must be >= 0")
            return
        
        if str(t) != inputs[0].strip() or str(n) != inputs[1].strip() or str(s) != inputs[2].strip():
            print("Inputs are not viable\n")
            print("t, n, s must be whole numbers")
            return
        
        p = 2
        p = valid_prime(p, n, s)
        
        if p < s:
            print("Fatal error!\n")
            print("s cannot be greater than p")
            return
        
        coefficients = generate_coefficients(t, p, s)
        try:
            file = open("shares.txt", "w")
        except:
            print("error opening shares.txt :/\n")
            return
        
        file.write(str(p) + "\n")
        for x in range(1, n+1):        
            fx = f(x, p, t, coefficients)
            file.write(str(x) + " "+  str(fx) + "\n")
        file.close()
        print("You generated", n, "shares.")
        print()
        print("To maintain security of your system:")
        print("Meet up with whomeever you intend to give a share, or send each share over a cryptographically secure channel")
        print("Delete every share from this system")
        print("Store your share securely")
        print()
        
    elif args[2] == 'r':
        try:
            file = open(args[1], "r")
        except:
            print("error opening shares.txt :/\n")
        lines = file.readlines()
        file.close()
        
        shares = []
        for x in range(0, len(lines)):
            if x == 0:
                p = int(lines[0])
            else:
                shares.append((lines[x].strip()).split(" "))
        #print(shares)
        t = len(shares)
        
        freq = {}
        offenders = []

        for x in shares:
            if x[0] not in freq.keys():
                freq[x[0]] = 1
            else:
                offenders.append(x[0])
        if len(offenders) > 0:
            print("Invalid shares input!")
            print("Remove repeated shares (x, f(x)) with x value", offenders)
            return
            
        try:
            b = []
            for j in range(0, t):
                product = 1
                for k in range(0, t):
                    if k != j:
                        product *= (int((shares[k][0])) % p) * pow(int(shares[k][0]) - int(shares[j][0]), -1, p)
                b.append(product % p)
            #print(b)

            summation = 0
            for j in range(0, t):
                #print("product:", b[j], "*", shares[j][1],  "%", p)
                summation += b[j] * int(shares[j][1]) 
            secret = summation % p
            #print(secret)
        except:
            print("Interpolation failed... :/")
            return
        
        try:
            file = open("recoveredsecret.txt", "w")
        except:
            print("Error opening recoveredsecret.txt\n")
        file.write(str(int(secret)))
        file.close()
        print("You've recovered the secret")
        print()
        print("To maintain security of your system:")
        print("Thoroughly and securely delete the secret from the system")
        print("Delete all shares used to recover the secret from this system")
        print("If you want to resecure the secret, invalidate all old shares and create new shares")
        print()

if __name__ == "__main__":
    main()