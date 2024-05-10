import pygame
from pygame.locals import *
import sys

pygame.init()

screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Impossible XOs')
red = (255, 0, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
font = pygame.font.SysFont(None, 40)
menu_options = {'Versus': (screen_width // 2 - 40, screen_height // 3),
                'AI': (screen_width // 2 - 10, screen_height // 3 * 2)}
state = 'menu' 
clicked = False
markers = []
game_over = False
winner = 0
player = 1  
play_again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)
def reset_markers():
    global markers
    markers = [[0] * 3 for _ in range(3)]

reset_markers()

def reset_game():
    global markers, player, game_over, winner
    markers = [[0] * 3 for _ in range(3)]
    player = 1   
    game_over = False
    winner = 0
def draw_menu():
    screen.fill((0, 0, 0))
    for text, pos in menu_options.items():
        text_surf = font.render(text, True, blue)
        screen.blit(text_surf, pos)
def draw_board():
    bg = (0, 0, 0)
    grid = (200, 200, 200)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, 100 * x), (screen_width, 100 * x), line_width)
        pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
            if y == -1:
                pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def check_game_over():
    global game_over, winner
    for col in range(3):
        if markers[0][col] == markers[1][col] == markers[2][col] != 0:
            winner = markers[0][col]
            game_over = True
            return
        if markers[col][0] == markers[col][1] == markers[col][2] != 0:
            winner = markers[col][0]
            game_over = True
            return

    if markers[0][0] == markers[1][1] == markers[2][2] != 0:
        winner = markers[0][0]
        game_over = True
        return
    if markers[0][2] == markers[1][1] == markers[2][0] != 0:
        winner = markers[0][2]
        game_over = True
        return
    if all(marker != 0 for row in markers for marker in row):
        winner = 0
        game_over = True
        return


def draw_game_over(winner):
    if winner != 0:
        end_text = "Player " + ("1" if winner == 1 else "2") + " wins!"
    else:
        end_text = "Tie"

    end_img = font.render(end_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, play_again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))

def prompt_player_choice():
    screen.fill((0, 0, 0))  
    prompt_text = "   First or Second"
    prompt_img = font.render(prompt_text, True, blue)
    screen.blit(prompt_img, (20, screen_height // 2 - 20))
    pygame.display.update()
    choosing = True
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < screen_width // 2:  
                    return 1  
                else:
                    return -1  
def ai_move():
    global player, game_over
    if markers[1][1] == 0:
        markers[1][1] = player
        player *= -1   
        return

    opponent = -player  
    for i in range(3):
        for j in range(3):
            if markers[i][j] == 0:  
                markers[i][j] = opponent  
                check_game_over()
                if game_over:
                    markers[i][j] = player  
                    game_over = False  
                    player *= -1  
                    return
                markers[i][j] = 0 
    for i in range(3):
        for j in range(3):
            if markers[i][j] == 0:  
                markers[i][j] = player  
                check_game_over()
                if game_over:
                    return   
                markers[i][j] = 0  
    for i in range(3):
        for j in range(3):
            if markers[i][j] == 0:
                markers[i][j] = player
                player *= -1  
                return





run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if game_over:
                if play_again_rect.collidepoint(pos):
                    reset_game()
                    if state == 'ai':
                        player_choice = prompt_player_choice()  
                        if player_choice == -1:
                            player = -1
                            ai_move() 
                        else:
                            player = 1
            elif state == 'menu':
                for text, rect in menu_options.items():
                    if Rect(rect[0], rect[1], 150, 40).collidepoint(pos):
                        state = 'game' if text == 'Versus' else 'ai'
                        reset_game()
                        if state == 'ai':
                            player_choice = prompt_player_choice() 
                            if player_choice == -1:
                                player = -1
                                ai_move() 
                            else:
                                player = 1

            elif state in ['game', 'ai'] and not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell_x = pos[0] // 100
                    cell_y = pos[1] // 100
                    if markers[cell_x][cell_y] == 0:
                        markers[cell_x][cell_y] = player
                        check_game_over()
                        if not game_over:
                            player *= -1
                            if state == 'ai' and player == -1:
                                ai_move()
            
            if game_over:
                draw_game_over(winner)

    if state == 'menu':
        draw_menu()
    elif state in ['game', 'ai']:
        draw_board()
        draw_markers()
        if game_over:
            draw_game_over(winner)

    pygame.display.update()



    if state == 'menu':
        draw_menu()
    elif state in ['game', 'ai']:
        draw_board()
        draw_markers()
        if game_over:
            draw_game_over(winner)

    pygame.display.update()

pygame.quit()
