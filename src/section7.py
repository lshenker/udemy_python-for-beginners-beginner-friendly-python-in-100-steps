import string

'upp'.upper().isupper()  # True
'LOW'.lower().islower()  # True
'cap'.capitalize().istitle()  # True

'123'.isdigit()  # True
'ABC'.isalpha()  # True
'ABC123'.isalnum()  # True

'Hello'.endswith('lo')  # True
'Hello'.startswith('lo')  # True

'Hello'.find('l')  # 2
'ABC'.find('BC')  # 1

bool('Any string possible')  # True
bool('')  # False

int('45abc', 16)  # hex

message = 'Hello'    # contents of string objects cannot be modified
message = 'Goodbye'  # the variable points to a different location in memory

type(message[0])  # no character data type

string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits  # '0123456789'
string.hexdigits  # '0123456789abcdefABCDEF'
string.punctuation  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace  # ' \t\n\r\x0b\x0c'
'abc' in string.ascii_lowercase  # True

vowels = 'aeiouAEIOU'
'z' in vowels  # False

for char in vowels:  # prints each vowel
    print(char)

long_message = "Hey, how's it going? I haven't seen you in a while!"
long_message.split()  # ['Hey,', "how's", 'it', 'going?', 'I', "haven't", 'seen', 'you', 'in', 'a', 'while!']
'1' * 10  # '1111111111'
