import sys, pygame, constantes, sprite
from random import randint, randrange
from sys import exit
from pygame import QUIT, KEYUP

pygame.init()

#nome do jogo
pygame.display.set_caption("Coin Battle")

#sons do jogo
pygame.mixer.Sound.play(constantes.SOUNDTRACK_MENU, -1)
constantes.SOUNDTRACK.set_volume(0.3)
constantes.SOUNDTRACK_MENU.set_volume(1)
constantes.SOUNDTRACK_GAMEOVER.set_volume(0.5)
constantes.POINT_SOUND.set_volume(1)
constantes.MENU_BLIP.set_volume(1)
constantes.BOOM.set_volume(1)

#sprites
todas_as_sprites = pygame.sprite.Group()
blue = sprite.Blue()
todas_as_sprites.add(blue)

red = sprite.Red()
todas_as_sprites.add(red)

moeda_sprite = pygame.sprite.Group()
coin = sprite.Coin()
moeda_sprite.add(coin)

bomb_sprite = pygame.sprite.Group()
bombs = []
for i in range(7):
    bomb = sprite.Bomb()
    bombs.append(bomb)
    bomb_sprite.add(bomb)


def menu():
    message_play = "PRESSIONE C PARA INICIAR"
    message_quit = "PRESSIONE ESC PARA SAIR"
    formatted_text_play = constantes.FONT.render(message_play, False,
                                                 constantes.WHITE)
    formatted_text_quit = constantes.FONT.render(message_quit, False,
                                                 constantes.WHITE)
    rect_text_play = formatted_text_play.get_rect()
    rect_text_quit = formatted_text_quit.get_rect()
    rect_text_play.center = (constantes.WIDTH // 2, constantes.HEIGHT - 250)
    rect_text_quit.center = (constantes.WIDTH // 2, constantes.HEIGHT - 200)
    constantes.SCREEN.fill(constantes.BLACK)
    constantes.SCREEN.blit(constantes.MENU_SCREEN, (0, 0))
    constantes.SCREEN.blit(formatted_text_play, rect_text_play)
    constantes.SCREEN.blit(formatted_text_quit, rect_text_quit)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYUP:
            if event.key == pygame.K_c:
                constantes.MENU_BLIP.play()
                pygame.time.delay(200)
                constantes.QUERO_JOGAR = True
            if event.key == pygame.K_ESCAPE:
                constantes.MENU_BLIP.play()
                pygame.time.delay(200)
                pygame.quit()
                exit()


def game_over():
    if constantes.BLUE_POINTS >= 5:
        win_screen = constantes.BLUE_WIN_SCREEN

    if constantes.RED_POINTS >= 5:
        win_screen = constantes.RED_WIN_SCREEN

    message_play = "PRESSIONE R PARA REINICIAR"
    message_quit = "PRESSIONE ESC PARA SAIR"
    formatted_text_play = constantes.FONT.render(message_play, False,
                                                 constantes.WHITE)
    formatted_text_quit = constantes.FONT.render(message_quit, False,
                                                 constantes.WHITE)
    rect_text_play = formatted_text_play.get_rect()
    rect_text_quit = formatted_text_quit.get_rect()
    rect_text_play.center = (constantes.WIDTH // 2, constantes.HEIGHT - 250)
    rect_text_quit.center = (constantes.WIDTH // 2, constantes.HEIGHT - 200)
    pygame.mixer.Sound.stop(constantes.SOUNDTRACK)
    pygame.time.delay(200)
    pygame.mixer.Sound.play(constantes.SOUNDTRACK_GAMEOVER, -1)
    constantes.GAME_OVER = True

    while constantes.GAME_OVER:
        constantes.SCREEN.fill(constantes.BLACK)
        constantes.SCREEN.blit(win_screen, (0, 0))
        constantes.SCREEN.blit(formatted_text_play, rect_text_play)
        constantes.SCREEN.blit(formatted_text_quit, rect_text_quit)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYUP:
                if event.key == pygame.K_r:
                    constantes.MENU_BLIP.play()
                    pygame.time.delay(200)
                    pygame.mixer.Sound.stop(constantes.SOUNDTRACK_GAMEOVER)
                    restart()

                if event.key == pygame.K_ESCAPE:
                    constantes.MENU_BLIP.play()
                    pygame.time.delay(200)
                    pygame.quit()
                    exit()


def restart():
    constantes.RED_POINTS = 0
    constantes.BLUE_POINTS = 0
    constantes.X_COIN = randint(100, constantes.WIDTH - 115)
    constantes.Y_COIN = randint(150, constantes.HEIGHT - 125)
    blue.animar = False
    blue.rect.center = (100, 390)
    blue.index_lista = 0
    blue.image = blue.caminhar_direita_blue[blue.index_lista]
    red.animar = False
    red.rect.center = (constantes.WIDTH - 110, 390)
    red.index_lista = 0
    red.image = red.caminhar_esquerda_red[red.index_lista]
    pygame.mixer.Sound.play(constantes.SOUNDTRACK, -1)
    constantes.GAME_OVER = False


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a] and blue.rect.left > 70:
        if pressed[pygame.K_d] or pressed[pygame.K_w] or pressed[pygame.K_s]:
            pass
        else:
            blue.caminharParaEsquerda()
            blue.rect = blue.rect.move(-5, 0)

    if pressed[pygame.K_d] and blue.rect.right < constantes.WIDTH - 90:
        if pressed[pygame.K_a] or pressed[pygame.K_w] or pressed[pygame.K_s]:
            pass
        else:
            blue.caminharParaDireita()
            blue.rect = blue.rect.move(5, 0)

    if pressed[pygame.K_w] and blue.rect.top > 110:
        if pressed[pygame.K_d] or pressed[pygame.K_a] or pressed[pygame.K_s]:
            pass
        else:
            blue.caminharParaCima()
            blue.rect = blue.rect.move(0, -5)

    if pressed[pygame.K_s] and blue.rect.bottom < constantes.HEIGHT - 110:
        if pressed[pygame.K_d] or pressed[pygame.K_w] or pressed[pygame.K_a]:
            pass
        else:
            blue.caminharParaBaixo()
            blue.rect = blue.rect.move(0, 5)

    if pressed[pygame.K_j] and red.rect.left > 73:
        if pressed[pygame.K_l] or pressed[pygame.K_i] or pressed[pygame.K_k]:
            pass
        else:
            red.caminharParaEsquerda()
            red.rect = red.rect.move(-5, 0)

    if pressed[pygame.K_l] and red.rect.right < constantes.WIDTH - 85:
        if pressed[pygame.K_j] or pressed[pygame.K_i] or pressed[pygame.K_k]:
            pass
        else:
            red.caminharParaDireita()
            red.rect = red.rect.move(5, 0)

    if pressed[pygame.K_i] and red.rect.top > 110:
        if pressed[pygame.K_l] or pressed[pygame.K_j] or pressed[pygame.K_k]:
            pass
        else:
            red.caminharParaCima()
            red.rect = red.rect.move(0, -5)

    if pressed[pygame.K_k] and red.rect.bottom < constantes.HEIGHT - 110:
        if pressed[pygame.K_l] or pressed[pygame.K_i] or pressed[pygame.K_j]:
            pass
        else:
            red.caminharParaBaixo()
            red.rect = red.rect.move(0, 5)


def coin_position():
    if colisao_blue:
        constantes.BLUE_POINTS += 1
    if colisao_red:
        constantes.RED_POINTS += 1
    constantes.POINT_SOUND.play()
    constantes.X_COIN = randint(100, constantes.WIDTH - 115)
    constantes.Y_COIN = randint(150, constantes.HEIGHT - 125)
    coin.rect = (constantes.X_COIN, constantes.Y_COIN)


def bomb_position():
    if colisao_bomb_blue:
        if constantes.BLUE_POINTS > 0:
            constantes.BLUE_POINTS -= 1
        constantes.BOOM.play()
        blue.animar = False
        blue.rect.center = (100, 390)
        blue.index_lista = 0
        blue.image = blue.caminhar_direita_blue[blue.index_lista]
        pygame.time.delay(100)

    if colisao_bomb_red:
        if constantes.RED_POINTS > 0:
            constantes.RED_POINTS -= 1
        constantes.BOOM.play()
        red.animar = False
        red.rect.center = (constantes.WIDTH - 110, 390)
        red.index_lista = 0
        red.image = red.caminhar_esquerda_red[red.index_lista]
        pygame.time.delay(100)

    constantes.X_BOMB = randrange(120, constantes.WIDTH - 115, 90)
    constantes.Y_BOMB = randrange(120, constantes.HEIGHT - 125, 90)
    bombs[i].rect = (constantes.X_BOMB, constantes.Y_BOMB)


def atualizar():
    constantes.CLOCK.tick(30)
    constantes.SCREEN.fill(constantes.BLACK)
    constantes.SCREEN.blit(constantes.BACKGROUND, (0, constantes.HEIGHT - 720))
    constantes.SCREEN.blit(formatted_text_blue, (80, 10))
    constantes.SCREEN.blit(formatted_text_red, (380, 10))
    bomb_sprite.draw(constantes.SCREEN)
    todas_as_sprites.draw(constantes.SCREEN)
    moeda_sprite.draw(constantes.SCREEN)
    todas_as_sprites.update()
    moeda_sprite.update()
    bomb_sprite.update()
    pygame.display.flip()


while constantes.QUERO_JOGAR == False:
    menu()

pygame.mixer.Sound.stop(constantes.SOUNDTRACK_MENU)
pygame.mixer.Sound.play(constantes.SOUNDTRACK, -1)

while True:
    message_blue = f"Pontos Azul: {constantes.BLUE_POINTS}"
    formatted_text_blue = constantes.FONT_PONTUACAO.render(
        message_blue, False, constantes.WHITE)
    message_red = f"Pontos Vermelho: {constantes.RED_POINTS}"
    formatted_text_red = constantes.FONT_PONTUACAO.render(
        message_red, False, constantes.WHITE)
    events()

    colisao_blue = pygame.sprite.collide_mask(blue, coin)
    colisao_red = pygame.sprite.collide_mask(red, coin)

    if colisao_red or colisao_blue:
        coin_position()

    for i in range(7):
        colisao_bomb_blue = pygame.sprite.collide_mask(blue, bombs[i])
        colisao_bomb_red = pygame.sprite.collide_mask(red, bombs[i])

        if colisao_bomb_blue or colisao_bomb_red:
            bomb_position()

    if constantes.BLUE_POINTS >= 5 or constantes.RED_POINTS >= 5:
        game_over()

    atualizar()
