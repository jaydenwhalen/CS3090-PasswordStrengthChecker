# CS3090-PasswordStrengthChecker
This program accepts a password that a user inputs and asseses its strength. Factors that contribute to a password's strength in this algorithm include length and use of lowercase letters, uppercase letters, digits, and symbols. It outputs the strength of the given password and some suggestions to strengthen it (if applicable). This tool does not collect passwords or any other data.

How To Run -- This program was written in Python 3.x and has no dependencies besides the standard python library. To run, save the file as passwordChecker.py and execute with python 3 passwordChecker.py. It requires input from stdin and prints to the terminal.

Warnings/Limitations -- This password checker is a simple program and should not be used to guarantee password security. It can mark a password "Strong" even if it is frequently used or easy to guess. It does not check for common patterns or reused passwords. The password is visible in the terminal when entered.

Ethical Considerations -- This program is intended to be used for educational purposes, demonstrating basic password checking procedures and constructive feedback. This program should not be used to log users' passwords for malicious purposes. A "Strong" label does not necessarily mean the password is safe (security-wise) in all contexts. This checker does not account for uniqueness and vulnerability to guessing attacks.
