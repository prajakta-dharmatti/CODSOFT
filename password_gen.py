import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
symbol = string.punctuation


print("----- Welcome to the Password Generator ----")

while True:
        pass_len = int(input("Enter the desired length of password (minimum 8): "))
        
        if pass_len < 8:
            print("Password length should be greater than or equal to 8.")
            continue
        else:
            break

def generate_custom_password(n_letters, n_digits, n_symbols):
    password = []
    for _ in range(n_letters):
        password.append(random.choice(upper + lower))
    for _ in range(n_digits):
        password.append(random.choice(digit))
    for _ in range(n_symbols):
        password.append(random.choice(symbol))
    
    random.shuffle(password)
    return ''.join(password)


        
print("\n--- Custom Password Options ---")
n_letters = int(input("How many letters do you want: "))
n_digits = int(input("How many digits do you want: "))
n_symbols = int(input("How many symbols do you want: "))
    
if n_letters + n_digits + n_symbols != pass_len:
    print("The total of letters, digits, and symbols must equal the desired password length.")
else:
    custom_password = generate_custom_password(n_letters, n_digits, n_symbols)
    print(f"Custom Password: {custom_password}")


    






   
    
