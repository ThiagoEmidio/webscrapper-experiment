import random
import string

def generate_random_hash(n_chars:int=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    hash_result = ''.join(random.choices(characters, k=n_chars))
    return hash_result

# result = generate_random_hash()
# print(result)