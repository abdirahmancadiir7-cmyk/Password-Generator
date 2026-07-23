import random
import string

print("=" * 50)
print("        PASSWORD GENERATOR")
print("=" * 50)

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for _ in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
