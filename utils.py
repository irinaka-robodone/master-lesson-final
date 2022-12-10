import object
def get_who_lose(object_list:list):
    for object in object_list:
        if object.hp<=0:
            if object.type=="Player":
                print("勝ち")
            elif object.type=="Enemy":
                print("負け")
            return object.type
    
    return None