from simplecrypt import decrypt, DecryptionException

with open('passwords.txt') as pass_file:
    passwords = [line.strip() for line in pass_file]

with open('encrypted.bin', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

results = []

for password in passwords:
    result = False
    try:
        result = decrypt(password, encrypted)
    except DecryptionException:
        print('Bad password')
    if result:
        results.append(result)

print(results)
