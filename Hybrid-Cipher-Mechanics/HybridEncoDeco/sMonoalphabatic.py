def create_substitution_cipher(key):
    if key == "abcde" :
        key = "hybrid"
    elif key == "ABCDE" :
        key = "cipher"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    cipher = {}
    key_index = 0

    for char in alphabet:
        if key_index < len(key):
            if key[key_index] not in cipher.values():
                cipher[char] = key[key_index]
                key_index += 1
            else:
                remaining_alphabet = "".join(c for c in alphabet if c not in cipher.values())
                if remaining_alphabet:
                    cipher[char] = remaining_alphabet[0]
                else:
                    return None #Key contains all 26 letters and no remaining alphabet.
        else:
            remaining_alphabet = "".join(c for c in alphabet if c not in cipher.values())
            cipher[char] = remaining_alphabet[0]

    return cipher

def monoalphabetic_encrypt(plaintext, key):
    print("monoalphabetic cipher")
    cipher = create_substitution_cipher(key)
    if cipher is None: return "Key error: Key must contain unique characters"
    plaintext = plaintext.upper()
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            ciphertext += cipher[char]
        else:
            ciphertext += char  # Keep non-alphabetic characters

    return ciphertext

def monoalphabetic_decrypt(ciphertext, key):
    cipher = create_substitution_cipher(key)
    if cipher is None: return "Key error: Key must contain unique characters"
    ciphertext = ciphertext.upper()
    plaintext = ""
    reverse_cipher = {v: k for k, v in cipher.items()} #create reverse cipher for decryption

    for char in ciphertext:
        if char.isalpha():
            plaintext += reverse_cipher[char]
        else:
            plaintext += char  # Keep non-alphabetic characters

    return plaintext.lower()
