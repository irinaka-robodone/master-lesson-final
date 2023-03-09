from pygame.locals import*
from world import Wold

wold=Wold("bun_v2.csv")

while wold.running :
    wold.process()
