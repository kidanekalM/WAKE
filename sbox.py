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

print(sbox)












class WAKE:
    def __init__(self, key):
        self.key = key
        self.T = [0]*256
        self.initialize_T()

    def initialize_T(self):
        # This is a simplified example and does not represent the actual initialization of T in WAKE
        for i in range(256):
            self.T[i] = (i + self.key) % 256

    def encrypt(self, plaintext):
        ciphertext = []
        for char in plaintext:
            # This is a simplified example and does not represent the actual encryption process in WAKE
            ciphertext.append(char ^ self.T[char])
        return bytes(ciphertext)

    def decrypt(self, ciphertext):
        plaintext = []
        for char in ciphertext:
            # This is a simplified example and does not represent the actual decryption process in WAKE
            plaintext.append(char ^ self.T[char])
        return bytes(plaintext)

# Example usage
wake = WAKE(123)
ciphertext = wake.encrypt(b"Hello, World!")
print("Ciphertext:", ciphertext)
plaintext = wake.decrypt(ciphertext)
print("Plaintext:", plaintext)
#Fool