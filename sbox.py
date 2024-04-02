import random

def generate_sbox(key):
    # Initialize the S-box with zeros
    sbox = [0] * 256
    # Generate a permutation of all possible bytes for the high-order byte
    permutation = list(range(256))
    random.shuffle(permutation)

    # Generate random values for the low-order 3 bytes
    random_values = [[random.randint(0, 255) for _ in range(3)] for _ in range(256)]
    
    # Combine the high-order byte and low-order 3 bytes to form the S-box entries
    for i in range(256):
        sbox[i] = ((permutation[i] << 24) | (random_values[i][0] << 16) | (random_values[i][1] << 8) | random_values[i][2])

    return sbox

# Generate the S-box using a key
key = [random.randint(0, 255) for _ in range(4)]  # Replace this with your actual key
sbox = generate_sbox(key)

# def generate_sbox():
#     sbox = [0] * 256
#     t = 0
#     for i in range(256):
#         t = (t + i) % 256
#         sbox[i] = bin(t)
#     return sbox

sbox = generate_sbox("key")
print(bin(ord('a')))
sbox.sort()
# for i in range(0,256):
    # print(sbox[i])