# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

valid_card_regex = r"^(?!.*(\d)(?:-?\1){3})[456]\d{3}(?:-?\d{4}){3}$"

for _ in range(int(input())):
    card_number = input()
    if re.match(valid_card_regex, card_number):
        print("Valid")
    else:
        print("Invalid")