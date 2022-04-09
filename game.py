from turtle import back
import pygame
import slot
import time

numToFruitName = {
    1: "apple",
    2: "cherry",
    3: "plum",
    4: "grape",
    5: "banana",
    6: "totem-head1",
    7: "totem-head2",
    8: "totem-head3"
}

fruitNameToImage = {
    "apple": pygame.image.load("Assets/apple.png"),
    "cherry": pygame.image.load("Assets/cherry.png"),
    "plum": pygame.image.load("Assets/plum.png"),
    "grape": pygame.image.load("Assets/grape.png"),
    "banana": pygame.image.load("Assets/banana.png"),
    "totem-head1": pygame.image.load("Assets/totem-head1.png"),
    "totem-head2": pygame.image.load("Assets/totem-head2.png"),
    "totem-head3": pygame.image.load("Assets/totem-head3.png")
}

positions = [[(45, 118), (45, 220), (45, 323)],
             [(158, 118), (158, 220), (158, 323)],
             [(272, 118), (272, 220), (272, 323)]]


def animate(screen, strips, i, j, k):
    # 
    num_of_shifts = len(strips[0])
    i = i + num_of_shifts
    j = j + num_of_shifts
    k = k + num_of_shifts

    p = 0
    q = 0
    r = 0

    while p < i or q < j or r < k:
        clock.tick(10)

        if p < i:
            p += 1
        if q < j:
            q += 1
        if r < k:
            r += 1

        drawCanvas()
        new_strips = [slot.shift(strips[0], p), slot.shift(strips[1], q), slot.shift(strips[2], r)]
        # slot.printSlot(new_strips)

        drawOnSlot(screen, new_strips)

        pygame.display.update()


def drawOnSlot(screen, strips):
    global positions
    for i in range(3):
        for j in range(3):
            fruitName = numToFruitName[strips[i][j]]
            image = fruitNameToImage[fruitName]

            if strips[i][j] <= 5:
                image = pygame.transform.scale(image, (85, 85))
                screen.blit(image, positions[i][j])
            elif strips[i][j] == 6:
                image = pygame.transform.scale(image, (85, 85))
                x, y = positions[i][j]
                y = y + 9
                screen.blit(image, (x, y))
            elif strips[i][j] == 7:
                image = pygame.transform.scale(image, (85, 97))
                x, y = positions[i][j]
                y = y - 2
                screen.blit(image, (x, y))
            elif strips[i][j] == 8:
                image = pygame.transform.scale(image, (85, 85))
                x, y = positions[i][j]
                y = y - 4
                screen.blit(image, (x, y))


def buttonClicked(button):
    mouse_position = pygame.mouse.get_pos()

    if button.collidepoint(mouse_position):
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

bet_amount_font = pygame.font.SysFont("Arial", 50, bold=True)
balance_font = pygame.font.SysFont("Arial", 50, bold=True)
multipliers_font = pygame.font.SysFont("Arial", 35, bold=True)

slot_machine = pygame.image.load('Assets/slot-machine.png')
background = pygame.image.load('Assets/background.jpg')
background = pygame.transform.scale(background, (width, height))
coins = pygame.image.load('Assets/coins.png')
coins = pygame.transform.scale(coins, (50, 50))

spinButton = pygame.Rect(370, 120, 60, 60)
lower100Button = pygame.Rect(95, 430, 40, 40)
lower10Button = pygame.Rect(155, 430, 40, 40)
increase10Button = pygame.Rect(215, 430, 40, 40)
increase100Button = pygame.Rect(275, 430, 40, 40)

strips = [slot.strip1, slot.strip2, slot.strip3]

run = True
clock = pygame.time.Clock()

balance = 1000
bet_amount = 10
strip_len = len(strips[0])
n = 0
# i, j, k = slot.selectShifts()
# current_i = i
# current_j = j
# current_k = k
i, j, k = 0, 0, 0
current_i = 0
current_j = 0
current_k = 0


