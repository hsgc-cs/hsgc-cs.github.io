alphabet = "abcdefghijklmnopqrstuvwxyz"


def index_of_letter(letter):
    return alphabet.index(letter)


def index_of_element_in_list(element, a_list):
    return a_list.index(element)


def encrypt_caesar(plaintext, encryption_key):
    return "this is some placeholder encrypted text. remove this and finish this function!"


def decrypt_caesar(ciphertext, encryption_key):
    return "this is some placeholder decrypted text. remove this and finish this function!"


def encrypt_substitution(plaintext, substitution_table):
    return "this is some placeholder encrypted text. remove this and finish this function!"


def decrypt_substitution(ciphertext, substitution_table):
    return "this is some placeholder decrypted text. remove this and finish this function!"


def encrypt_vigenere(plaintext, encryption_text):
    return "this is some placeholder encrypted text. remove this and finish this function!"


def decrypt_vigenere(ciphertext, encryption_text):
    return "this is some placeholder decrypted text. remove this and finish this function!"


def main():
    print "Welcome to the crypto project."
    print "Which cipher would you like to use?"
    print "    1) Caesar Cipher"
    print "    2) Substitution Cipher"
    print "    3) Vigenere Cipher"
    cipher = int(raw_input("Enter the number of your choice: "))

    print ""
    print "Would you like to encrypt or decrypt??"
    print "    1) Encrypt"
    print "    2) Decrypt"
    operation = int(raw_input("Enter the number of your choice: "))

    if operation == 1:
        plaintext = raw_input("\nEncrypting, Enter plaintext: ")

        if cipher == 1:
            encryption_key = int(raw_input("Enter your encryption key: "))
            print ""
            print "CIPHERTEXT: " + encrypt_caesar(plaintext, encryption_key)
        elif cipher == 2:
            substitution_table = raw_input("Enter your substitution table: ")
            print ""
            print "CIPHERTEXT: " + encrypt_substitution(plaintext, substitution_table)
        elif cipher == 3:
            encryption_text = raw_input("Enter your encryption text. Must be as long or longer than your message: ")
            print ""
            print "CIPHERTEXT: " + encrypt_vigenere(plaintext, encryption_text)
        else:
            print "Please enter a valid choice. Try again."

    elif operation == 2:
        ciphertext = raw_input("\nDecrypting, Enter ciphertext: ")

        if cipher == 1:
            encryption_key = int(raw_input("Enter your encryption key: "))
            print ""
            print "PLAINTEXT: " + decrypt_caesar(ciphertext, encryption_key)
        elif cipher == 2:
            substitution_table = raw_input("Enter your substitution table: ")
            print ""
            print "PLAINTEXT: " + decrypt_substitution(ciphertext, substitution_table)
        elif cipher == 3:
            encryption_text = raw_input("Enter your encryption text. Must be as long or longer than your message: ")
            print ""
            print "PLAINTEXT: " + decrypt_vigenere(ciphertext, encryption_text)
        else:
            print "Please enter a valid choice. Try again."

    else:
        print "Please enter a valid choice. Try again."


def test_crypto_function(function, plaintext, expected_text, key):
    encrypted_text = function(plaintext, key)
    function_success = expected_text == encrypted_text
    if function_success:
        print function.__name__ + "() is implemented correctly :)"
    else:
        print function.__name__ + '("' + plaintext + ", " + str(key) + ") is not implemented correctly"
        print "* Expected: " + expected_text
        print "* Returned: " + encrypted_text + ""


def test():
    test_crypto_function(encrypt_caesar, "party this saturday", "whyaf aopz zhabykhf", 7)
    test_crypto_function(decrypt_caesar, "whyaf aopz zhabykhf", "party this saturday", 7)
    test_crypto_function(encrypt_substitution, "party this saturday", "kfmsy soph hfstmbfy", "fgabcijopqrdewxklmhstuvnyz")
    test_crypto_function(decrypt_substitution, "kfmsy soph hfstmbfy", "party this saturday", "fgabcijopqrdewxklmhstuvnyz")


print ""
test()
print ""
main()
