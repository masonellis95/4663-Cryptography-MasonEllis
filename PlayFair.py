import pprint
import re

class StringManip:
    """
    Helper class to speed up simple string manipulation
    """

    def generateAlphabet(self):
        #Create empty alphabet string
        alphabet = ""

        #Generate the alphabet
        for i in range(0,26):
            alphabet = alphabet + chr(i+65)

        return alphabet


    def cleanString(self,s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
        """
        Cleans message by doing the following:
        - up            - uppercase letters
        - spLetters     - split double letters with some char
        - reSpaces      - replace spaces with some char or '' for removing spaces
        - reNonAlphaNum - remove non alpha numeric
        - reDupes       - remove duplicate letters
        @param   string -- the message
        @returns string -- cleaned message
        """
        if 'up' in options:
            s = s.upper()

        if 'spLetters' in options:
            #replace 2 occurences of same letter with letter and 'X'
            s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)

        if 'reSpaces' in options:
            space = options['reSpaces']
            s = re.sub(r'[\s]', space, s)

        if 'reNonAlphaNum' in options:
            s = re.sub(r'[^\w]', '', s)

        if 'reDupes' in options:
            s= ''.join(sorted(set(s), key=s.index))

        return s


class PlayFair:
    """
    Class to encrypt via the PlayFair cipher method
    Methods:
    - generateSquare
    - transposeSquare
    -
    """

    def __init__(self,key,message):
        self.Key = key
        self.Message = message
        self.Square = []
        self.Transposed = []
        self.StrMan = StringManip()
        self.Alphabet = ""

        self.generateSquare()
        self.transposeSquare()

        self.Message = self.StrMan.cleanString(self.Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':1})
        self.EvenLength()
        
    def EvenLength(self):
        if len(self.Message) % 2 == 1:
            self.Message += 'X'

    def generateSquare(self):
        """
        Generates a play fair square with a given keyword.
        @param   string   -- the keyword
        @returns nxn list -- 5x5 matrix
        """
        row = 0     #row index for sqaure
        col = 0     #col index for square

        #Create empty 5x5 matrix
        self.Square = [[0 for i in range(5)] for i in range(5)]

        self.Alphabet = self.StrMan.generateAlphabet()

        #uppercase key (it meay be read from stdin, so we need to be sure)
        self.Key = self.StrMan.cleanString(self.Key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})

        #Load keyword into square
        for i in range(len(self.Key)):
            self.Square[row][col] = self.Key[i]
            self.Alphabet = self.Alphabet.replace(self.Key[i], "")
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

        #Remove "J" from alphabet
        self.Alphabet = self.Alphabet.replace("J", "")

        #Load up remainder of playFair matrix with
        #remaining letters
        for i in range(len(self.Alphabet)):
            self.Square[row][col] = self.Alphabet[i]
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

    def transposeSquare(self):
        """
        Turns columns into rows of a cipher square
        @param   list2D -- playFair square
        @returns list2D -- square thats transposed
        """
        #Create empty 5x5 matrix
        self.Transposed = [[0 for i in range(5)] for i in range(5)]

        for col in range(5):
            for row in range(5):
               self.Transposed[col][row] = self.Square[row][col]


    def getCodedDigraph(self,digraph):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- encoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])

       # print(location1)
        #print(location2)

        #print(self.Square[location1[0]][location2[1]])
        #print(self.Square[location2[0]][location1[1]])

        return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]
        
        
    """
    getDeCodedDigraph(digraph)
    Parameters: self, digraph: a list of two ints.
    Return Type: digraph
    
    This method will return the decoded digraph give an encoded 
    digraph. It will basically undo the getCodedDigraph method
    by preforming the inverse of those operations.
    
    """    
    def getDeCodedDigraph(self,digraph):
    
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])

        return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]

    def getLocation(self,letter):
        row = 0
        col = 0

        count = 0
        for list in self.Square:
            if letter in list:
                row = count
            count += 1

        count = 0
        for list in self.Transposed:
            if letter in list:
                col = count
            count += 1
        return [row,col]
        
    """
    EncryptMessage()
    Parameters: Self
    Return Value: String
    
    This method will Encrypt the entire message
    and return the string "Cipher_Text" with the 
    encoded message. This method will utilize the 
    getCodedDigraph method.
    """
    def EncryptMessage(self):
        Cipher_Text = ""
        Count = 0
        OldDigraph = ["",""]
        NewDigraph = ["",""]
        while (Count < len(self.Message)):
            OldDigraph[0] = self.Message[Count]
            OldDigraph[1] = self.Message[Count + 1]
            NewDigraph = self.getCodedDigraph(OldDigraph)
            Cipher_Text += NewDigraph[0]
            Cipher_Text += NewDigraph[1]
            Count += 2
        return Cipher_Text
        
         
    """
    DecryptMessage()
    Parameters: Self
    Return Value: String
    
    This Functions will Decrypt the entire message
    and return the string "Plain_Text" with the 
    decoded message. This method will utilize the 
    getDeCodedDigraph method.
    """   
    def DecryptMessage(self):
        Plain_Text = ""
        Count = 0
        OldDigraph = ["",""]
        NewDigraph = ["",""]
        while (Count < len(self.Message)):
            OldDigraph[0] = self.Message[Count]
            OldDigraph[1] = self.Message[Count + 1]
            NewDigraph = self.getDeCodedDigraph(OldDigraph)
            Plain_Text += NewDigraph[0]
            Plain_Text += NewDigraph[1]
            Count += 2
        return Plain_Text
            
    #############################################
    # Helper methods just to see whats going on
    #############################################
    def printNewKey(self):
        print(self.Key)

    def printNewMessage(self):
        print(self.Message)

    def printSquare(self):
        for list in self.Square:
            print(list)
        print('')

    def printTransposedSquare(self):
        for list in self.Transposed:
            print(list)
        print('')


