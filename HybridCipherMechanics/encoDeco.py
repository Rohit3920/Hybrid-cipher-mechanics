import time
from pymongo import MongoClient
from flask import jsonify

from KeyGen.edKay import generate_keys
from HybridEncoDeco.sCeaserCipher import *
from HybridEncoDeco.sMonoalphabatic import *
from HybridEncoDeco.sPlayfairCipher import *
from HybridEncoDeco.sPolyalphabatic import *
from HybridEncoDeco.tRailFenceTransposition import *

# Connect to MongoDB (Assuming MongoDB is running locally)
client = MongoClient('mongodb://localhost:27017/')
db = client['chat-app']
messages_collection = db['messages']

def mTime(txt):
    messages = messages_collection.find().sort('timestamp', 1)
    for msg in messages :
        if msg['message'] == txt :
            return msg['time']

# Encryption
def encryption(plaintext) :
    plaintext = str(plaintext)
    ch = chooseED(setTime())
    eKey, numeric_key = chooseKey(ch, setTime())
    et = monoalphabetic_encrypt(plaintext, eKey) if ch ==1 else ceaser_encrypt(plaintext, eKey) if ch == 2 else playfair_encrypt(plaintext, eKey) if ch == 3 else  rail_fence_encrypt(plaintext, eKey) if ch == 4 else  polyalphabetic_encrypt(plaintext, eKey) if ch == 5 else ceaser_encrypt(plaintext, numeric_key)
    print("Encryption  > " + et)
    decryption(et)
    return et


# decryption
def decryption(ciphertext) :
    # msgTime = mTime(ciphertext)
    # ciphertext = str(ciphertext)
    ch = chooseED(setTime())
    dKey, numeric_key = chooseKey(ch, setTime())
    dt = monoalphabetic_decrypt(ciphertext, dKey) if ch ==1 else ceaser_decrypt(ciphertext, dKey) if ch == 2 else playfair_decrypt(ciphertext, dKey) if ch == 3 else  rail_fence_decrypt(ciphertext, dKey) if ch == 4 else polyalphabetic_decrypt(ciphertext, dKey) if ch == 5 else ceaser_decrypt(ciphertext, numeric_key)
    print("Decryption > " + dt)
    return dt

#set time for send massege


def setTime():
    today = time.localtime()
    yr = today.tm_year
    month = today.tm_mon
    mday = today.tm_mday
    hr = today.tm_hour
    mint = today.tm_min
    sec = today.tm_sec
    wday = today.tm_wday
    yday = today.tm_yday
    t = [yr, month, mday, hr, mint, sec, wday, yday]
    return t
setTime()

def chooseED(t):
    yr, month, mday, hr, mint, sec, wday, yday = t

    if mint == 0:
        mint = mint + 1

    t_val = (mint+60) + (hr  + wday + mday + month + yr + yday)
    mod_val = t_val % 100
    remain_val = int(t_val / 100)
    ch = (mod_val + remain_val) % 6
    return ch

#choose key for perticular cipher model
def chooseKey(ch, msgTime) :
    numeric_key, alphabetic_key = generate_keys(msgTime)
    key1 = int(numeric_key)
    key2 = str(alphabetic_key)
    print(key1)
    print(key2)

    if ch % 2 == 0 :
        key = key1
    else :
        key = key2
    return key, numeric_key

# try example for any
pText = "hybrid cipher mechanics"

