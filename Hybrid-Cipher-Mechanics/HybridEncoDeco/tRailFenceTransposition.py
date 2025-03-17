def rail_fence_encrypt(plaintext, k):
    print("rail_fence encryption")
    key = k % 10
    if key == 0 or key == 1:
        key = key + 2
    return rfEn(plaintext, key)

def rail_fence_decrypt(ciphertext, k):
    print("rail_fence decryption")
    key = k % 10
    if key == 0 or key == 1:
        key = key + 2
    return rfDe(ciphertext, key)

def rfEn(plaintext, key):
    rails = [""] * key
    rail_index = 0
    direction = 1  # 1 for down, -1 for up

    for char in plaintext:
        rails[rail_index] += char
        rail_index += direction

        if rail_index == key:
            rail_index = key - 2
            direction = -1
        elif rail_index == -1:
            rail_index = 1
            direction = 1

    ciphertext = "".join(rails)
    return ciphertext

def rfDe(ciphertext, key):
    rails = [""] * key
    rail_index = 0
    direction = 1
    rail_lengths = [0] * key  # store the length of each rail.

    for char in ciphertext:  # Find the length of each rail.
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

    for i in range(len(ciphertext)):
        plaintext += rail_contents[rail_index][rail_content_indices[rail_index]]
        rail_content_indices[rail_index] += 1
        rail_index += direction
        if rail_index == key:
            rail_index = key - 2
            direction = -1
        elif rail_index == -1:
            rail_index = 1
            direction = 1

    return plaintext
