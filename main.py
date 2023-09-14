"""Main file for Assignment 1."""

from src.encryption import key_to_length, vigenere_encrypt, row_col_transpose
from src.decryption import decrypt_row_col_transpose, decrypt_vigenre_cipher

KEY_WIDTH = 15
VALUE_WIDTH = 40
HEADING_WIDTH = KEY_WIDTH + VALUE_WIDTH + 3
END = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"


def color_result(key: str, value: str | None = None) -> str:
    """Color the result string."""

    if value:
        return f"{BLUE}{key: <{KEY_WIDTH}} | {value: <{VALUE_WIDTH}}{END}"
    else:
        return f"{GREEN}{key: <{HEADING_WIDTH}}{END}"


if __name__ == "__main__":
    PLAIN_TEXT = "wearediscoveredusingchapgptsaveyourself"
    VIGENERE_KEY = "eri"
    ROW_COLUMN_KEY = 31425

    ###################
    ##### Encrypt #####
    ###################
    # Part 1
    print(
        f"""
    {"1. ENCRYPTING": ^{VALUE_WIDTH+KEY_WIDTH}}
    +----------------------------------------------------------+
    |{color_result("Plain text to Vigenere cipher:")}|
    +----------------------------------------------------------+
    """
    )

    # Encrypt the plain text using the vigenere ciphering method
    vigenere_encrypted = vigenere_encrypt(PLAIN_TEXT, VIGENERE_KEY)
    print(f"PLAIN TEXT: {PLAIN_TEXT}")
    print(f"VIGENERE KEY: {VIGENERE_KEY}")
    print(f"VIGENERE ENCRYPTED: {vigenere_encrypted}")

    # Part 3
    print(
        f"""
    +----------------------------------------------------------+
    |{color_result("Vigenere to row-column cipher text:")}|
    +----------------------------------------------------------+
    """
    )
    # Encrypt the vigenere cipher text using the row-column transposition method
    row_col_cipher = row_col_transpose(vigenere_encrypted, ROW_COLUMN_KEY)
    print(f"VIGENERE ENCRYPTED: {vigenere_encrypted}")
    print(f"ROW-COLUMN KEY: {ROW_COLUMN_KEY}")
    print(f"ROW-COLUMN ENCRYPTED: {row_col_cipher}")

    ###################
    ##### Decrypt #####
    ###################
    # Step 1: Revere the row column transpose
    print(
        f"""
    {"2. DECRYPTING": ^{VALUE_WIDTH+KEY_WIDTH}}
    +----------------------------------------------------------+
    |{color_result("Row column cipher to vigenere cipher:")}|
    +----------------------------------------------------------+
    """
    )

    vigenere_encrypted = decrypt_row_col_transpose(
        row_col_cipher, ROW_COLUMN_KEY
    )
    print(f"ROW-COLUMN ENCRYPTED: {row_col_cipher}")
    print(f"ROW-COLUMN KEY: {ROW_COLUMN_KEY}")
    print(f"VIGENERE ENCRYPTED: {vigenere_encrypted}")

    # Step 2: Reverse the vigenere cipher
    print(
        f"""
    +----------------------------------------------------------+
    |{color_result("Vigenere cipher to plain text")}|
    +----------------------------------------------------------+
    """
    )

    plain_text = decrypt_vigenre_cipher(vigenere_encrypted, VIGENERE_KEY)
    print(f"VIGENERE ENCRYPTED: {vigenere_encrypted}")
    print(f"VIGENERE KEY: {VIGENERE_KEY}")
    print(f"PLAIN TEXT: {plain_text}")

    ###################
    ##### Reverse #####
    ###################

    # Part 1
    print(
        f"""
    {"3. REVERSING": ^{VALUE_WIDTH+KEY_WIDTH}}

    +----------------------------------------------------------+
    |{color_result("Plain text to row-column cipher text:")}|
    +----------------------------------------------------------+
    """
    )

    row_col_cipher = row_col_transpose(PLAIN_TEXT, ROW_COLUMN_KEY)
    print(f"PLAIN TEXT: {PLAIN_TEXT}")
    print(f"ROW-COLUMN KEY: {ROW_COLUMN_KEY}")
    print(f"ROW-COLUMN ENCRYPTED: {row_col_cipher}")

    # Part 3
    print(
        f"""
    +----------------------------------------------------------+
    |{color_result("Row-column cipher to vigenere cipher:")}|
    +----------------------------------------------------------+
    """
    )
    vigenere_encrypted = vigenere_encrypt(row_col_cipher, VIGENERE_KEY)
    print(f"ROW-COLUMN ENCRYPTED: {row_col_cipher}")
    print(f"VIGENERE KEY: {VIGENERE_KEY}")
    print(f"VIGENERE ENCRYPTED: {vigenere_encrypted}")

    # Part 5
    print(
        f"""
    +----------------------------------------------------------+
    |{color_result("Vigenere cipher to row-column cipher text:")}|
    +----------------------------------------------------------+
    """
    )

    vigenere_encrypted = decrypt_vigenre_cipher(
        vigenere_encrypted, VIGENERE_KEY
    )
    print(f"VIGENERE ENCRYPTED: {vigenere_encrypted}")
    print(f"VIGENERE KEY: {VIGENERE_KEY}")
    print(f"ROW-COLUMN ENCRYPTED: {row_col_cipher}")

    print(
        f"""
    +----------------------------------------------------------+
    |{color_result("Row-column cipher to plain text:")}|
    +----------------------------------------------------------+
    """
    )

    plain_text = decrypt_row_col_transpose(vigenere_encrypted, ROW_COLUMN_KEY)
    print(f"ROW-COLUMN ENCRYPTED: {row_col_cipher}")
    print(f"ROW-COLUMN KEY: {ROW_COLUMN_KEY}")
    print(f"PLAIN TEXT: {plain_text}")
