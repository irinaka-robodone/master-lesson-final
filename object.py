
class Player():
    def __init__(self,hp,guard) -> None:
        self.hp=hp
        self.guard=guard
        self.type="Player"
    def die(self):
        print("Game Over!")

    def attack(self,pwa,opponent ):
        opponent.get_damage(pwa)
        
    def get_damage(self,damage):
        damage -= self.guard
        self.hp-=damage
        print("player1.hp "+str(self.hp))

class Enemy():
    def __init__(self,hp,guard) -> None:
        self.hp=hp
        self.guard=guard
        self.type="Enemy"

    def attack(self,pwa,opponent ):
        opponent.get_damage(pwa)

    def get_damage(self,damage):
        damage -= self.guard
        self.hp-=damage
        print("enemy1.hp "+str(self.hp))