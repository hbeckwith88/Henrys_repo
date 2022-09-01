class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self,robot):
        print(f"{self.name} attacked {robot.name} and caused {self.attack_power} damage!")
        robot.health -= self.attack_power
        print(f"{robot.name} has {robot.health} health remaining!")
        print("")
       
        
   