##########################################################
##########################################################
 
# Selector is for the user to select which option they want.
Selector = 0
# The Plain text that the user will input
Plain_Text = ""
# The Encrypted Text
Cipher_Text = ""
# The keyword
Key = ""

print("What would you like to do?")
print("1. Encrypt A Message.")
print("2. Decrypt A Message.")
print("3. Quit.")

# The user will input the selector
Selector = input()

# This loop validates the input
# The user will be continuously propmted until
# they enter a valid selection.
while Selector < 1 or Selector > 3:
    print("Invalid input. Please try again.")
    Selector = input()
    
# Will loop until the user types a 3(To Quit)
while Selector != 3:
    
    # If the user selects a 1 (Encryption)
    if Selector == 1:
        # The user will enter a message to be encrypted.
        Plain_Text = raw_input("Please Enter the Message:")
        # The user will enter a Keyword.
        Key = raw_input("Please Enter the Key:")
        Cipher = PlayFair(Key, Plain_Text)        
        
        #The Cipher object will preform the encryption.
        Cipher_Text = Cipher.EncryptMessage()
        print(Cipher_Text)
        
    # If the user selects a 2 (Decryption)
    if Selector == 2:
        # The user will enter an Encrypted message to Decrypt.
        Cipher_Text = raw_input("Please Enter the Message:")
        # The user will enter the keyword.
        Key = raw_input("Please Enter the Key:")
        Cipher = PlayFair(Key, Cipher_Text)
        
        # The Cipher object will preform the decryption.
        Plain_Text = Cipher.DecryptMessage()
        print(Plain_Text) 
             
    # Reprints the Menu options for the user to make another selection.
    print("Please make another selection:")
    print("1. Encrypt A Message.")
    print("2. Decrypt A Message.")
    print("3. Quit.")
    Selector = input()    
    
    #Validates the Input.
    while Selector < 1 or Selector > 3:
        print("Invalid input. Please try again.")
        Selector = input()

#When the user types a 3, The program will end with this message.
print("Thank you using PlayFair.py")
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     


