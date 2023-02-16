import csv
import pprint
import object
from object import Puizu
import random

#def callback_func():



def puizuBOX(file):
    puizus=[]
    with open(file, encoding="utf-8") as f:
        #print(f.read())
        reader=csv.reader(f)

        for i,row in enumerate(reader):
            #print(row)
            if i < 1:
                pass
            else:
                puizu=Puizu()
                puizu.question=row[0]
                puizu.type=row[1]
                puizu.answer=row[2]
                puizu.choices=[]
                puizu.choices.append(row[3])
                puizu.choices.append(row[4])
                puizu.choices.append(row[5])
                puizu.choices.append(row[6])
                
                
                puizus.append(puizu)
    return puizus
#puizues=puizuBOX()
# puizues = puizues[random.randint(0,2)]
# print(puizues)
