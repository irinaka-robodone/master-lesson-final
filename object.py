import random
import pygame

class Teki():

    def __init__(self,hp,speed,kasikosa) -> None:
        self.hp = hp
        self.speed_hp_increase = speed
        self.type = "teki"
    def attack(self):
        if self.hp<=0:
            print("YOU WIN!")

    def get_damage(self):
        self.hp-=1
        print(self.hp)

    def random_attack(self,opponent):
        opponent.hp -= random.randreng(0,int(opponent,hp*10),3)

class Player():

    def __init__(self,hp,speed,kasikosa) -> None:
        self.hp = hp
        self.speed = speed
        self.kasikosa = kasikosa
        self.type = "player"


    def attack(self,enemy_object: Teki):
        enemy_object.get_damage()
        if enemy_object.hp <=0:
            print("YOU WIN!")
        else:
            pass

    def die(self):
        self.hp = 0
        print("!!Game Over!!")





