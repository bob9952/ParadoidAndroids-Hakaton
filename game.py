import pygame
import slot

numToFruitName = {
    1:"apple",
    2:"cherry",
    3:"plum",
    4:"grape",
    5:"banana",
    6:"diamond",
    7:"diamond",
    8:"diamond"
}

fruitNameToImage = {
    "apple":pygame.image.load("Assets/apple.png"),
    "cherry":pygame.image.load("Assets/cherry.png"),
    "plum":pygame.image.load("Assets/plum.png"),
    "grape":pygame.image.load("Assets/grape.png"),
    "banana":pygame.image.load("Assets/banana.png"),
    "diamond":pygame.image.load("Assets/diamond.png")
}

positions = [ [(45,120), (45, 220), (45, 325)], 
             [(158, 120), (158, 220), (158, 325)], 
             [(272, 120), (272, 220), (272, 325)]  ]

def drawOnSlot(screen, strips):
    global positions
    for i in range(3):
        for j in range(3):
            fruitName = numToFruitName[strips[i][j]]
            image = fruitNameToImage[fruitName]
            image = pygame.transform.scale(image, (85, 85))

            screen.blit(image, positions[i][j])


pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slot Machine")
logo = pygame.image.load('Assets/banana.png')
pygame.display.set_icon(logo)
background_color = [250, 239, 147]

slot_machine = pygame.image.load('Assets/slot-machine.png')

run = True
n = 0
i, j, k = slot.selectShifts()
    
while run:
    screen.fill(background_color)

    screen.blit(slot_machine, (0, -40))
    if not (n % 500): 
        i, j, k = slot.selectShifts()    
    drawOnSlot(screen, [slot.shift(slot.strip1,i), slot.shift(slot.strip2, j), slot.shift(slot.strip3, k)])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    n += 1

    pygame.display.update()

pygame.quit()
