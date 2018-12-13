#Created by Oranje Maan
#13 December 2018

def Caesar(message,key):
    #Caesar Cipher. Shall shift the message by a key amount.
    output = ""
    #Checking if message and key are string and int respectfully
    if not (all(ord(i) <= 126 for i in message) and all(ord(i) >= 33 for i in message)):
        print("Error - Message uses characters beyond allowed.") 
        return
    try:
        int(key)
    except:
        print("Error - Key is not an integer.")
        return
    else:
        b = int(key)
    #Commencing cipher
    for i in range(len(message)):
        a = ord(message[i])
        if((a + b) > 126):
            output += chr((a + b)-94)
        else:
            output += chr(a + b)
    return output

def CaesarDecrypt(message,key):
    #Shall decrypt a message via a key
    output = ""
    #Checking if message and key are string and int respectfully
    if not (all(ord(i) <= 126 for i in message) and all(ord(i) >= 33 for i in message)):
        print("Error - Message uses characters beyond allowed.") 
        return
    try:
        int(key)
    except:
        print("Error - Key is not an integer.")
        return
    else:
        b = int(key)
    #Commencing decrypting
    for i in range(len(message)):
        a = ord(message[i])
        if((a - b) < 33):
            output += chr((a - b) + 94)
        else:
            output += chr(a - b)
    return output

def Vingenere(message,key):    
    #Vingenere Cipher. Shall encrypt a message via Vingenere Cipher method. Requires a message to encrypt and a string to use as the encryption key.
    lstAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    output = ""
    message = message.lower()
    key = key.lower()
    #Checking if both the message and key are made up of only letters
    for i in message:
        if not(i in lstAlphabet):
            print("Error - Message contains non-alphabetical letters.")
            return
    for i in key:
        if not(i in lstAlphabet):
            print("Error - Key contains non-alphabetical letters.")
            return
    #Commencing Vingenere Cipher
    for i in range(len(message)):
        a = lstAlphabet.index(message[i])
        b = lstAlphabet.index(key[i % len(key)])
        if ((a + b) > 26):
            output += lstAlphabet[a + b - 26]
        else:
            output += lstAlphabet[a + b]
    return output

def VingenereDecrypt(message,key):
    #Shall decrypt a message via vingenere method. Requires message and key.
    lstAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    output = ""
    message = message.lower()
    key = key.lower()
    #Checking if both the message and key are made up of only letters
    for i in message:
        if not(i in lstAlphabet):
            print("Error - Message contains non-alphabetical letters.")
            return
    for i in key:
        if not(i in lstAlphabet):
            print("Error - Key contains non-alphabetical letters.")
            return
    #Commencing Vingenere Cipher
    for i in range(len(message)):
        a = lstAlphabet.index(message[i])
        b = lstAlphabet.index(key[i % len(key)])
        if ((a - b) < 0):
            output += lstAlphabet[a - b + 26]
        else:
            output += lstAlphabet[a - b]
    return output
    
def Main():
    #Testing Caesar Encryption/Decryption
    a = input("Give a message: ")
    b = input("Give a key as a number: ")
    c = Caesar(a,b)
    print("The string " + a + " shifted " + b + " times is " + c)
    print(CaesarDecrypt(c,b))
    #Testing VingenereEncryption/Decryption
    a = input("Give a message: ")
    b = input("Give a key as a string: ")
    c = Vingenere(a,b)
    print("The string " + a + " set to the key " + b + " is " + c)
    print(VingenereDecrypt(c,b))

Main()
