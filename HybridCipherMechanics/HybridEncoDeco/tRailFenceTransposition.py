def rail_fence_encrypt(plaintext, k):
    print("rail_fence")
    x = plaintext.split(" ")
    for i in range(len(x)) :
        x[i] = rfEn(x[i], k)
    ciphertext = " ".join(x)
    return ciphertext

def rail_fence_decrypt(ciphertext, k):
    x = ciphertext.split(" ")
    for i in range(len(x)) :
        x[i] = rfDe(x[i], k)
    plaintext = " ".join(x)
    return plaintext

def rfEn(plaintext, key):
    rails = [""] * key
    rail_index = 0
    direction = 1  # 1 for down, -1 for up

    for char in plaintext:
        if char.isalpha() or char.isdigit():  # Only encrypt alphanumeric characters.
            rails[rail_index] += char
            rail_index += direction

            if rail_index == key:
                rail_index = key - 2
                direction = -1
            elif rail_index == -1:
                rail_index = 1
                direction = 1
        else:  # Preserve non-alphanumeric characters.
            rails[rail_index] += char

    ciphertext = "".join(rails)
    return ciphertext

def rfDe(ciphertext, key):
    rails = [""] * key
    rail_index = 0
    direction = 1
    rail_lengths = [0] * key  # store the length of each rail.

    for char in ciphertext:  # Find the length of each rail.
        if char.isalpha() or char.isdigit():
            rail_lengths[rail_index] += 1
            rail_index += direction
            if rail_index == key:
                rail_index = key - 2
                direction = -1
            elif rail_index == -1:
                rail_index = 1
                direction = 1
        else:
            rail_lengths[rail_index] += 1
            rail_index += direction
            if rail_index == key:
                rail_index = key - 2
                direction = -1
            elif rail_index == -1:
                rail_index = 1
                direction = 1

    start_indices = [0] * key
    for i in range(1, key):  # Find the starting position for each rail's characters.
        start_indices[i] = start_indices[i - 1] + rail_lengths[i - 1]

    rail_contents = [""] * key
    for i in range(key):
        rail_contents[i] = ciphertext[start_indices[i]:start_indices[i] + rail_lengths[i]]

    plaintext = ""
    rail_index = 0
    direction = 1
    rail_content_indices = [0] * key

    for original_char in ciphertext:
        if original_char.isalpha() or original_char.isdigit():
            plaintext += rail_contents[rail_index][rail_content_indices[rail_index]]
            rail_content_indices[rail_index] += 1
            rail_index += direction
            if rail_index == key:
                rail_index = key - 2
                direction = -1
            elif rail_index == -1:
                rail_index = 1
                direction = 1
        else:
            plaintext += original_char

    return plaintext
