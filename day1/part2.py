import re

def main(filename: str) -> int:
	"""Reads a file containing a calibration document.
	Prints the sum of the calibration values.
	"""
	with open(filename) as f:
		sum = sum_calibration_vals(f)
		print(sum)


def sum_calibration_vals(input) -> int:
	"""Takes a calibration document and returns the summed calibration values."""
	sum: int = 0
	for line in input:
		first, last = get_first_and_last_numbers(line)
		sum += int(str(first) + str(last))  # Concat digits then cast to int
	return sum


def get_first_and_last_numbers(s: str) -> (str, str):
	"""Takes a string and returns the first and last number inside it as a tuple.

	Numbers can be Unicode digits 0-9 or their equivalents spelled out.
	"""
	converted = convert_number_strings(s)
	digits = [x for x in converted if x.isdigit()]
	# print(f'{s} -> {converted} -> {digits}')
	try:
		first, last = digits[0], digits[-1]
		return first, last
	except IndexError:
		return 0


def convert_number_strings(s: str) -> str:
	"""Takes a string as input and returns the same string with all instances
	of spelled out digits 1-9 converted into decimal.

	Ex: 1three5seventeen -> 1357
	"""
	num_dict = {
		'one':   '1',
		'two':   '2',
		'three': '3',
		'four':  '4',
		'five':  '5',
		'six':   '6',
		'seven': '7',
		'eight': '8',
		'nine':  '9'
	}
	pattern = re.compile('|'.join(num_dict.keys()))
	replaced = re.sub(pattern, lambda m: num_dict[m.group(0)], s)
	return replaced

	
if __name__ == '__main__':
	main('input.txt')
