import time
import string

def generate_keys():
    today = time.localtime()
    mint = today.tm_min
    hr = today.tm_hour
    wday = today.tm_wday
    mday = today.tm_mday
    month = today.tm_mon
    yr = today.tm_year

    t_val = mint *(hr  + wday + mday + month + yr)
    print(t_val)
    mod_val = t_val % 100
    remain_val = int(t_val / 100)
    numeric_key = (mod_val + remain_val) % 100

    alphabet = list(string.ascii_lowercase)

    lett = numeric_key % (len(alphabet)*2)
    arrNum = [yr, month, mday, wday, hr, mint]

    alphabetic_key = ""
    for i in range (len(arrNum)) :
        alVal = (lett * arrNum[i]) % len(alphabet)
        alphabetic_key = alphabetic_key + alphabet[alVal]

    return numeric_key, alphabetic_key

if __name__ == "__main__":
    numeric_key, alphabetic_key = generate_keys()
    # print("Numeric Key:", numeric_key)
    # print("Alphabetic Key:", alphabetic_key)