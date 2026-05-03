import random
import sys
import ast
import math
from sympy import nextprime, randprime

def encrypt(m, N, r, g):
    c1 = pow(g, m, N*N)
    c2 = pow(r, N, N*N)
    c = (c1 * c2) 
    c = c % (N*N)
    return c

def L(x, n):
    return (x - 1) // n

def main(argc, argv):
    if argc != 2:
        print("Usage: python encrypt.py inputfile.txt\n")
        return
    try:
        inputfile = argv[1]
        with open(inputfile, 'r') as f:
            lines = f.readlines()
            coefficients = ast.literal_eval(lines[0].strip())
            x = int(lines[1].strip())
            degree = len(coefficients) - 1
            f.close
    except:
        print("Error reading input file.\n")
        return
    
    p = randprime(2**100, 2**101)
    q = randprime(2**100, 2**101)
    while p == q:
        p = randprime(2**100, 2**101)
    N = p * q
    
    g = N+1
    h = math.lcm(p-1, q-1)
    while math.gcd(L(pow(g, h, N*N), N), N) != 1:
        g = random.randint(1, N*N)
        
    used_r = {}
    encrypted_coefficients = []
    for coefficent in coefficients:
        r = random.randint(1, N-1)
        while math.gcd(r, N) != 1 or r in used_r:
            r = random.randint(1, N-1)
        m = coefficent 
        encrypted_c = encrypt(m, N, r, g)
        encrypted_coefficients.append(encrypted_c)
        used_r[r] = True

    f = open("keys.txt", "w")
    f.write(f"[{N}, {g}]\n")
    f.write(f"[{p}, {q}]")
    f.close()
    
    f = open("out.txt", "w")
    f.write(f"{encrypted_coefficients}\n")
    f.write(f"[{N}, {g}]\n")
    f.write(f"{x}\n")
    f.write(f"{degree}")
    f.close()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv[:])