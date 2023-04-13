import math
import sys
# range
for i in range(2, 10, 3):
    print(i)

for i in ["apple", "banana", "orange"]:
    print(i)

# enumerate 
# enumerateはインデックス番号と要素を取得できる
for i, fruit in enumerate(["apple", "banana", "orange"]):
    print(i, fruit)

# zip
# zipは複数のリストを同時にループ処理できる
for i, fruit, money in zip([1, 2, 3, 4], ["apple", "banana", "orange", "melon"], [100, 200, 300, 400]):
    print(i, fruit, money)

# クロージャー
# クロージャーは関数の中で関数を定義することができる

def outer(a, b):
    def inner():
        return a + b
    return inner

f = outer(1, 2)
r = f()
print(r)

# デコレーター
# デコレーターは関数の前後で処理を追加することができる

def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return wrapper

@print_info
def add_num(a, b):
    print(a + b)

add_num(10, 20)

# apiを叩く
import requests

# 例外処理
# r = requests.get("https://api.github.com/events")
# print(r.text)

try:
    r = requests.get("https://api.github.com/events/1")
    r.raise_for_status()
    print(r.text)
except requests.exceptions.HTTPError as err:
    print(err)





