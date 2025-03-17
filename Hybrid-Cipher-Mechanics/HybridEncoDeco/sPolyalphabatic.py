def polyalphabetic_encrypt(plaintext, key):
    print("polyalphabetic cipher")
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += shifted_char
            key_index += 1
        else:
            ciphertext += char  # Keep non-alphabetic characters

    return ciphertext

def polyalphabetic_decrypt(ciphertext, key):
    """Decrypts ciphertext using a polyalphabetic cipher (Vigenère cipher)."""
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            shifted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A')) #Adding 26 to handle negative modulus.
            plaintext += shifted_char
            key_index += 1
        else:
            plaintext += char  # Keep non-alphabetic characters

    return plaintext.lower()