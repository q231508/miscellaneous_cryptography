import ast
import sys
import math

def L(x, n):
    return (x - 1) // n

def main(argc):
    if argc != 1:
        print("Usage: python decrypt.py\n")
        return
    try:
        inputfile = "encryptedresult.txt"
        with open(inputfile, 'r') as f:
            lines = f.readlines()
            c = int(lines[0].strip())
            f.close()
    except:
        print("Error reading result file.\n")
        return
    try:
        inputfile = "keys.txt"
        with open(inputfile, 'r') as f:
            lines = f.readlines()
            keys = ast.literal_eval(lines[0].strip())
            N = keys[0]
            g = keys[1]
            private_keys = ast.literal_eval(lines[1].strip())
            p = private_keys[0]
            q = private_keys[1]
            f.close()
    except:
        print("Error reading keys file.\n")
        return
    
    h = math.lcm(p-1, q-1)
    c_lambda = pow(c, h, N*N)
    g_lambda = pow(g, h, N*N)
    top = L(c_lambda, N)
    bot = L(g_lambda, N)
    
    bot_inv = pow(bot, -1, N)
    m = (top * bot_inv) % N

    print(m)

if __name__ == "__main__":
    main(len(sys.argv))