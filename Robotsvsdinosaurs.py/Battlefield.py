from robots import Robot
from dinosaurs import Dinosaur



class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Godzilla", 50)
        self.robot = Robot("Mega-Man")
         
        
        
    def run_game(self): 
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print("")
        print("Welcome to this exciting battle between Mega-man and a T-Rex!")
        print("")
    
    def battle_phase(self): 
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            if self.robot.health == 0 or self.dinosaur.health == 0:
                break

    def display_winner(self):
        if self.robot.health <= 0:
            print(f"Oh no! {self.robot.name} has fallen in battle! {self.dinosaur.name} wins the battle!!!")
        elif self.dinosaur.health <= 0:
            print(f"{self.robot.name} is victorious!!! {self.dinosaur.name} has fallen!!!")

          
            