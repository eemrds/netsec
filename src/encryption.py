"""Encryption Assignment1."""


def key_to_length(plain_text: str, key: str, autokey: bool = False) -> str:
    """Makes the key the same lenght as the plain text by adding itself x times.

    ex:
        erierierierierierierierierierierierieri

    Args:
        plain_text (str): A plain text string.
        key (str): The encryption key determining how many positions the letter
            should be shifted.

    Returns:
        The encryption key.
    """
    key_to_length = ""
    # If autokey is used, add the plain text to the end of the key
    if autokey:
        key_to_length = f"{key}{plain_text}"
    else:
        # Add the key to itself until it is the same length as the plain text
        for _ in range(len(plain_text) // len(key) + 1):
            key_to_length += key
    # Remove the extra chars so that it is the same length as the plain text
    key_to_length = key_to_length[: len(plain_text)]
    return key_to_length


def generate_encryption_matrix() -> list[list[str]]:
    """Generates the encryption matrix.

       A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
      ------------------------------------------------------------------------------
    A |a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z|
    B |b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a|
    C |c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b|
    D |d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c|
    E |e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d|
    F |f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e|
    G |g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f|
    H |h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g|
    I |i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h|
    J |j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i|
    K |k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j|
    L |l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k|
    M |m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l|
    N |n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m|
    O |o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n|
    P |p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o|
    Q |q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p|
    R |r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q|
    S |s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r|
    T |t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s|
    U |u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t|
    V |v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u|
    W |w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v|
    X |x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w|
    Y |y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x|
    Z |z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y|
      ------------------------------------------------------------------------------

    Returns:
        The enctyption matrix.
    """
    encryption_matrix = []
    # Create a list of the alphabet
    characters = list("abcdefghijklmnopqrstuvwxyz")
    for _ in range(len(characters)):
        # For each letter in the alphabet add the list to the encryption matrix
        encryption_matrix.append(characters)

        # Remove the first char and add it back to the end of the list
        char = characters[0]
        characters = characters[1:]
        characters.append(char)
    return encryption_matrix


def vigenere_encrypt(
    plain_text: str,
    key: str,
    autokey: bool = False,
    row_col_transpose_key: int | None = None,
    row_col_transpose_first: bool = False,
) -> str:
    """Encrypts a string using the Vigenere cipher.

    Vigenère Cipher
    • One of the best known and simplest polyalphabetic substitution ciphers
    • Use a substitution matrix to together with the key and plaintext to encode
    • To encrypt a message, a key is needed
    • Key must be as long as the message
    • Usually, the key is a repeating keyword
    • Example from powerpoint:
        message: "we are discovered save yourself"
        key: deceptivedeceptivedeceptive
        plaintext: wearediscoveredsaveyourself
        ciphertext: ZICVTWQNGRZGVTWAVZHCQYGLMGJ
    • Autokey concatenates some of the plain text to the key itself.
        • This makes it harder to crack since no key value is repeating.
        • Still vulnerable to statistical analysis though :(

    Allows the use of row-column transposition before or after the encryption.

    Args:
        plain_text: A plain text string.
        key: The encryption key determining how many positions the letter
            should be shifted.
        autokey: bool to determine if should use autokey version or not.
        row_col_transpose_key: The key to use when transposing the text with
            row-column transposition.
        row_col_transpose_first: Whether to transpose the text with row-column
            transposition first or not.

    Returns:
        str: Encrypted string.
    """
    # If row-column transposition key is given and row-column transposition is
    # set to first, transpose the text
    if row_col_transpose_key and row_col_transpose_first:
        plain_text = row_col_transpose(plain_text, row_col_transpose_key)
    # Make the key the same length as the plain text
    key = key_to_length(plain_text, key, autokey=autokey).lower()
    # Get the encryption matrix
    encryption_matrix = generate_encryption_matrix()

    encrypted_string = ""
    # For each char in the plain text
    for i, char in enumerate(plain_text):
        # Find the index for the column for the plain text char
        col = ord(char) - 97
        # Find the index for the row for the key char
        row = ord(key[i]) - 97
        # Add the char from the encryption matrix to the encrypted string
        encrypted_string += encryption_matrix[col][row]

    # If the row-column transposition key is given then row-column transposition
    # the encrypted string
    if row_col_transpose_key and not row_col_transpose_first:
        encrypted_string = row_col_transpose(
            encrypted_string, row_col_transpose_key
        )
    return encrypted_string


def text_to_rectangle(text: str, key: int) -> list[list[str]]:
    """Transposes a text into a rectangle.

    Args:
        text: The text to transpose.
        key: The key to transpose the text with.

    Returns:
        list[list[str]]: The transposed text.
    """
    length = len(str(key))
    rectagled_text = []
    # Get the amount of rows needed for the rectangle based on the length of the
    # plain text
    for _ in range(len(text) // length + 1):
        # If the last row isn't filled up, fill it up with x's
        if len(text) < length and text:
            text_slice = list(f"{text:{'x'}<{length}}")
            if text_slice:
                rectagled_text.append(text_slice)

        else:
            # Split the text into slices of the length of the key and add it as
            # a row to the rectangle
            text_slice = list(text[:length])
            text = text[length:]
            rectagled_text.append(text_slice)
    # Remove empty lists
    rectagled_text = [arr for arr in rectagled_text if arr]
    return rectagled_text


def row_col_transpose(text: str, key: int) -> str:
    """Transposes a text into a rectangle and then reads it column by column.

      3   1   4   2   5
    | w | e | a | r | e |
    | d | i | s | c | o |
    | v | e | r | e | d |
    | u | s | i | n | g |
    | c | h | a | p | g |
    | p | t | s | a | v |
    | e | y | o | u | r |
    | s | e | l | f | x |

    Args:
        text: The text to transpose.
        key: The key to transpose the text with.

    Returns:
        str: The transposed text.
    """
    row_column_cipher = ""
    key_list = [int(key) for key in list(str(key))]
    # Get the text in the form of a rectangle with the length of the key
    rectangle_text = text_to_rectangle(text, key)
    # Go through the rectangle column by column and add the chars to the cipher
    # text
    for i in range(1, len(key_list) + 1):
        index = key_list.index(i)
        for text_list in rectangle_text:
            row_column_cipher += text_list[index]
    return row_column_cipher
