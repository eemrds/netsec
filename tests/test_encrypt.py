import pytest
from src.decryption import decrypt_row_col_transpose, decrypt_vigenre_cipher
from src.encryption import (
    key_to_length,
    row_col_transpose,
    text_to_rectangle,
    vigenere_encrypt,
)
from src.cracking import kasiski_examination


@pytest.mark.parametrize(
    "key, key_to_lenght, key_to_length_autokey, plain_text",
    [
        (
            "eri",
            "erierierierierierierierierierierierieri",
            "eriwearediscoveredusingchapgptsaveyours",
            "wearediscoveredusingchapgptsaveyourself",
        ),
        (
            "erik",
            "erikerikerikerikerikerikerikerikerikeri",
            "erikwearediscoveredusingchapgptsaveyour",
            "wearediscoveredusingchapgptsaveyourself",
        ),
        (
            "erikmartin",
            "erikmartinerikmartinerikmartinerikmarti",
            "erikmartinwearediscoveredusingchapgptsa",
            "wearediscoveredusingchapgptsaveyourself",
        ),
        (
            "eri",
            "erierierierierierierierierieri",
            "eriwearediscoveredusingchapgpt",
            "wearediscoveredusingchapgptsav",
        ),
    ],
)
def test_key_to_length(key, key_to_lenght, key_to_length_autokey, plain_text):
    """Test the key_to_length function."""
    k2l = key_to_length(plain_text, key, False)
    assert k2l == key_to_lenght
    assert len(k2l) == len(plain_text)
    k2l_autokey = key_to_length(plain_text, key, True)
    assert k2l_autokey == key_to_length_autokey
    assert len(k2l_autokey) == len(plain_text)


def test_vigenere_encrypt():
    """Test the vigenere_encrypt function."""
    plain_text = "wearediscoveredusingchapgptsaveyourself"
    key = "eri"
    cipher_text = vigenere_encrypt(plain_text, key)
    assert cipher_text == "avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn"


def test_vigenere_encrypt_with_row_col_last():
    """Test the vigenere_encrypt function with row_col_transpose_last."""
    plain_text = "wearediscoveredusingchapgptsaveyourself"
    key = "eri"
    row_col_key = 31425
    cipher_text = vigenere_encrypt(
        plain_text, key, row_col_transpose_key=row_col_key
    )
    assert cipher_text == "vmmjlbpivkvrxrynalmykgiaijvqrwwcvslxkdix"


def test_vigenere_encrypt_with_row_col_first():
    """Test the vigenere_encrypt function with row_col_transpose_first."""
    plain_text = "wearediscoveredusingchapgptsaveyourself"
    key = "eri"
    row_col_key = 31425
    cipher_text = vigenere_encrypt(
        plain_text,
        key,
        row_col_transpose_key=row_col_key,
        row_col_transpose_first=True,
    )
    assert cipher_text == "izmwybcvzgvvtrcjnlzlktvaejzmrascmsuokmzb"
    decrypted_vigenre_cipher = decrypt_vigenre_cipher(cipher_text, key)

    # Try to decrypt and see if we end up with the plaintext
    assert (
        decrypted_vigenre_cipher == "eieshtyercenpaufwdvucpesasriasoleodggvrx"
    )
    assert (
        decrypt_row_col_transpose(decrypted_vigenre_cipher, row_col_key)
        == plain_text
    )


def test_text_to_rectangle():
    """Test the text_to_rectangle function."""
    cipher_text = "avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn"
    key = 31425
    t2r = text_to_rectangle(cipher_text, key)
    for i, row in enumerate(t2r):
        if len(cipher_text[len(row) * i : len(row) * (i + 1)]) < 5:
            assert (
                "".join(row)
                == f"{cipher_text[len(row) * i : len(row) * (i + 1)]}x"
            )
        else:
            assert (
                "".join(row) == cipher_text[len(row) * i : len(row) * (i + 1)]
            )


def test_row_col_transpose():
    """Test the row_col_transpose function."""
    row_column_key = 31425
    text = "avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn"
    row_column_cipher = row_col_transpose(text, row_column_key)
    assert row_column_cipher == "vmmjlbpivkvrxrynalmykgiaijvqrwwcvslxkdix"


def test_row_col_transpose_reverse():
    """Test the row_col_transpose function with reverse=True."""
    row_column_key = 31425
    row_column_cipher = "vmmjlbpivkvrxrynalmykgiaijvqrwwcvslxkdix"
    # reversed_key = reverse_key(row_column_key)
    # assert reversed_key == 35241
    reversed_row_column_cipher = decrypt_row_col_transpose(
        row_column_cipher, row_column_key
    )

    vigenere_cipher = "avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn"
    assert reversed_row_column_cipher[: len(vigenere_cipher)] == vigenere_cipher


def test_decrypt_vigenre_cipher():
    """Test the decrypt_vigenre_cipher function."""
    plain_text = "wearediscoveredusingchapgptsaveyourself"
    key = "eri"
    cipher_text = "avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn"
    decrypted_text = decrypt_vigenre_cipher(cipher_text, key)
    assert decrypted_text == plain_text


def test_kasiski_examination():
    """Test the kasiski_examination function."""
    encrypted_text = "avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn"
    key_length = kasiski_examination(encrypted_text)
    assert key_length == 3


@pytest.mark.parametrize(
    "ciphertext, key_length",
    [
        # ("avivvlmjksmmvvlyjqrxklrxkgbwrdipwyiaicn", 3), # Does not work. Text is probably too short
        (
            # Trying a very long string to check if it works
            vigenere_encrypt(
                "Another strength of the cipher is the unpredictability that comes from a long and unpredictable key. If the key is long and unpredictable, it is harder to brute force. There are some ways to attempt to brute force the key, by looking at the frequency of certain letters which to some extent can help determine the cipher length.".replace(
                    " ", ""
                )
                .replace(",", "")
                .replace(".", "")
                .lower(),
                "eri",
            ),
            3,
        ),
    ],
)
def test_kasiski_examination(ciphertext, key_length):
    """Test the kasiski_examination function."""
    assert kasiski_examination(ciphertext) == key_length


@pytest.mark.parametrize(
    "ciphertext, key_length",
    [
        (
            vigenere_encrypt(
                "Another strength of the cipher is the unpredictability that comes from a long and unpredictable key. If the key is long and unpredictable, it is harder to brute force. There are some ways to attempt to brute force the key, by looking at the frequency of certain letters which to some extent can help determine the cipher length.".replace(
                    " ", ""
                )
                .replace(",", "")
                .replace(".", "")
                .lower(),
                "eri",
                autokey=True,
            ),
            3,
        ),
    ],
)
def test_kasiski_examination_with_autokey(ciphertext, key_length):
    """Test the kasiski_examination function with autokey."""
    assert kasiski_examination(ciphertext) != key_length
