import TextMaskZero
import string
import random
dict = {'0':"\u200B", '1':"\u200C", ' ':"\u200D"}
key_list = list(dict.keys())
val_list = list(dict.values())

def is_binary(x):
    state = True
    for character in str(x):
        if character not in key_list:
            state = False
    return state
def test_binary_encoding():
    assert is_binary(TextMaskZero.binary_encoding(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1,9))))) == True

def test_binary_decoding():
    initial_message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1,9)))
    assert is_binary(TextMaskZero.binary_decoding(TextMaskZero.binary_encoding(initial_message))) == False
    assert TextMaskZero.binary_decoding(TextMaskZero.binary_encoding(initial_message)) == initial_message


def test_zero_width_encoding():
    test_string = TextMaskZero.Message(TextMaskZero.zero_width_encoding(TextMaskZero.binary_encoding(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1,9))))))
    assert TextMaskZero.Message.isencoded(test_string) == True

def test_zero_width_decoding():
    initial =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1,9)))
    test_string = TextMaskZero.Message(TextMaskZero.zero_width_encoding(TextMaskZero.binary_encoding(initial)))
    assert TextMaskZero.Message.isencoded(TextMaskZero.binary_decoding(TextMaskZero.zero_width_decoding(test_string))) == False
    assert TextMaskZero.binary_decoding(TextMaskZero.zero_width_decoding(test_string)) == initial


def test_binary():
    assert TextMaskZero.binary_decoding(TextMaskZero.binary_encoding("hi")) == "hi"
    assert TextMaskZero.binary_decoding(TextMaskZero.binary_encoding("hello, world")) == "hello, world"
    initial_mess = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1,20)))
    assert TextMaskZero.binary_decoding(TextMaskZero.binary_encoding(initial_mess)) == initial_mess
    assert TextMaskZero.binary_decoding(TextMaskZero.binary_encoding("The fundamental currency of the universe is energy")) == "The fundamental currency of the universe is energy"