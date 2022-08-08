import pygame

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height + 100))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.update()
font = pygame.font.SysFont('Comic Sans MS', 50)
font2 = pygame.font.SysFont('Courier New', 100)
board = [' '] * 9
empty_board = board.copy()


def drawBoard():
    screen.fill((255, 255, 255))
    for i in range(4):
        pygame.draw.line(screen, (0, 0, 0), ((int)(i * width / 3), 100), ((int)(i * width / 3), height + 100))
        pygame.draw.line(screen, (0, 0, 0), (0, (int)(i * height / 3) + 100), (height, (int)(i * height / 3) + 100))


text = font.render("Current Turn:", False, (0, 0, 0))
currentTurn = 'o'
running = True
end = False


def is_playable(a):
    for i in range(9):
        if a[i] == ' ': return True
    return False


def is_win(a):
    for i in range(3):
        if a[i * 3] == a[i * 3 + 1] == a[i * 3 + 2] and a[i * 3] != ' ': return a[i * 3]
        if a[i] == a[i + 3] == a[i + 6] and a[i] != ' ': return a[i]
    if a[0] == a[4] == a[8] and a[1] != ' ': return a[0]
    if a[2] == a[4] == a[6] and a[2] != ' ': return a[2]
    return ' '


def getval(a, turn):
    values = []
    if is_win(a) == 'x':
        values.append(10)
    elif is_win(a) == 'o':
        values.append(-10)
    elif is_playable(a):
        for i in range(9):
            b = a.copy()
            if b[i] == ' ':
                b[i] = turn
                if turn == 'x':
                    next_turn = 'o'
                if turn == 'o':
                    next_turn = 'x'
                values.append(getval(b, next_turn))
    else:
        values.append(0)
    if turn == 'x': return max(values)
    if turn == 'o': return min(values)


def solve(a, turn):
    for i in range(9):
        if a[i] == ' ':
            b = a.copy()
            b[i] = turn
            if turn == 'x':
                next_turn = 'o'
            if turn == 'o':
                next_turn = 'x'
            if getval(a, turn) == getval(b, next_turn):
                return i
    return -1
game_turn='x'
won=False
while running:
    change = False
    if not end:
        drawBoard()
        turn_text = font2.render(currentTurn, False, (0, 0, 0))
        screen.blit(text, (0, 0))
        screen.blit(turn_text, (330, -20))
    else:
        if currentTurn == 'o' and won:
            winner_text = font.render("Player Won", True, (0, 0, 0), (240, 240, 240))
        elif currentTurn == 'x' and won:
            winner_text = font.render("AI won", True, (0, 0, 0), (240, 240, 240))
        elif not won:
            winner_text = font.render("tie", True, (0, 0, 0), (240, 240, 240))
        screen.blit(winner_text, (50, 180))
        pygame.display.update()
        pygame.time.delay(1000)
        end = False
        won = False
        currentTurn=game_turn
        if currentTurn== 'o':
            game_turn='x'
        else:
            game_turn='o'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            end = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click_x, click_y = int(mouse_x * 3 / width), int((mouse_y - 100) * 3 / height)
            if board[click_x + click_y * 3] == ' ' and mouse_y > 100:
                board[click_x + click_y * 3] = currentTurn
                change = True
    if currentTurn == 'x' and is_playable(board):
        board[solve(board, currentTurn)] = 'x'
        change = True
    for i in range(9):
        box_val_text = font2.render(board[i], False, (0, 0, 0))
        x = i % 3
        y = int(i / 3)
        screen.blit(box_val_text, (int(x * width / 3) + 30, int(y * width / 3) + 100))
    if is_win(board) != ' ':
        end = True
        change = False
        won = True
        board = empty_board.copy()
    if not is_playable(board):
        end = True
        board = empty_board.copy()
        change = False
    if change:
        if currentTurn == 'x':
            nextTurn = 'o'
        if currentTurn == 'o':
            nextTurn = 'x'
        currentTurn = nextTurn
    pygame.display.update()
