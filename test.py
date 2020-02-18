import sys
from normalize_english import normalize_

text = input("Enter an english sentence to be normalized:    ")
text = normalize_(text)
print()
print("------NORMALIZED TEXT:------")
print()
print(text)
