def get_who_win(object_list:list):

    for object in object_list:
        if object.hp <=0:
            if object.type == "player":
                print("You lose")
            else:
                print("You win!!")
            return object.type
        else:
            return None