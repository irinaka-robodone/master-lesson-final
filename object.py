import random
import pygame

class Enemy():
    
    def __init__(self, hp, guard) -> None:
        self.hp = hp
        self.type = "Enemy"
        # self.speed_hp_increase = speed_hp_increase

    def is_die(self):
        if self.hp <= 0: 
            print("you win!")
    
    def get_damage(self, damage):
        self.hp -= damage
        """
        テスト用
        Python ではprintして上手くいっているかをよくチェックする
        """
        print("敵hp:", self.hp)
    
    def random_attack(self, opponent):
        damage = random.randrange(0,int(opponent.hp*1.3),1)
        opponent.get_damage(damage)
        
class Player():
    
    def __init__(self, hp, speed, wisdom) -> None:
        self.hp = hp
        self.speed = speed
        self.wisdom = wisdom
        self.type = "Player"
        
    def attack(self, enemy_object: Enemy):
        """
        Player クラスができる処理！
        """
        enemy_object.get_damage(10)
        
    def is_winner(self, enemy_object: Enemy):
        if enemy_object.hp <= 0:
            print("You win!")
        else:
            pass
    def get_damage(self, damage):
        self.hp -= damage
        print("Player HP:", self.hp)
    
    def die(self):
        self.hp = 0
        print("Game Over!")
        
        


"""
本日のTodo
1. player は敵に攻撃できる
2. 攻撃すると敵のHPが減る
3. 敵のHPは時間とともに増えていく
4. 敵はランダムにプレイヤーのHPを減らしていく
4. 増えるスピードよりも早くキーを連打して敵のHPをゼロにする
"""