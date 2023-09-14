"""Function for cracking the vigenere cipher."""

import re
import math


def kasiski_examination(
    ciphertext: str,
    minimum_sequence_length: int = 3,
    maximum_sequence_length: int = 7,
) -> int:
    """Kasinski examination for vigenere cipher text to guess length of the key.

    Step 1:
        Find all the repeating sequences in the text for different sequence
            lengths.
    Step 2:
        Find the number of letters or distance between the repeating sequences.
    Step 3:
        Find the Factor of this distance. If the number is repeated, it is
        likely to be the key length.

    Args:
        ciphertext: The ciphertext to examine.
        minimum_sequence_length: The minimum length of the sequence to look for.
        maximum_sequence_length: The maximum length of the sequence to look for.

    Returns:
        int: The key length.
    """

    repeats = {}
    # Get all the repeats sequences of the text starting from the minimum up to
    # the maximum sequence length
    for length in range(minimum_sequence_length, maximum_sequence_length + 1):
        for i in range(0, len(ciphertext) - length):
            # Get a sequence of the length
            seq = ciphertext[i : i + length]
            # Remove everything before the sequence
            temp_cipher = ciphertext[i + length :]
            if seq in temp_cipher:
                if not repeats.get(seq, None):
                    # Get all the start positions of the sequence from the
                    # ciphertext
                    repeats[seq] = [
                        m.start() for m in re.finditer(seq, ciphertext)
                    ]

    if not repeats:
        return 0
    # Find the distances between the repeating sequences
    distances = []
    for startposition in repeats.values():
        # Get the distances between the repeating sequences for each sequence
        distances.extend(
            [
                # Get the distance between the current index and the next index
                startposition[i + 1] - startposition[i]
                for i in range(len(startposition) - 1)
            ]
        )
    # Find the greatest common divisor of the distances (signalizing the key
    # length)
    gcd_value = distances[0]
    for distance in distances[1:]:
        gcd_value = math.gcd(gcd_value, distance)
    return gcd_value
