# Python Coding and Decoding

This Python script encodes and decodes sentences with a simple, reversible word transformation.

## Features

- Encodes words with three or more characters by moving the first character to the end and adding fixed markers.
- Reverses words shorter than three characters.
- Decodes text by removing the markers and restoring the original character order.
- Uses only Python’s standard library.

## Requirements

- Python 3
- No third-party packages

## Run the script

Open a terminal in the project folder and run:

```bash
python ex-4code.py
Enter a sentence when prompted. Enter 0 to encode it or 1 to decode it.
Example
For the sentence hello world, choose 0 to encode:
hkfellohwgc hkfordlwwgc
Choose 1 and enter the encoded text to decode it:
hello world
The script currently prints True or False before the result to show the selected mode.
How it works
For words with three or more characters, the script moves the first character to the end, then adds hkf at the beginning and wgc at the end. For shorter words, it reverses the characters.

When decoding, the script removes the markers and moves the final character back to the beginning. It reverses shorter words again.
Note
This transformation demonstrates basic string manipulation. It does not provide secure encryption: the markers and rules are fixed and easy to discover.

To polish the project, fix the `santence` prompt typo, remove `print(what)` if you don’t want the extra `True`/`False` line, and validate that the user enters only `0` or `1`.

  
8:35 PM
