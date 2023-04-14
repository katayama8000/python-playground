# class
# animalクラス
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("name:", self.name, "age:", self.age)
    def speak(self):
        pass

# dogクラス # animalクラスを継承
class dog(animal):
    def speak(self):
        print("bowwow")
    
# catクラス # animalクラスを継承
class cat(animal):
    def speak(self):
        print("meow")

def main():
    dog1 = dog("dog1", 3)
    dog1.show()
    dog1.speak()
    cat1 = cat("cat1", 2)
    cat1.show()
    cat1.speak()

# main
if __name__ == "__main__":
    main()
