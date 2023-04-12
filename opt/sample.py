import math
import sys

def main():
	val = float(sys.argv[1])
	print(math.radians(val))
	num = sum(1, 2)
	print(num)
	arr = [1, 2, 3, 4, 5]
	for i in arr:
		print(i)
	while True:
		print("Hello World")
		break
	taple = (1, 2, 3, 4, 5)
	for i in taple:
		print(i)
	# diff array and taple
	# array is mutable and taple is immutable
	# array can be changed and taple can't be changed
	# array can be changed by using append, insert, remove, pop, clear, extend, sort, reverse
	# taple can't be changed by using append, insert, remove, pop, clear, extend, sort, reverse
	arr.append(6)
	print(arr)
	# taple.append(6)
	# print(taple)


def sum(a, b):
	return a + b

if __name__ == "__main__":
	main()

