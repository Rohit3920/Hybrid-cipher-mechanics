import time

from KeyGen.edKay import generate_keys
from HybridEncoDeco.sCeaserCipher import *
from HybridEncoDeco.sMonoalphabatic import *
from HybridEncoDeco.sPlayfairCipher import *
from HybridEncoDeco.sPolyalphabatic import *
from HybridEncoDeco.tRailFenceTransposition import *

# Encryption
def encryption(ch, plaintext, eKey) :
    et = monoalphabetic_encrypt(plaintext, eKey) if ch ==1 else ceaser_encrypt(plaintext, eKey) if ch == 2 else playfair_encrypt(plaintext, eKey) if ch == 3 else  rail_fence_encrypt(plaintext, eKey) if ch == 4 else  polyalphabetic_encrypt(plaintext, eKey) if ch == 5 else ceaser_encrypt(plaintext, eKey)
    return et


# decryption
def decryption(ch, ciphertext, dKey) :
    dt = monoalphabetic_decrypt(ciphertext, dKey) if ch ==1 else ceaser_decrypt(ciphertext, dKey) if ch == 2 else playfair_decrypt(ciphertext, dKey) if ch == 3 else  rail_fence_decrypt(ciphertext, dKey) if ch == 4 else polyalphabetic_decrypt(ciphertext, dKey) if ch == 5 else ceaser_decrypt(ciphertext, numeric_key)
    return dt

#Key managemenet
numeric_key, alphabetic_key = generate_keys()
key1 = int(numeric_key)
key2 = str(alphabetic_key)
print(key1)
print(key2)

def chooseED():
    today = time.localtime()
    mint = today.tm_min
    hr = today.tm_hour
    wday = today.tm_wday
    mday = today.tm_mday
    month = today.tm_mon
    yr = today.tm_year

    t_val = mint *(hr  + wday + mday + month + yr)
    mod_val = t_val % 100
    remain_val = int(t_val / 100)
    ch = (mod_val + remain_val) % 6
    return ch

#choose key for perticular cipher model
def chooseKey(ch) :
    if ch % 2 == 0 :
        key = key1
    else :
        key = key2
    return key


# try example for any
pText = "hybrid cipher mechanics"
encrypted_text = encryption(chooseED(), pText, chooseKey(chooseED()))
print(f"Encrypted: {encrypted_text}")

decrypted_text = decryption(chooseED(), encrypted_text, chooseKey(chooseED()))
print(f"decrypted: {decrypted_text}")
