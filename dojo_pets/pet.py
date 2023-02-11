
class Pet:
    def __init__(self,name,type,tricks,sound):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.sound =sound
        self.health = 100
        self.energy = 100
        


    def sleep(self):
        self.energy+=25
        return self

    def eat(self):
        self.energy+=5
        self.health+=10
        return self

    def play(self):
        self.health+=5
        self.energy-=10
        return self

    def noise(self):
        print(self.sound)

    def display(self):
        if self.energy<100:
            print(f"Oh! {self.name} should eat and sleep a while!")
        else:
            print(f"Let's play {self.name}")
        return self


findik=Pet("findik","cat","sleeping","meow")
findik.play().display()