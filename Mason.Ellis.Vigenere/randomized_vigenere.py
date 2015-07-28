import random

"""
    buildVigenere(symbols)
    
    @param1 symbols-string

    This function will build a randomized Vigenere table out of a given keyword.
"""
def buildVigenere(symbols):

    #calculates the length of the message
    n = len(symbols)

    vigenere = [[0 for i in range(n)] for i in range(n)]

    #Build the vigenere matrix
    for i in range(n):
        for j in range(n):
            vigenere [i][j] = symbols[(i + j) % n]
    #Shuffles the rows.
    random.shuffle(vigenere)
    return vigenere
    
"""
    encrypt(V,Plain_Text,Keyword)
    
    @param1 V- nXn matrix:
        V is the matrix created to encrypt the message
    @param2 Plain_Text- string:
        The message to be encrypted
    @param3 Keyword- string:
        The keyword used to encrypt.
"""    
def encrypt(V,Plain_Text, Keyword):
    #An empty list for the Encrypted message
    Cipher_Text = []    
    
    #loops through the message
    for i in range (len(Plain_Text)):
        #Finds the look up indecies
        MIndex = symbols.find(Plain_Text[i])
        KIndex = symbols.find(Keyword[i % len(Keyword)])
        Cipher_Text.append(V[KIndex][MIndex])
     
    # converts to string
    Cipher_Text = "".join(Cipher_Text)
    return Cipher_Text
   
"""
    decrypt(V,Cipher_Text,Keyword)
    
    @param1 V- nXn matrix:
        V is the matrix created to encrypt the message
    @param2 Cipher_Text- string:
        The message to be decrypted
    @param3 Keyword- string:
        The keyword used to encrypt.
"""    
def decrypt(V,Cipher_Text, Keyword):
    #Empty list for the decrypted message.
    Plain_Text = []
    
    #Loops through cipher text
    for i in range(len(Cipher_Text)):
        #Finds the look up indecies
        KIndex = symbols.find(Keyword[i % len(Keyword)])
        MIndex = V[KIndex].index(Cipher_Text[i])
        
        Plain_Text.append(symbols[MIndex])
    #converts to string   
    Plain_Text = "".join(Plain_Text)
    return Plain_Text
 
#############################################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
#############################################################################  
def keywordFromSeed(seed):
    Letters = []
    seed = int(seed)

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)

#The string used to created the matrix.
symbols = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
