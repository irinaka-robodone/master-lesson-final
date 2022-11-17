

class Player():
    
    def __init__(self,hp,speed) -> None:
        self.hp=0
        self.speed=0
        
    def attack(self):
        pass
    def die(self):
        self.hp = 0
        print("Game Over!")

player = Player(10,100)
player.die()