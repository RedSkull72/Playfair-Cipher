# Playfair Cipher in Python

A clean Python implementation of the classic **Playfair Cipher** encryption and decryption algorithm. 

This repository contains a script that generates a dynamic 5x5 key matrix based on a user-provided keyword, processes plain text into valid digrams, encrypts it, and decrypts the resulting ciphertext back to its original form.

---

## 📌 How the Playfair Cipher Works

The Playfair cipher encrypts pairs of letters (digrams) rather than single letters, making it significantly harder to break using simple frequency analysis.

### Rules & Logic:

1. **5x5 Key Square (Alphabet Matrix):**
   * The grid consists of 25 letters.
   * Because the English alphabet contains 26 letters, `'J'` is merged into `'I'` (i.e., every `'J'` is treated as `'I'`).

2. **Key Matrix Construction:**
   * Duplicate letters are removed from the user's secret keyword.
   * The unique key letters are placed into the 5x5 grid first.
   * The remaining empty spaces are filled with the rest of the alphabet in standard order.

3. **Text Formatting (Digram Split):**
   * Non-alphabetic characters and spaces are removed.
   * The text is split into pairs of two letters.
   * If a pair contains duplicate letters (e.g., `"HELLO"` $\rightarrow$ `"HE" "LL" "O"`), a filler letter `'X'` is inserted between them (`"LX L..."`).
   * If the final text has an odd number of letters, a trailing `'X'` is appended to complete the last pair.

4. **Encryption Rules:**
   * **Same Row:** Replace each letter with the letter to its immediate right (wrapping around to the left if at the end).
   * **Same Column:** Replace each letter with the letter directly below it (wrapping around to the top if at the bottom).
   * **Rectangle (Different Row & Column):** Replace each letter with the letter in its own row, but in the column of the second letter.

5. **Decryption Rules:**
   * Reverses the encryption steps (shift left for rows, shift up for columns, and rectangle swap).

---

## ✨ Features

* **Dynamic 5x5 Key Matrix:** Automatically builds a custom alphabet grid from any keyword.
* **Text Preprocessing:** Automatically strips non-alphabetic characters and replaces `'J'` with `'I'`.
* **Automated Digram Formatting:** Handles repeating letters and odd-length strings by inserting padding `'X'` characters.
* **Full Cycle Support:** Demonstrates both encryption and decryption in a single workflow.

---

## 🚀 Getting Started

### Prerequisites

* [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Running the Script

Run the main script using your terminal or IDE:

```bash
python main.py
```

### Sample Output

```text
Enter a keyword for encryption: MONARCHY
Enter a plain text to encrypt: INSTRUMENTS

# Encrypted Ciphertext
GATLMZCLRQTX

# Decrypted Plaintext
INSTRUMENTSX
```

---

## 📂 Code Breakdown

* **Key Matrix Setup (`lofK` & `square`):** Filters out duplicate letters from the key and fills the remaining slots with unused alphabet characters.
* **Digram Split Loop:** Iterates through the sanitized plaintext string, inserting `'X'` padding where duplicate letters occur consecutively or at the string boundary.
* **Encryption Loop:** Calculates 2D matrix indices (`row = idx // 5`, `col = idx % 5`) and applies Playfair rules to produce `cT` (Ciphertext).
* **Decryption Loop:** Performs the inverse modular shifts on `cT` to recover `dT` (Decrypted text).

---

## 📝 Notes & Potential Improvements

* **Filler Removal:** The code attempts to clean up padding using `.replace("X", "")`. Note that this will also remove any legitimate `'X'` characters present in the original message.