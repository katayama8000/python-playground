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

# main
if __name__ == "__main__":
    d = dog("pochi", 3)
    d.show()
    d.speak()
    c = cat("tama", 5)
    c.show()
    c.speak()
    a = animal("animal", 10)
    a.show()
    a.speak()

