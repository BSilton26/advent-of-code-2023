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
		first, last = get_first_and_last_digit(line)
		sum += int(str(first) + str(last))  # Concat digits then cast to int
	return sum


def get_first_and_last_digit(s: str) -> (str, str):
	"""Takes a string and returns the first and last digit inside it as a tuple."""
	digits = [x for x in s if x.isdigit()]
	try:
		first, last = digits[0], digits[-1]
		return first, last
	except IndexError:
		return 0

	
if __name__ == '__main__':
	main('input.txt')
