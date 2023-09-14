# DAT 510: Assignment 1

## Abstract

## 1. Introduction

The project is divided into four parts. The first part is to implement two different functions for encrypting a message. A Vigenère cipher and a row-column transposition cipher, as well as assessing the security of the cipher methods. The second part is to implement a function for decrypting the messages produced by the different ciphers. The third part is encrypting the plain text again using the two different ciphers, but in a reverse order. The fourth and last part is to assess which combination of the two ciphers provide the most secure message.

The Vigenère cipher, a symmetrical ciphering method *"is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key."* [[1]](#1)  The main idea is to generate a cipher text by shifting a letter specific number of places in the alphabet. This is done for each letter of the plain text message. To choose the cipher letter you use a *Vigenère square*. The Vigenère square is a alphabetic tablet with the length and height of the alphabet. Each row contains all the letters of the alphabet, but in each row the previous first letter is added to the end of the current row and the second is shifted up.

![Vigenère square example](images/vigenere-table.png)
> The Vigenère square. Used to encrypt and decrypt messages using the Vigenère cipher.
> The letter of the message is found in the top row. The letter in the same position on the key is used to find the row. The cipher letter is the letter in the intersection between the row and column.

The row-column transposition "*is a method of encryption which scrambles the positions of characters (transposition) without changing the characters themselves.*"[[2]](#2) The main point of encrypting a message using row-column transposition is by arranging them in a square like object. The message is inserted, one by one, into the square and. When the row is full you move on to the next row. *It is also possible to change from inserting into rows to inserting into columns.* The key has to be the same length as the row or column, depending on the version you use and be of rearranged incrementing numbers. The letters are then encrypted by choosing the column corresponding to the key letter 1 and making the column the first part of the text, then going to column corresponding to the key letter 2 and so on.

![Row-column transposiontion example with a key](images/row-col-example.png)
> Row-column transposition example with a key.
> The key is 3, 1, 4, 2. The message is inserted into the square row by row. The first part of the cipher would be `eieshtye` aka. column number 2.

## 2. Design and Implementation

### 2.1. Part I

The message should first be encrypted using a Vigenère cipher and the encrypted message should then again be encrypted using row-column transposition.

### 2.2. Part II

### 2.3. Part III

### 2.4. Part IV

## 3. Test Results

## 4. Discussion

## 5. Conclusion

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

## References

<a id="1">[1]</a>
Vigenère cipher. (2023, August 11). In *Wikipedia*. https://en.wikipedia.org/w/index.php?title=Vigen%C3%A8re_cipher&oldid=1169803142   
<a id="2">[2]</a>
Row-column transposition. (2023, June 27). In *Wikipedia*. https://en.wikipedia.org/w/index.php?title=Transposition_cipher&oldid=1162245447