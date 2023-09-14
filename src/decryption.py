"Part 2 Assignment 1."

from src.encryption import generate_encryption_matrix, key_to_length


def get_max(key_list: list) -> int:
    """Gets the max value in a list that contains None.

    Args:
        key_list: The list to get the max value from.

    Returns:
        int: The max value in the list.
    """
    max_val = 0
    for key in key_list:
        if key is not None:
            if key > max_val:
                max_val = key
    return max_val


def get_min(key_list: list) -> int:
    """Gets the min value in a list that contains None.

    Args:
        key_list: The list to get the min value from.

    Returns:
        int: The min value in the list.
    """
    min_val = 100
    for key in key_list:
        if key is not None:
            if key < min_val:
                min_val = key
    return min_val


# NOT USED
# def reverse_key(key: int) -> int:
#     """Reverses the key.

#     Args:
#         key: The key to reverse.

#     Returns:
#         int: The reversed key.
#     """
#     list_key = [int(key) for key in list(str(key))]
#     reverse_key = [None] * len(list_key)
#     for _ in range(len(list_key)):
#         list_none_values = [key for key in list_key if key is not None]
#         if (len(list_none_values)) == 0:
#             break
#         if (len(list_none_values)) == 1:
#             remaining = list_none_values
#             remaining_index = reverse_key.index(None)
#             reverse_key[remaining_index] = remaining[0]
#             list_key = [None for _ in range(len(list_key))]
#         else:
#             max_val_in_key = get_max(list_key)
#             min_val_in_key = get_min(list_key)
#             max_index = list_key.index(max_val_in_key)
#             min_index = list_key.index(min_val_in_key)
#             reverse_key[min_index] = max_val_in_key
#             reverse_key[max_index] = min_val_in_key
#             list_key[max_index] = None
#             list_key[min_index] = None
#     return int("".join([str(key) for key in reverse_key]))


def decrypt_row_col_transpose(ciphertext: str, key: int) -> str:
    """decryptes the row column transpose.

    Args:
        ciphertext: The ciphertext to decrypt.
        key: The key used to encrypt the text with.

    Returns:
        str: The decryptne ciphertext.
    """
    ciphertext_list = []
    key_length = len(str(key))

    # Create the matrix were the length of the rows is the length of the key
    # | None | None | None | None | None | ...
    # | None | None | None | None | None | ...
    # | None | None | None | None | None | ...
    # | None | None | None | None | None | ...
    # ...
    column_matrix = [
        [None for _ in range(key_length)]
        for _ in range(len(ciphertext) // key_length)
    ]
    # Split the ciphertext into a list of strings with the length of the key
    for i in range(key_length):
        ciphertext_list.append(
            ciphertext[len(column_matrix) * i : len(column_matrix) * (i + 1)]
        )

    # Get the index of the key
    list_index = [int(string) for string in list(str(key))]

    # Fill the column matrix with the ciphertext based on the index of the key
    # (basically doing the reverse of the row column transpose and filling them back going column by column)
    for row in ciphertext_list:
        index = list_index.index(get_min(list_index))
        for i, matrix_row in enumerate(column_matrix):
            matrix_row[index] = row[i]
        list_index[index] = None

    # Finally go through the column matrix and add the chars to the decrypted
    # text
    decrypted_text = ""
    for row in column_matrix:
        decrypted_text += "".join(row)
    return decrypted_text.rstrip("x")


def decrypt_vigenre_cipher(
    cipher_text: str, key: str, autokey: bool = False
) -> str:
    """decryptes the vigenre cipher.

    Args:
        cipher_text: The cipher text to decrypt.
        key: The key used to encrypt the text with.
        autokey: Whether autokey was used to encrypt or not.

    Returns:
        str: The decryptne cipher text.
    """
    decrypted_string = ""
    # Make the key into the specified length
    key = key if autokey else key_to_length(cipher_text, key)
    # Get the encryption matrix
    encryption_matrix = generate_encryption_matrix()

    # Find the row and column of the cipher text in the encryption matrix based
    # on the key and plain text
    for i, char in enumerate(cipher_text):
        row = ord(str(key)[i]) - 97
        col = encryption_matrix[row].index(char)
        decrypted_string += encryption_matrix[0][col]
        # If autokey is used, add the decrypted char to the key
        if autokey:
            key += encryption_matrix[0][col]
    return decrypted_string
