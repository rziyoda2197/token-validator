class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class TokenValidator:
    def __init__(self):
        self.valid_token_types = ['ACCESS_TOKEN', 'REFRESH_TOKEN', 'AUTHORIZATION_CODE']
        self.valid_token_values = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

    def validate_token(self, token):
        if not isinstance(token, Token):
            return False

        if token.token_type not in self.valid_token_types:
            return False

        if not all(char in self.valid_token_values for char in token.value):
            return False

        return True

# Misol:
token_validator = TokenValidator()

token1 = Token('ACCESS_TOKEN', 'abc123')
print(token_validator.validate_token(token1))  # True

token2 = Token('INVALID_TOKEN', 'abc123')
print(token_validator.validate_token(token2))  # False

token3 = Token('ACCESS_TOKEN', 'abc!@#')
print(token_validator.validate_token(token3))  # False
