#
# If you use this helping code, you MUST write a comment about EACH LINE.
# Tell us in English what that line does. (It may only be a few words)
#
# Use # to write a comment.
#

print("Example comment line. Ignore me.") # Comments can come at the end of the line.

def encrypt_caesar(plain_text, encryption_key):
    cipher_text =
    for plain_letter in plain_text:
        if plain_letter in alphabet:
            plain_letter_index =
            shifted_index =
            cipher_index =
            cipher_letter =
            cipher_text +=
        else:
            cipher_text +=
    return cipher_text


def decrypt_caesar(cipher_text, decryption_key):
    plain_text =
    for cipher_letter in plain_text:
        if cipher_letter in alphabet:
            cipher_letter_index =
            shifted_index =
            plain_index =
            plain_letter =
            plain_text +=
        else:
            plain_text +=
    return plain_text


def encrypt_substitution(plain_text, substitution_string):
    if len(substitution_string) < len(alphabet):
        return "There are too few letters in the substitution table."
    if len(substitution_string) > len(alphabet):
        return "There are too many letters in the substitution table."

    cipher_text =
    for plain_letter in plain_text:
        if plain_letter in alphabet:
            plain_letter_index =
            cipher_letter =
            cipher_text +=
        else:
            cipher_text +=
    return cipher_text


def decrypt_substitution(cipher_text, substitution_string):
    if len(substitution_string) < len(alphabet):
        return "There are too few letters in the substitution string."
    if len(substitution_string) > len(alphabet):
        return "There are too many letters in the substitution string."

    plain_text =
    for cipher_letter in cipher_text:
        if cipher_letter in substitution_string:
            cipher_letter_index =
            plain_letter =
            plain_text +=
        else:
            plain_text +=
    return plain_text
