#
# HSGC Intro to CS
# Spring 2015
# Cryptography Project Help
#
# This is code to help you with the substitution cipher if you get stuck.
# This code WILL NOT run, but all the lines of code and variables you need are here.
# You will need to write what to assign to each variable.
#
# A.) Use this code as a hint, or 
# B.) Replace your code's functions with these, then fill in the blanks.
#
# If you use this helping code, you MUST write a comment about EACH LINE.
# Tell us in English what that line does. (It may only be a few words.)
#
# Use # to write a comment.
#

print("Example comment line. Ignore me.") # Comments can come at the end of the line.


def encrypt_substitution(plain_text, substitution_string):
    if len(substitution_string) < len(alphabet):
        return "STUDENT: Describe why we have to bail out early here."
    if len(substitution_string) > len(alphabet):
        return "STUDENT: Describe why we have to bail out early here."
	
    cipher_text =
    for plain_letter in plain_text:
        if plain_letter in alphabet:
            letter_index =
            cipher_letter =
            cipher_text =
        else:
            cipher_text =
    return cipher_text


def decrypt_substitution(cipher_text, substitution_string):
    if len(substitution_string) < len(alphabet):
        return "STUDENT: Describe why we have to bail out early here."
    if len(substitution_string) > len(alphabet):
        return "STUDENT: Describe why we have to bail out early here."
    
    plain_text =
    for cipher_letter in cipher_text:
        if cipher_letter in substitution_string:
            letter_index =
            plain_letter =
            plain_text =
        else:
            plain_text =
    return plain_text