def drawCanvas(row=-1, isWinningRow=False):
    screen.blit(background, (0, 0))

    if isWinningRow:
        if row == 0:
            pygame.draw.rect(screen, (255, 215, 0), (30, 115, 335, 98))
            pygame.draw.rect(screen, (230, 230, 230), (30, 215, 335, 98))
            pygame.draw.rect(screen, (230, 230, 230), (30, 315, 335, 98))
        if row == 1:
            pygame.draw.rect(screen, (230, 230, 230), (30, 115, 335, 98))
            pygame.draw.rect(screen, (255, 215, 0), (30, 215, 335, 98))
            pygame.draw.rect(screen, (230, 230, 230), (30, 315, 335, 98))
        if row == 2:
            pygame.draw.rect(screen, (230, 230, 230), (30, 115, 335, 98))
            pygame.draw.rect(screen, (230, 230, 230), (30, 215, 335, 98))
            pygame.draw.rect(screen, (255, 215, 0), (30, 315, 335, 98))
    else:
        pygame.draw.rect(screen, (230, 230, 230), (30, 115, 335, 98))
        pygame.draw.rect(screen, (230, 230, 230), (30, 215, 335, 98))
        pygame.draw.rect(screen, (230, 230, 230), (30, 315, 335, 98))

    screen.blit(slot_machine, (0, -40))
    current_balance_text = balance_font.render(str(balance), True, (230, 0, 0))
    screen.blit(current_balance_text, (600, 60))
    screen.blit(coins, (550, 70))

    # TODO: dynamic text aligment
    bet_amount_text = bet_amount_font.render("Bet: " + str(bet_amount), True, (0, 0, 0))
    screen.blit(bet_amount_text, (125, 515))

    for i in range(1, 6):
        fruitName = numToFruitName[i]
        image = fruitNameToImage[fruitName]
        image = pygame.transform.scale(image, (35, 35))
        screen.blit(image, (540, 164 + (i - 1) * 50))
        multipliers_text = multipliers_font.render("- x" + str(slot.symbols[i]), True, (230, 0, 0))
        screen.blit(multipliers_text, (590, 162 + (i - 1) * 50))

    totemImage = pygame.image.load("Assets/totem-full.png")
    totemImage = pygame.transform.scale(totemImage, (28, 84))
    screen.blit(totemImage, (545, 160 + (6 - 1) * 50))
    multipliers_text = multipliers_font.render("- x" + str(slot.symbols[6]), True, (230, 0, 0))
    screen.blit(multipliers_text, (590, 182 + (6 - 1) * 50))


def drawWin(strips, screen):
    winning_rows = []
    for i in range(3):
        if strips[0][i] == strips[1][i] and strips[1][i] == strips[2][i]:
            winning_rows.append(i)

    for row in winning_rows:
        for i in range(10):
            drawCanvas(row, True if i % 2 else False)
            drawOnSlot(screen, strips)
            clock.tick(10)
            pygame.display.update()


while run:
    drawCanvas()

    drawOnSlot(screen, strips)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonClicked(spinButton):
                if balance >= bet_amount:
                    balance -= bet_amount
                    i, j, k = slot.selectShifts()
                    animate(screen, strips, i - current_i + strip_len, j - current_j + strip_len,
                            k - current_k + strip_len)
                    current_i = i
                    current_j = j
                    current_k = k
                    strips = [slot.shift(slot.strip1, i), slot.shift(slot.strip2, j), slot.shift(slot.strip3, k)]
                    multi = slot.check(strips)
                    balance += multi * bet_amount

                    if multi > 0:
                        drawWin(strips, screen)

            elif buttonClicked(lower100Button):
                if bet_amount > 100:
                    bet_amount -= 100
            elif buttonClicked(lower10Button):
                if bet_amount > 10:
                    bet_amount -= 10
            elif buttonClicked(increase10Button):
                bet_amount += 10
            elif buttonClicked(increase100Button):
                bet_amount += 100

    n += 1

    pygame.display.update()

pygame.quit()
