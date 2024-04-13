def get_hex_numeric_sequence(input_string):
    numeric_sequence = []
    for c in input_string:
        char_value = ord(c)
        numeric_sequence.append(char_value)
    return numeric_sequence