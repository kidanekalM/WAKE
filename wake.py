def get_hex_numeric_sequence(input_string):
    numeric_sequence = []
    for c in input_string:
        char_value = ord(c)
        numeric_sequence.append(char_value)
    return numeric_sequence

def decrypt(cipher_text,key):
    encrypted_text = cipher_text

    encrypted_numeric = get_hex_numeric_sequence(encrypted_text)
    key_numeric = get_hex_numeric_sequence(key)

    decrypted_numeric = []
    for i in range(len(encrypted_numeric)):
        decrypted_char = encrypted_numeric[i] ^ key_numeric[i % len(key_numeric)]
        decrypted_numeric.append(decrypted_char)

    decrypted_text = ''.join(chr(num) for num in decrypted_numeric)

    return decrypted_text