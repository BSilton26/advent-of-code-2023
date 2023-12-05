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

	# Match all nums or their strings, including overlaps
	nums_pattern = re.compile(r"(?=(\d|" + '|'.join(num_dict.keys()) + r"))")
	all_nums = nums_pattern.findall(s)
	first, last = all_nums[0], all_nums[-1]
	if len(first) > 1:  # Not pretty, but relatively efficient
		first = num_dict[first]
	if len(last) > 1:
		last = num_dict[last]
	return first, last


def convert_number_strings(s: str) -> str:
	"""Takes a string as input and returns the same string with all instances
	of spelled out digits 1-9 converted into decimal.

	Ex: 1threee5seventeen -> 13e57teen

	Doesn't work for this problem! Fails because it always chooses the leftmost
	number in cases where they overlap (e.g. 'twone'), and we'd want to choose 
	the rightmost at the end of the string.

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
