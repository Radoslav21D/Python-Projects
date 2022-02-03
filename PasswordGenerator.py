import random

print("Hello, Welcome to Password generator!")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = int(input("\nEnter the length of password: "))
amount = int(input("Enter the amount of passwords: "))

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
