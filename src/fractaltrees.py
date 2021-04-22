import pygame
import math

# Variables
(width, height) = (900, 900)
background_color = pygame.Color(47, 143, 148)
branch_color = pygame.Color(81, 207, 150)
depth = 9
angleMod = .1
lengthMod = 1.4


# Setup code
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fractal Trees')
screen.fill(background_color)


# Classes
# Class branch represents a branch of the tree
class Branch:

    def __init__(self, x, y, ang, length):
        self.x = x
        self.y = y
        self.ang = ang
        self.endx = x + length * math.sin(ang)
        self.endy = y - length * math.cos(ang)
        self.length = length

    # Draws the line
    def display(self):
        pygame.draw.line(screen, branch_color, (self.x, self.y), (self.endx, self.endy))


# Recursive draw function
def drawtree(prevBrEndX, prevBrEndY, prevBrAng, prevBrLen, remDepth):
    if remDepth > 0:
        br1 = Branch(prevBrEndX, prevBrEndY, (prevBrAng+angleMod) % (2*math.pi), prevBrLen / lengthMod)
        br2 = Branch(prevBrEndX, prevBrEndY, (prevBrAng-angleMod) % (2*math.pi), prevBrLen / lengthMod)
        br1.display()
        br2.display()
        drawtree(br1.endx, br1.endy, br1.ang, br1.length, remDepth - 1)
        drawtree(br2.endx, br2.endy, br2.ang, br2.length, remDepth - 1)
        del br1  # Mem cleanup, going to add sliders so don't want these objects clogging stuff up
        del br2  # Probably will just remove the class altogether


def main():

    # Make a root of the tree
    root = Branch(width/2, height, 0, 200)
    root.display()
    # Make the recursive call
    drawtree(root.endx, root.endy, root.ang, root.length, depth)
    # Update the display
    pygame.display.flip()

    # Termination conditions
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

pygame.display.flip()

if __name__ == "__main__":
    main()
