def playfair_encrypt(plaintext, key):
    print("Playfair cipher")
    plaintext = plaintext.upper().replace("J", "I")
    plaintext_processed = ""
    for char in plaintext:
        if char.isalpha():
            plaintext_processed += char
        elif char == ' ':
            plaintext_processed += ' '  # Keep spaces

    if len(plaintext_processed.replace(" ", "")) % 2 != 0:
        plaintext_processed = plaintext_processed.replace(" ", "")
        plaintext_processed += "X"

    ciphertext = ""
    i = 0
    while i < len(plaintext_processed):
        if plaintext_processed[i] == ' ':
            ciphertext += ' '
            i += 1
        else:
            if i + 1 < len(plaintext_processed) and plaintext_processed[i + 1] != ' ':
                pair = plaintext_processed[i:i + 2]
                ciphertext += pEncrypt(pair, key)
                i += 2
            else:
                pair = plaintext_processed[i] + 'X'  # Pad with X if last char and not space
                ciphertext += pEncrypt(pair, key)
                i += 1
    return ciphertext

def playfair_decrypt(ciphertext, key):
    print("Playfair decryption")
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == ' ':
            plaintext += ' '
            i += 1
        else:
            pair = ciphertext[i:i + 2]
            plaintext += pDecrypt(pair, key)
            i += 2

    # Remove trailing 'X' if added during encryption
    if len(plaintext.replace(" ", "")) % 2 != 0 and plaintext[-1] == 'X':
        plaintext = plaintext[:-1]

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

def pEncrypt(pair, key):
    matrix = create_playfair_matrix(key)
    char1 = pair[0]
    char2 = pair[1]

    row1, col1 = find_char_position(matrix, char1)
    row2, col2 = find_char_position(matrix, char2)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle
        return matrix[row1][col2] + matrix[row2][col1]

def pDecrypt(pair, key):
    matrix = create_playfair_matrix(key)
    char1 = pair[0]
    char2 = pair[1]

    row1, col1 = find_char_position(matrix, char1)
    row2, col2 = find_char_position(matrix, char2)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle
        return matrix[row1][col2] + matrix[row2][col1]