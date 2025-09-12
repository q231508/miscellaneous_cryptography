from operator import xor

discoveredWordLength = 3 # Tells the algorithm to only return results if the found word is of length x

def ascii_XOR(c1, c2):
# XOR two ascii ciphertexts
#**************************    
    result = []
    x = 0
    while x < len(c1):
        result.append(xor(ord(c1[x]), ord(c2[x])))
        x += 1
    return result

def hex_XOR(c1, c2):
# XOR two hex ciphertexts
#**************************    
    result = []
    x = 0
    while x < len(c1):
        result.append(xor(int(c1[x]+c1[x+1], 16), int(c2[x]+c2[x+1], 16)))
        x+=2
    return result

def auto(cipher, guessList, checkList):
# Automatically guess
# **************
    mode = "auto"
    for word in guessList:   
        cribdrag(cipher, "" + word.strip() + "", guessList, checkList, mode)

def manual(cipher, checkList, guess):
# Manually guess
# **************
    mode = "manual"
    cribdrag(cipher, guess, checkList, checkList, mode)
    
def cribdrag(cipher, word, guessList, checkList, mode):
# Drags our guess across the result of XORing c1 and c2
    wordLength = len(word)
    for x in range(0, len(cipher)-wordLength+1):
        result = ""
        for index in range(0, wordLength):
            result += chr(cipher[x + index]^ord(word[index]))
        check(checkList, result, word, mode)

def check(checkList, result, guess, mode):
# Prints result of cribdragging our guess
# Automatic guess only return matching words
    global discoveredWordLength
    match = 0
    for word in checkList:  
        if (""+(word.lower()).strip()+"") in result.lower() and len(word.strip()) >= discoveredWordLength:
            match += 1
            print(result + " | Guess: [" + guess + "] Found word: [" + word.strip() + "]")   
    if match == 0 and mode == "manual":
        print(result)
       
def main():
    global discoveredWordLength
    
    file = "D:/Downloads/cribdrag_wordlist.txt" # File path to wordlist with guesses
    guessList = open(file, 'r').readlines()

    file2 = "D:/Downloads/cribdrag_wordlist2.txt" # File path to wordlist we want to check against
    checkList = open(file2, 'r').readlines()
    
    # hex encoded ex
    #c1 = "2c1549100043130b1000290a1b"
    #c2 = "3f16421617175203114c020b1c" 
    #cipher = hex_XOR(c1, c2)
    
    # ascii encoded ex
    c1 = "ie|}m"
    c2 = "vob}f"
    cipher = ascii_XOR(c1, c2)

    try:
# Pick one: auto or manual
#   Do you want to guess and check from one wordlist?
#   Provide the same list as arg 2 and 3!
#   ex: auto(cipher, guessList, guesslist)
#***********
        discoveredWordLength = 4
        auto(cipher, checkList, checkList) 
        #manual(cipher, checkList, "world")
        print(cipher)
    except KeyboardInterrupt:
        print()
        print("You stopped checking...")
        print(cipher)

if __name__ == "__main__":
    main()
