import random
from sbox import sBlock

#shuffle the sbox to add more confusion
#use same sbox for one session i.e to encrypt and decrypt
random.shuffle(sBlock)
# print(sBlock)

def calculate_next_value(R, prevR):
    R_decimal = int(R, 16)
    prevR_decimal = int(prevR, 16)

    sum_val = R_decimal + prevR_decimal
    S_index = sum_val & 255
    S_value = sBlock[S_index]  # Assuming get_S_value is defined elsewhere
    result = (sum_val >> 8) ^ S_value

    return '{:08X}'.format(result)

def get_hex_numeric_sequence(input_string):
    numeric_sequence = []
    for c in input_string:
        char_value = ord(c)
        numeric_sequence.append(char_value)
    return numeric_sequence

#Generate aoto key from the input key
def get_auto_key(plain_key):
    # Get hex key
    hexadecimal_result = []
    for c in plain_key:
        #hex_value = format(ord(c), 'X2')
        hex_value ='{:02X}'.format(ord(c))
        hexadecimal_result.append(hex_value)
    hex_key = ''.join(hexadecimal_result)
    if len(hex_key) < 16:
        print("Error", "Enter a key of at least 16 characters.")
        return
    #init registers
    R3 = hex_key[0:8]
    R4 = hex_key[8:16]
    R5 = hex_key[16:24]
    R6 = hex_key[24:32] 
    R3_next = calculate_next_value(R3, R6)
    R4_next = calculate_next_value(R4, R3_next)
    R5_next = calculate_next_value(R5, R4_next)
    R6_next = calculate_next_value(R6, R5_next)

    new_key = R6_next
    return new_key

def decrypt(cipher_text,key):
    encrypted_numeric = get_hex_numeric_sequence(cipher_text)
    key_numeric = get_hex_numeric_sequence(get_auto_key(key))

    decrypted_numeric = []
    for i in range(len(encrypted_numeric)):
        #print("aaa",encrypted_numeric[i],type( key_numeric[i % len(key_numeric)]))
        decrypted_char = encrypted_numeric[i] ^ key_numeric[i % len(key_numeric)]
        decrypted_numeric.append(decrypted_char)

    decrypted_text = ''.join(chr(num) for num in decrypted_numeric)
    # print("Decrypted text: ",decrypted_text)
    return decrypted_text

def encrypt(plaintext,input_key):
    key = get_auto_key(input_key)

    plaintext_numeric = get_hex_numeric_sequence(plaintext)
    key_numeric = get_hex_numeric_sequence(key)

    encrypted_numeric = []
    for i in range(len(plaintext_numeric)):
        encrypted_char = plaintext_numeric[i] ^ key_numeric[i % len(key_numeric)]
        encrypted_numeric.append(encrypted_char)

    encrypted_text = ''.join(chr(num) for num in encrypted_numeric)
    return encrypted_text
    # print("Encrypted text: " , encrypted_text)
    # textBox2.delete("1.0", "end")
    # textBox2.insert("1.0", encrypted_text)

    # dataGridView1.delete(*dataGridView1.get_children())

    # for i in range(len(plaintext)):
    #     dataGridView1.insert('', 'end', values=(i + 1, plaintext[i], plaintext_numeric[i], key_numeric[i % len(key_numeric)], encrypted_numeric[i], chr(encrypted_numeric[i])))

    # return encrypted_text

enc = encrypt("FineGuy","FineTheManBerariwSuperman")
dec = decrypt(enc,"FineTheManBerariwSuperman")
print("Encrypted text: ",enc)
print("Decrypted text: ",dec)













