import csv
import pprint
import object
from object import Puizu

def puizuBOX():
    puizus=[]
    with open('bun.csv', encoding="utf-8") as f:
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
                puizu.choices=row[3]
                print(puizu)
                puizus.append([puizu])
    return puizus
puizues=puizuBOX()
print(puizues)
