# Hamming Code - encoding and decoding processes

def convert_letter_to_ASCII_value(letter = 'a'):
	return ord(letter)


def convert_ASCII_value_to_8bit_binary(ascii_value = 100):

	result_bin_value = bin(ascii_value)[2:]
	
	if len(result_bin_value) != 8:
		result_bin_value = '0' * (8 - len(result_bin_value)) + result_bin_value
		return result_bin_value
	else:
		return result_bin_value

def getting_triple_value(value = '0'):
	return 3 * value

def hamming_encoding(string = 'test'):
	ascii_code_of_letters_in_str = []
	for letter in string:
		ascii_code_of_letters_in_str.append(convert_letter_to_ASCII_value(letter))

	ascii_code_of_str_letters_in_8bit = []
	for value in ascii_code_of_letters_in_str:
		ascii_code_of_str_letters_in_8bit.append(convert_ASCII_value_to_8bit_binary(value))

	tripled_8bit_ascii_codes_of_letters = []
	for value in ascii_code_of_str_letters_in_8bit:
		for digit in value:
			tripled_8bit_ascii_codes_of_letters.append(getting_triple_value(digit))

	
	result_encoded_string = ''.join(tripled_8bit_ascii_codes_of_letters)
	return result_encoded_string


input_str = 'hello. this is me.'
encoded_str = hamming_encoding(input_str)
print(encoded_str)


def splitting_by_three_elements(string = '123456'):
	if len(string) % 24 != 0:
		return 'error'

	result_grouped_elements = []
	for i in range(0, len(string), 3):
		result_grouped_elements.append(string[i:i + 3])

	print(result_grouped_elements)
	return result_grouped_elements

def get_corrected_bits_from_strings(strings = ['001']):
	result_corrected_bits = []
	for string in strings:
		if string.count('0') > string.count('1'):
			result_corrected_bits.append('0')
		elif string.count('1') > string.count('0'):
			result_corrected_bits.append('1')

	return result_corrected_bits

def get_grouped_8bits(bits_list = ['0']):
	result_8bits_elements = []
	for i in range(0, len(bits_list), 8):
		result_8bits_elements.append(''.join(bits_list[i:i + 8]))

	print(result_8bits_elements)
	return result_8bits_elements


def converting_bits_to_decimal_nums(elems_with_8bits = ['00110010']):
	decimal_numbers = []
	for elem in elems_with_8bits:
		decimal_numbers.append(int(elem, 2))

	return decimal_numbers

def convert_ascii_values_into_characters(decimal_numbers = [100]):
	result_string = ''
	for number in decimal_numbers:
		result_string += chr(number)

	return result_string


def hamming_decoding(bin_string = '0010'):
	grouped_by_three_elements = splitting_by_three_elements(bin_string)
	corrected_bits = get_corrected_bits_from_strings(grouped_by_three_elements)
	groupted_by_8bits = get_grouped_8bits(corrected_bits)
	decimal_nums_from_8bits = converting_bits_to_decimal_nums(groupted_by_8bits)
	decoded_string = convert_ascii_values_into_characters(decimal_nums_from_8bits)

	return decoded_string

decoded_str = hamming_decoding(encoded_str)
print('Decoded string:', decoded_str)