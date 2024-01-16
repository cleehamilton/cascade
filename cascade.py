from random import randrange

class character:
    def __init__(self, char_name, health, damage, speed):
        self.name = char_name
        self.health = health
        self.damage = damage
        self.speed = speed

    def display(self):
        #display stats
        print(f"\n:::{self.name} Stats:::")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Speed: {self.speed}")
        
    def double_speed(self):
        self.speed *= 2
        
    def battle_loss(self,roll):
        self.health -= roll
        
warrior = character('Warrior',100,5,2)
ninja = character('Ninja',100,4,4)

## compile list of characters

dead = 0
if __name__ == '__main__':
    warrior.display()
    ninja.display()
    rpt = int(input(f"\nReady to Battle, Press 1 to Battle or 9 to Exit. "))
    while rpt == 1:
        #input(f"Choose your character: ")
       
        print("\nBATTLE!")
        roll = randrange(11)
        print(f"you rolled a {roll}!")
        if roll % 2 == 0:
            print(f"Ninja Stikes first!")
            roll *= ninja.damage
            warrior.battle_loss(roll)
            if warrior.health <= 0:
                warrior.health = 0
            print(f"Warrior damaged to health -{roll} points. Warrior new health is {warrior.health}.")
            if warrior.health <= 0:
                d = input(f"\nThe Warrior recieved a fatal blow, and died. The Ninja Wins! ")
                dead = 1
        else:
            print(f"Warrior Stikes first!")
            roll *= warrior.damage
            ninja.battle_loss(roll)
            if ninja.health <= 0:
                ninja.health = 0
            print(f"Ninja damaged to health -{roll} points. Ninja new health is {ninja.health}.")
            if ninja.health <= 0:
                d = input(f"\nThe Ninja recieved a fatal blow, and died. The Warrior Wins! ")
                dead = 1
        if dead != 1:
            r = int(input(f"Press 1 to Battle again or 9 to exit. "))
        else:
            r = 0
        if r == 1:
            rpt = 1
            print("-------------------------------")
            warrior.display()
            ninja.display()
        else:
            rpt = 9
            
