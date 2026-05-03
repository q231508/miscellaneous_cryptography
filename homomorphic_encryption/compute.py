import ast
import sys

def main(argc):
    if argc != 1:
        print("Usage: python compute.py\n")
        return
    try:
        inputfile = "out.txt"
        with open(inputfile, 'r') as f:
            lines = f.readlines()
            encrypted_coefficients = ast.literal_eval(lines[0].strip())
            keys = ast.literal_eval(lines[1].strip())
            N = keys[0]
            g = keys[1]
            
            x = int(lines[2].strip())
            degree = int(lines[3].strip())
            f.close
    except:
        print("Error reading input file.\n")
        return
    
    evaluated_polynomial = 1
    for i in range(degree + 1):
        c = encrypted_coefficients[i]
        input_value = pow(x, i)
        cx = pow(c, input_value, N*N)
        evaluated_polynomial = (evaluated_polynomial * cx) % (N*N)
    f = open("encryptedresult.txt", "w")
    f.write(f"{evaluated_polynomial}\n")
    f.close()

if __name__ == "__main__":
    main(len(sys.argv))
