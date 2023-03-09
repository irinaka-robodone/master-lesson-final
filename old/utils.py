def get_who_win(object_list: list):
    """
    [player, enemy]
    """
    for object in object_list:
        if object.hp <= 0:
            if object.type == "Player":
                print("You lose!")
            else:
                print("You win!")
            return object.type
    
    return None         # None型: データ何もなし
        