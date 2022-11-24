import random
import pygame

class Enemy():
    
    def __init__(self, hp, speed_hp_increase) -> None:
        self.hp = hp
        self.speed_hp_increase = speed_hp_increase

    def is_die(self):
        if self.hp <= 0: 
            print("you win!")
    
    def get_damage(self):
        self.hp -= 0.5
    
    def random_attack(self, opponent):
        opponent.hp -= random.randrange(0,int(opponent.hp*0.5),1)

class Player():
    
    def __init__(self, hp, speed, wisdom) -> None:
        self.hp = hp
        self.speed = speed
        self.wisdom = wisdom
        
    def attack(self, enemy_object: Enemy):
        """
        Player クラスができる処理！
        """
        enemy_object.get_damage()
        
    def is_winner(self, enemy_object: Enemy):
        if enemy_object.hp <= 0:
            print("You win!")
        else:
            pass
    
    def die(self):
        self.hp = 0
        print("Game Over!")
        
        
player = Player(10,20,30)
enemy = Enemy(20, 0.1)


player.attack(enemy)



"""
本日のTodo
1. player は敵に攻撃できる
2. 攻撃すると敵のHPが減る
3. 敵のHPは時間とともに増えていく
4. 敵はランダムにプレイヤーのHPを減らしていく
4. 増えるスピードよりも早くキーを連打して敵のHPをゼロにする
"""