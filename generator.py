import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', '\\', '{', '}', '|', ';', "'", ':', '"', ',', '.', '/', '<', '>', '?', '`', '~']

print("\nBem-vindo ao generator de senhas!")
print(r'''
       .-""-.
      / .--. \
     / /    \ \
     | |    | |
     | |.-""-.|
    ///`.::::.`\      8 8          ,o.  
   ||| ::/  \:: ;    d8o8azzzzzzzzd   b 
   ||; ::\__/:: ;                  `o' 
    \\\ '::::' /
     `=':-..-'`
''')

password = []

nr_letters = int(input("Quantas letras deseja na sua senha?\n"))

count_letter = 0
for letter in range(0, nr_letters):
    count_letter += 1
    if count_letter < nr_letters + 1:
        letter_random = rd.choice(letters)
        password.append(letter_random)

nr_symbols = int(input(f"Quantos símbolos deseja incluir?\n"))

count_symbols = 0
for symbol in symbols:
    count_symbols += 1
    if count_symbols < nr_symbols + 1:
        symbol_random = rd.choice(symbols)
        password.append(symbol_random)

nr_numbers = int(input(f"Quantos números deseja incluir?\n"))

count_number = 0
for number in numbers:
    count_number += 1
    if count_number < nr_numbers + 1:
        number_random = rd.choice(numbers)
        password.append(number_random)

rd.shuffle(password)
new_password = "".join(password)
print(f"\nSua senha é:\n\n  {new_password}")

