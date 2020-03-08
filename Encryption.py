class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        alphabet = {}
        lower = {}
        upper = {}
        Lletters = []
        for i in string.ascii_lowercase:
            Lletters.append(i)
        Uletters = []
        for i in string.ascii_uppercase:
            Uletters.append(i)
        Llettershift = Lletters[:]
        Ulettershift = Uletters[:]
        while shift > 0:
            Llettershift = Llettershift[1:] + Llettershift[0:1]
            Ulettershift = Ulettershift[1:] + Ulettershift[0:1]
            shift -= 1
        j = 0
        for i in range(len(Lletters)):    
            lower[Lletters[i]] = Llettershift[j]
            j += 1
        j = 0
        for i in range(len(Uletters)):    
            upper[Uletters[i]] = Ulettershift[j]
            j += 1
        for key, value in lower.items():
            alphabet[key] = value
        for key, value in upper.items():
            alphabet[key] = value
        return alphabet
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifter = self.build_shift_dict(shift)
        newscript = ""
        for i in self.message_text:
            try:
                newscript += shifter[i]
            except:
                newscript += i
        return(newscript)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.nshift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.nshift)
        self.message_text_encrypted = Message.apply_shift(self, self.nshift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.nshift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        newdict = {}
        for k,y in self.encrypting_dict.items():
            newdict[k] = y
        return newdict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.nshift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.nshift)
        self.message_text_encrypted = Message.apply_shift(self, self.nshift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        bestshift = 0
        besttranslate = None
        translatescore = 0
        shift = 0
        first = True
        while shift < 26 :
            currenttranslate = ""
            currenttranslatescore = 0
            shifter = Message.build_shift_dict(self, shift)
            newscript = Message.apply_shift(self, shift)
            lscript = newscript.split(" ")
            for i in lscript:
                if i in self.valid_words:
                    currenttranslatescore += 1
                word = i + " "
                currenttranslate += word
            if first or translatescore < currenttranslatescore:
                translatescore = currenttranslatescore
                besttranslate =  currenttranslate[:-1]
                bestshift = shift
            shift += 1
            first = False
        return bestshift, besttranslate

def decrypt_story():
    return CiphertextMessage(get_story_string()).decrypt_message()
               
                   
           