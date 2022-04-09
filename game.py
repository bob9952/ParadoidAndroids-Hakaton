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

def spinClicked(spinButton):
    mouse_position = pygame.mouse.get_pos()
    
    if spinButton.collidepoint(mouse_position):
        if pygame.mouse.get_pressed()[0] == 1:
            return True

    return False


pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slot Machine")
logo = pygame.image.load('Assets/banana.png')
pygame.display.set_icon(logo)
background_color = [230, 230, 230]

balance_font = pygame.font.SysFont("Arial", 50)
bet_amount_font = pygame.font.SysFont("Arial", 50)


slot_machine = pygame.image.load('Assets/slot-machine.png')
coins = pygame.image.load('Assets/coins.png')
coins = pygame.transform.scale(coins, (50, 50))

spinButton = pygame.Rect(370, 120, 60, 60)

strips = [slot.strip1, slot.strip2, slot.strip3]

run = True
balance = 1000
bet_amount = 10
n = 0
i, j, k = slot.selectShifts()
    
while run:
    screen.fill(background_color)

    screen.blit(slot_machine, (0, -40))
    current_balance_text = balance_font.render(str(balance), True, (0, 0, 0))
    screen.blit(current_balance_text, (600, 60))
    screen.blit(coins, (550, 70))
    
    # TODO: dynamic text aligment
    bet_amount_text = bet_amount_font.render(str(bet_amount), True, (0, 0, 0))
    screen.blit(bet_amount_text, (175, 515))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spinClicked(spinButton): 
                if balance >= bet_amount:
                    balance -= bet_amount
                    i, j, k = slot.selectShifts()   
                    strips = [slot.shift(slot.strip1,i), slot.shift(slot.strip2, j), slot.shift(slot.strip3, k)]
                    multi = slot.check(strips)
                    balance += multi * bet_amount 
    
    drawOnSlot(screen, strips)
            
    n += 1

    pygame.display.update()

pygame.quit()
