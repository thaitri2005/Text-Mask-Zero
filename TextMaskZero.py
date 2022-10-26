# -*- code: ascii -*-
import random
dict = {'0':"\u200B", '1':"\u200C", ' ':"\u200D"}
key_list = list(dict.keys())
val_list = list(dict.values())


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text
        a Message object has one attribute:
            self.message_text (string, determined by input text)
            self.state (boolean, tells whether it is encoded or not)
        '''
        self.message_text = str(text)
        self.state = Message.isencoded(self.message_text)

    def __str__(self):
        return f"{self.message_text}"

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def isencoded(self):
        '''
        Check if the string given contains zero width characters or not
        Return: True if encoded, False if not
        '''
        result = False
        for character in str(self):
            if character in dict.values():
                result = True
                break
        return result



def binary_encoding(ascii_string):
    '''
    Used to change the message into binary form
    Return: a string of the binary form of the text
    '''
    ascii_string = str(ascii_string)
    l,msg=[],[]
    for i in ascii_string:
        l.append(ord(i))
    for i in l:
        msg.append(str(bin(i)[2:]))
    return str(' '.join(msg))

def zero_width_encoding(msg):
    '''
    Used to encode binary text into zero width characters
    Return: a zero width string'''
    result = ''
    for x in str(msg):
        result+= dict[x]
    return str(result)



def binary_decoding(binary_string):
    '''
    Used to change the binary text back into normal readable form
    Return: a string of the text in normal form
    '''
    binary_values = str(binary_string).split()

    ascii_string = ""
    for binary_value in binary_values:
        i = int(binary_value, 2)
        ascii_character = chr(i)
        ascii_string += ascii_character
    return str(ascii_string)

def zero_width_decoding(msg):
    '''
    Used to decode zero width characters back to binary
    Return: a binary string'''
    result = ''
    for x in str(msg):
        result+= key_list[val_list.index(x)]
    return str(result)

def strip_zerowidth(m):
    m = str(m)
    for k in dict:
        m = m.replace(dict[k],"")
    return m


def main(msg, mask =''):
    position =random.randint(0,len(mask))
    message = Message(msg)
    if not message.state:
        mask = strip_zerowidth(mask)
        msg = strip_zerowidth(msg)
        return mask[:position] + zero_width_encoding(binary_encoding(Message.get_message_text(message))) + mask[position:]
    else:
        mess = ''
        for character in Message.get_message_text(message):
            if character in val_list:
                mess+=character
        return binary_decoding(zero_width_decoding(mess))
