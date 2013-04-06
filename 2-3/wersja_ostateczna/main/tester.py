'''
Created on Mar 25, 2013

@author: dracco
'''
from cyphers.rail import rail
from cyphers.matrix_translation_a import matrix_translation_a

def uni_test(cypher, name, keys, word="enciphered", errors_only=True):
    success = True
    for key in keys:
        c = cypher(key)
        try:
            assert c.decrypt_button(c.encrypt_button(word)) == word
        except:
            success = False
            print   "Key", "`" + key.__str__() + "`",\
                    "failed the test using word", "`" + word + "`"
        else:
            if not errors_only:
                print "Key", "`" + key.__str__() + "`", "passed the test"
    print "Test of", "`" + name + "`", "succeeded" if success else "failed"

if __name__ == '__main__':
    uni_test(rail, "Rail Fence",
             [2, 3, 4, 5, 6])
    uni_test(matrix_translation_a, "Matrix Transformation A",
             ["1-2-3-4","1-4-2-3","1-5-6-2-3-4"])
    pass