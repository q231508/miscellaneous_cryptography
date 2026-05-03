@
ciphertext = '''@ r@j4u l!jw6!d !t 6a@4uq d!w !drf @qq!m6@wup lj6b@mf n6w9
qumej6wf cew nudw !d w! juljuqudw lj6b@mf @q qumej6wf qumeju ql@mu !j
qumeju 6dt!ja@w6!d Qumej6wf 6q @d !bujr@ll6d4 cew @j4e@crf a!ju m!dmjuwu
p!a@6d w9@d lj6b@mf @q lj6b@mf 6dmrepuq m!alruv q!m6!merwej@r t@mw!jq
n96ru qumej6wf t!mequq a!ju !d l9fq6m@r ju@r6w6uq'''

x = 1
m = 1
attacking = True

index = list(ciphertext)
plaintext = list(ciphertext)
freq = {}
guesses={}

for x in index:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
del(freq[" "])
s = sum(freq.values())
for key in freq:
    freq[key] /= s    
    freq[key] *= 100
    freq[key] = round(freq[key], 2)
print("[Frequency]")
print(freq)
print("[Current CipherText]")
print(ciphertext)
print("[Assignments]")
print(guesses)
print()

while attacking:
    target = input("What character do you want to replace? ")
    guess = input("Your guess? ")
    guesses[target] = guess
    pos = []
    count = 0
    for x in range(0, len(index)):
        if index[x] == target:
            pos.append(x)

    #print(pos)
    for j in pos:
        plaintext[j] = guess
    print()
    print("[Frequency]")
    print(freq)
    print("[Attack Results]")
    print("".join(plaintext))
    print("[Assignments]")
    print(guesses)
    #print("".join(index))
    print()
    
    if input("Clear assignments? [y/n]") == "y":
        plaintext = list(ciphertext)
        guesses = {}
        print()
        print("[Frequency]")
        print(freq)
        print("[Current CipherText]")
        print(ciphertext)
        print("[Assignments]")
        print(guesses)
        print()
    else:
        print()
        print("[Frequency]")
        print(freq)
        print("[Current Ciphertext]")
        print("".join(plaintext))
        print("[Assignments]")
        print(guesses)
        print()
