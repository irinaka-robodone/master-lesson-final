from pygame.locals import*
from src.world import World

world=World("asset/qa_v2.csv", 5, 5)

while world.running :
    world.process()
