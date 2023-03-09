def get_who_win(objeckt_list:list):
    """"
    [player,enemy]
    """
    
    for objeckt in objeckt_list:
        #print(objeckt,objeckt.hp)
        if objeckt.hp <= 0:
            if objeckt.type == "Player":
                print("You Lose!")
            else:
                print("You win!")
            return objeckt.type
    return None