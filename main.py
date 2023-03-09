from pygame.locals import*
from world import Wold

wold=Wold("asset/bun.csv")

while wold.running :
    wold.process()
