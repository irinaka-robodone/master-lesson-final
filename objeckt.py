import random
import pygame


class Enemy():
    
    def __init__(self,hp,kaihuku) -> None:
        self.hp=hp
        self.kaihuku=kaihuku
        self.type="Enemy"
        
    def get_attack(self):
        self.hp -= 5
        print("敵hp:",self.hp)

    def X_attck(self,player):
        player.hp -= random.randrange(0,int(player.hp*1.5),3)
        print("自分hp",player.hp)
        
class Player():
    
    def __init__(self,hp,speed) -> None:
        self.hp=hp
        self.speed=speed
        self.type="Player"
        
    def attack(self,enemy:Enemy):
        enemy.get_attack()
        
        
    def die(self):
        self.hp = 0
        print("Game Over!")
        
    def is_winer(self,enemy:Enemy):
        if enemy.hp <= 10:
            print("Your winer")
        else:
            pass
