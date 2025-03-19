def playfair_encrypt(plaintext, k):
    print("Play fair cipher")
    x = plaintext.split(" ")
    for i in range(len(x)) :
        x[i] = pEncrypt(x[i], k)
    ciphertext = " ".join(x)
    return ciphertext

def playfair_decrypt(ciphertext, k):
    x = ciphertext.split(" ")
    for i in range(len(x)) :
        x[i] = pDecrypt(x[i], k)
    plaintext = " ".join(x)
    return plaintext

def create_playfair_matrix(key):
    """Creates a 5x5 Playfair cipher matrix from a key."""
    key = key.upper().replace("J", "I")  # Replace J with I
    matrix = []
    seen = set()

    for char in key:
        if char.isalpha() and char not in seen:
            matrix.append(char)
            seen.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_char_position(matrix, char):
    """Finds the row and column of a character in the Playfair matrix."""
    for row_index, row in enumerate(matrix):
        if char in row:
            return row_index, row.index(char)
    return None

def pEncrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join(filter(str.isalpha, plaintext))  # Remove non-alpha chars
    if len(plaintext) % 2 != 0:
        plaintext += "X"  # Pad with X if odd length

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def pDecrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext.lower()