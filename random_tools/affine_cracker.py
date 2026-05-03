
ciphertext = "IqtqdgvactczgdqiebgdDMGkchebemyctmamvmczzathativwcdgthckldakqtekpqdmVramkemvpqhctqatmeyrgwgovrgvvrqmqldakqmwqdqtcvmqbqyvqhpogtoctqqbmqpqzcdqVrqldcpgpabavotcvvcdqiqtqdgvqgldakqamyckkqtmedgvqwavrvrqmqyedavobqnqbazTAMVmdqyckkqthgvact"

a = 0
m = 26
v = 0
n = 1
results = []
while n > 0:
    plaintext = ""
    try:
        pow(a, -1, 26)
    except:
        a+=1
        continue
    for x in range(0, 26):
        plaintext = ""
        try:
            pow(x, -1, 26)
        except ValueError:
            continue
        for char in ciphertext:
            inv = pow(a, -1, m)
            if ord(char) <= 90:
                d = inv*((ord(char) - 65) - x)%26
                d = chr(d+64)
            else:
                d = inv*((ord(char) - 97) - x)%26
                d = chr(d+96)
            plaintext+=d
        print(plaintext)
        print("a:", a, "x:", x)
        print("Try again?")
        print("[q to quit]")
        print("[r to see past results]")
        i = input("[press enter to try again]")
        results.append((("a:", a),("x:", x), plaintext))
        print()
        if i.lower().strip() == "q":
            v = x
            n = 0
            break
        elif i.lower().strip() == "r":
            print("[Past results]")
            for x in results:
                print(x)
                print()
            i = input("[press enter to return to attempts]")
            print()
    if a >26:
        break
    a+=1