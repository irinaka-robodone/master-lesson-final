
class Player():
    def __init__(self) -> None:
        self.hp=10
    def die(self):
        print("Game Over!")
        

player=Player()
print(player)
print(player.hp)
print(player.die())