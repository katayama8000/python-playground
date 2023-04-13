import math
import sys
from functions import add_numbers, multiply_numbers

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
	num_tuple = (1, 2, 3, 4, 5)
	x, y, z, a, b = num_tuple
	print(x, y, z, a, b)
	# 辞書
	dict = {"apple": "りんご", "orange": "みかん", "grape": "ぶどう"}
	print(dict["apple"])
	# 集合型
	set = {"apple", "orange", "grape"}
	print(set)
	# 集合のメソッド
	set.add("banana")
	print(set)
	set.remove("banana")
	print(set)
	set.clear()
	print(set)
	set = {"apple", "orange", "grape"}
	set2 = {"banana", "melon", "grape"}
	set3 = set | set2
	print(set3)
	set4 = set & set2
	print(set4)
	set5 = set - set2 # 両方にあるもの
	print(set5)
	set6 = set ^ set2 # どちらかにしかないもの
	print(set6)
	# 関数
	print(sum(1, 2))
	print(sub(1, 2))
	print("--------------------")
	result1 = add_numbers(1, 2)
	result2 = multiply_numbers(3, 4)

	print(result1)  # 3
	print(result2)  # 12



def sum(a, b):
	return a + b

# 型をつけた関数
# 引き算
def sub(a: int, b: int) -> int:
	return a - b

if __name__ == "__main__":
	main()

