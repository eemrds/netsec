# Assignment 1

Author: **Erik Martin**
Studentnr: **250660**
University: **University of Stavanger**

Code should have a proper README file that describes the contents of the directory and any special instructions needed to run your programs (i.e. if it requires packages, commands to install the package. describe any command line arguments with the required parameters).

## Layout

`src/` - contains all the modules for the assignment. It is split into three files:

* cracking.py - contains the code for the Vigenere cipher cracking using the Kasiski examination method
* encryption.py - contains the code for the Vigenere cipher and row-column transposition cipher encryption
* decryption.py - contains the code for the Vigenere cipher and row-column transposition cipher decryption

`test/` - contains all the pytest unit tests for the assignment.

`main.py` - contains the main program for the assignment using the specific plain texts and keys provided in the assignment. This is the program that should be run to see the results of the assignment.

## Running the program

### Requirements

Using basic Python packages except for `pytest`` which is used for unit testing.

Other packages used are `re` and `math` which should be included in the standard Python library.

To run the assignment:

```bash
python3 main.py
```

To run the tests:

```bash
pytest -svv test/
```
