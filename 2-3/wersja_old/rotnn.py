#!/usr/bin/python
import string

## rotNN.py ####################################################################
#
# RotNN.py is a python library that allows you to do character 'rotation' of 
# any length you want.  Default is 13, so a straight rotnn.rotate(string) is
# equivalent to a rot13 encryption.

# One word about that:  Rot13 isn't really much for encryption.  It is an
# excellent tool for obfuscation and whatnot, but if you really want to keep
# your information secure, you'd be much better off going with a stronger
# scheme.  However, I must say that an srotation followed by a rotation is 
# enough to keep out a majority of the people in the world.  And it's quick,
# too.

# Usage: Run this module by itself to see the test cases print out.  I find
# that a few examples is worth more than me giving you lots of (s [,n])'s.

# Note: As of rotnn-1.1, this module should come with a script (which 
# might or might not be named rotnn_test_script.py) that does some 
# semi-cool stuff that you might enjoy playing with.  Give it a whack.

#!/usr/local/bin/python
import string

__version__ = "1.1"

def rotate(a_string, amount=13):
        if (amount > 26) or (amount < 0):
                raise ValueError, "Invalid Rotation Value"
        char_list = []
        for single_char in a_string:
                ord_char = ord(single_char)
                if (65 <= ord_char <= (90-amount)) or (97 <= ord_char <= (122-amount)):
                        char_list.append (chr(ord_char + amount))
                elif ((91-amount) <= ord_char <= 90):
                        char_list.append (chr(65 + (amount - (91 - ord_char))))
                elif ((123-amount) <= ord_char <= 122):
                        char_list.append (chr(97 + (amount - (123 - ord_char))))
                else:
                        char_list.append (chr(ord_char))
        ret_str = string.join(char_list,"")
        return (ret_str)

def unrotate(a_string, amount=13):
        ret_str = rotate(a_string, 26 - amount)
        return (ret_str)

def srotate(a_string, amount=26):
        if (amount > 94) or (amount < 0):
                raise ValueError, "Invalid Rotation Value"
        char_list = []
        for single_char in a_string:
                ord_char = ord(single_char)
                if (32 <= ord_char <= (126-amount)):
                        char_list.append(chr(ord_char + amount))
                elif ((127-amount) <= ord_char <= 126):
                        char_list.append(chr(31 + (amount - (126 - ord_char))))
                else:
                        char_list.append(chr(ord_char))
        ret_str = string.join(char_list, "")
        return (ret_str)

def sunrotate(a_string, amount=26):
        ret_str = srotate(a_string, 95 - amount)
        return (ret_str)

def wrotate(a_string, amount=47):
        if (amount > 94) or (amount < 0):
                raise ValueError, "Invalid Rotation Value"
        char_list = []
        for single_char in a_string:
                ord_char = ord(single_char)
                if (33 <= ord_char <= (126-amount)):
                        char_list.append(chr(ord_char + amount))
                elif ((127-amount) <= ord_char <= 126):
                        char_list.append(chr(32 + (amount - (126 - ord_char))))
                else:
                        char_list.append(chr(ord_char))
        ret_str = string.join(char_list, "")
        return (ret_str)

def wunrotate(a_string, amount=47):
        ret_str = wrotate(a_string, 94 - amount)
        return (ret_str)

if __name__ == '__main__':
        foo_str = rotate("The Quick BROWN fox jumped over the lazy DoG!?")
        print foo_str
        foo_str = unrotate(foo_str)
        print foo_str
        foo_str = srotate("Try this -- http://www.foobar.com:8080", 26)
        print foo_str
        foo_str = sunrotate(foo_str, 26)
        print foo_str
        foo_str = wrotate("Try this -- http://www.foobar.com:8080")
        print foo_str
        foo_str = wrotate(foo_str)
        print foo_str

