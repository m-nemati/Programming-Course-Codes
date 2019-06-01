class Computer:
    
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
    
    def value(self):
        return self.ram + self.hard + self.cpu
class Laptop(Computer):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size

pc1 = Computer(12, 2, 4)
pc2 = Computer(8, 4, 3)
laptop1 = Laptop(16, 2, 4)
laptop1.size = 14

print (pc1.value())
print (pc2.value())
print (laptop1.value())