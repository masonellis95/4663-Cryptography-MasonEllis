###############################################
# Name: Mason Ellis
# Class: CMPS 46663 Cryptography
# Date: 27 July 2015
# Program 2 - Randomized Vigenere
###############################################

import argparse
import sys
import random
import randomized_vigenere as rv

def main():
    #Allows us to input command line arguements
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

    args = parser.parse_args()
    
    #Seeds the random number generator with the seed from the user.
    random.seed(args.seed)   
    #Generates a keyword from the seed.
    keyword = rv.keywordFromSeed(args.seed)

    #Our "Alphabet"
    symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    #Builds the Vigenere table    
    vigenere = rv.buildVigenere(symbols)
    
    #Opens The input File
    f = open(args.inputFile,'r')
    #Reads the message from the input file for reading.
    message = f.read()
    
    #If the mode is encrypt, the message will be encrypted,
    #Else, it will be decrypted.
    if(args.mode == 'encrypt'):
        data = rv.encrypt(vigenere, message, keyword)
    else:
        data = rv.decrypt(vigenere, message, keyword)
    #opens the output file for writing and writes the data to the file.
    o = open(args.outputFile,'w')
    o.write(str(data))

    

if __name__ == '__main__':
    main()