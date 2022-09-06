import pygame, os
from random import randint, randrange
pygame.init()

#tela e dimensões da tela
WIDTH = 720
HEIGHT = 770
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#FPS
FPS = 30

#relogio
CLOCK = pygame.time.Clock()

#cor da tela
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#paths dos diretorios
DIRETORIO_PRINCIPAL = os.path.dirname(__file__)
DIRETORIO_IMAGENS = os.path.join(DIRETORIO_PRINCIPAL, "imagens")
DIRETORIO_SONS = os.path.join(DIRETORIO_PRINCIPAL, "sons")
DIRETORIO_SPRITES = os.path.join(DIRETORIO_PRINCIPAL, "sprites")
DIRETORIO_FONTE = os.path.join(DIRETORIO_PRINCIPAL, "fonte")

#sprites
SPRITE_SHEET_BLUE = pygame.image.load(os.path.join(DIRETORIO_SPRITES, "spriteSheetAzul.png")).convert_alpha()
SPRITE_SHEET_RED = pygame.image.load(os.path.join(DIRETORIO_SPRITES, "spriteSheetVermelho.png")).convert_alpha()
SPRITE_SHEET_COIN = pygame.image.load(os.path.join(DIRETORIO_SPRITES, "spriteSheetCoin.png")).convert_alpha()
SPRITE_BOMB = pygame.image.load(os.path.join(DIRETORIO_SPRITES, "bomba.png")).convert_alpha()


#sons
SOUNDTRACK = pygame.mixer.Sound(os.path.join(DIRETORIO_SONS, "main_music.mp3"))
SOUNDTRACK_MENU = pygame.mixer.Sound(os.path.join(DIRETORIO_SONS, "title_music.mp3"))
SOUNDTRACK_GAMEOVER = pygame.mixer.Sound(os.path.join(DIRETORIO_SONS, "end_music.mp3"))
POINT_SOUND = pygame.mixer.Sound(os.path.join(DIRETORIO_SONS, 'smw_coin.wav'))
MENU_BLIP = pygame.mixer.Sound(os.path.join(DIRETORIO_SONS, "menu_blip.wav"))
BOOM = pygame.mixer.Sound(os.path.join(DIRETORIO_SONS, "boom.wav"))

#imagens
BACKGROUND = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, "background.png")).convert_alpha()
MENU_SCREEN = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, "telaInicial_CoinBattle.png")).convert_alpha()
MENU_SCREEN = pygame.transform.scale(MENU_SCREEN, (720, 770))
BLUE_WIN_SCREEN = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, "telaVitoriaAzul_CoinBattle.png")).convert_alpha()
BLUE_WIN_SCREEN = pygame.transform.scale(BLUE_WIN_SCREEN, (720, 770))
RED_WIN_SCREEN = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, "telaVitoriaVermelho_CoinBattle.png")).convert_alpha()
RED_WIN_SCREEN = pygame.transform.scale(RED_WIN_SCREEN, (720, 770))


#posição da moeda e obstaculo
X_COIN = randrange(100, WIDTH - 115)
Y_COIN = randrange(150, HEIGHT - 125)
X_BOMB = randrange(120, WIDTH - 115, 90)
Y_BOMB = randrange(120, HEIGHT - 125, 90)

#fonte dos textos
FONT_PONTUACAO = pygame.font.Font(os.path.join(DIRETORIO_FONTE, "Minecraft.ttf"), 30)
FONT = pygame.font.Font(os.path.join(DIRETORIO_FONTE, "Minecraft.ttf"), 20)

#pontos dos personagens
BLUE_POINTS = 0
RED_POINTS = 0

#game over
GAME_OVER = False

#menu
QUERO_JOGAR = False
