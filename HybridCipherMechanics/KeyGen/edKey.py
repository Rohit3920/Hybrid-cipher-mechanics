import string

def generate_keys(time):
    yr, month, mday, hr, mint, sec, wday, yday = time
    if mint == 0:
        mint = mint + 1
    t_val = mint *(hr  + wday + mday + month + yr + yday)
    mod_val = t_val % 100
    remain_val = int(t_val / 100)
    numeric_key = (mod_val * remain_val) % 10000

    alphabet = list(string.ascii_lowercase)

    lett = numeric_key % (len(alphabet)*2)
    arrNum = [yr, month, mday, wday, hr, mint]

    alphabetic_key = ""
    for i in range (len(arrNum)) :
        alVal = (lett * arrNum[i]) % len(alphabet)
        alphabetic_key = alphabetic_key + alphabet[alVal]
        if alphabetic_key == "aaaaaa" :
            alphabetic_key = "hcmmod"

    return numeric_key, alphabetic_key

if __name__ == "__main__":
    numeric_key, alphabetic_key = generate_keys()
    # print("Numeric Key:", numeric_key)
    # print("Alphabetic Key:", alphabetic_key)