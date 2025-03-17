def ceaser_encrypt(plaintext, key):
    k1 = key
    print("Ceaser cipher")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + k1) % 26 + start)
        else:
            shifted_char = char
        ciphertext += shifted_char
    return ciphertext

def ceaser_decrypt(ciphertext, key):
    return ceaser_encrypt(ciphertext, -key) #Decryption is just encryption with the negative key









