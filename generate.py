import secrets

# Generate a 50-character hexadecimal secret key
secret_key = secrets.token_hex(50)
print(secret_key)
