c1 = "01000011 01000010 01010110 01001000 01010100 01001010 01000100 01001110 01010110 01010001"
binary_values = c1.split()

ascii_string = ""
for binary_value in binary_values:
    an_integer = int(binary_value, 2)

    ascii_char = chr(an_integer)
    ascii_string += ascii_char

print(ascii_string)

################################################

string1 = "AARDWOLVES"

a_byte_array = bytearray(string1, "utf8")

byte_list = []

for byte in a_byte_array:
    bin_representation = bin(byte)

    byte_list.append(bin_representation)

print(byte_list)

##############################


