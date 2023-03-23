from pygame.locals import*
from world import Wold

wold=Wold("asset/bun_v2.csv")

while wold.running :
    wold.process()
