import secrets


generated_key = secrets.token_urlsafe(16)
print(generated_key)