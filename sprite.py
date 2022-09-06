import pygame, constantes
from random import randrange

class Blue(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.caminhar_direita_blue = []
        self.caminhar_esquerda_blue = []
        self.caminhar_cima_blue = []
        self.caminhar_baixo_blue = []
        for i in range(4):
            img = constantes.SPRITE_SHEET_BLUE.subsurface((i * 64, 128), (64, 64))
            self.caminhar_direita_blue.append(img)

            img = constantes.SPRITE_SHEET_BLUE.subsurface((i * 64, 64), (64, 64))
            self.caminhar_esquerda_blue.append(img)

            img = constantes.SPRITE_SHEET_BLUE.subsurface((i * 64, 192), (64, 64))
            self.caminhar_cima_blue.append(img)

            img = constantes.SPRITE_SHEET_BLUE.subsurface((i * 64, 0), (64, 64))
            self.caminhar_baixo_blue.append(img)

        self.index_lista = 0
        self.image = self.caminhar_direita_blue[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = 25
        self.rect.center = (100, 390)
        self.animar = False
        self.direcao = None

    def caminharParaDireita(self):
        self.animar = True
        self.direcao = "direita"

    def caminharParaEsquerda(self):
        self.animar = True
        self.direcao = "esquerda"

    def caminharParaCima(self):
        self.animar = True
        self.direcao = "cima"

    def caminharParaBaixo(self):
        self.animar = True
        self.direcao = "baixo"

    def update(self):
        if self.animar == True:
            self.index_lista += 0.2
            if self.index_lista > 4:
                self.animar = False
                self.index_lista = 0
            if self.direcao == "direita":
                self.image = self.caminhar_direita_blue[int(self.index_lista)]

            if self.direcao == "esquerda":
                self.image = self.caminhar_esquerda_blue[int(self.index_lista)]

            if self.direcao == "cima":
                self.image = self.caminhar_cima_blue[int(self.index_lista)]

            if self.direcao == "baixo":
                self.image = self.caminhar_baixo_blue[int(self.index_lista)]

        self.image = pygame.transform.scale(self.image, (64 * 1.2, 64 * 1.2))


class Red(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.caminhar_direita_red = []
        self.caminhar_esquerda_red = []
        self.caminhar_cima_red = []
        self.caminhar_baixo_red = []

        for i in range(4):
            img = constantes.SPRITE_SHEET_RED.subsurface((i * 64, 128), (64, 64))
            self.caminhar_direita_red.append(img)

            img = constantes.SPRITE_SHEET_RED.subsurface((i * 64, 64), (64, 64))
            self.caminhar_esquerda_red.append(img)

            img = constantes.SPRITE_SHEET_RED.subsurface((i * 64, 192), (64, 64))
            self.caminhar_cima_red.append(img)

            img = constantes.SPRITE_SHEET_RED.subsurface((i * 64, 0), (64, 64))
            self.caminhar_baixo_red.append(img)

        self.index_lista = 0
        self.image = self.caminhar_esquerda_red[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = 25
        self.rect.center = (constantes.WIDTH - 110, 390)
        self.animar = False
        self.direcao = None

    def caminharParaDireita(self):
        self.animar = True
        self.direcao = "direita"

    def caminharParaEsquerda(self):
        self.animar = True
        self.direcao = "esquerda"

    def caminharParaCima(self):
        self.animar = True
        self.direcao = "cima"

    def caminharParaBaixo(self):
        self.animar = True
        self.direcao = "baixo"

    def update(self):
        if self.animar == True:
            self.index_lista += 0.2
            if self.index_lista > 4:
                self.animar = False
                self.index_lista = 0
            if self.direcao == "direita":
                self.image = self.caminhar_direita_red[int(self.index_lista)]

            if self.direcao == "esquerda":
                self.image = self.caminhar_esquerda_red[int(self.index_lista)]

            if self.direcao == "cima":
                self.image = self.caminhar_cima_red[int(self.index_lista)]

            if self.direcao == "baixo":
                self.image = self.caminhar_baixo_red[int(self.index_lista)]

        self.image = pygame.transform.scale(self.image, (64 * 1.2, 64 * 1.2))


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.coin_girar = []
        for i in range(6):
            img = constantes.SPRITE_SHEET_COIN.subsurface((i * 200, 0), (200, 600))
            self.coin_girar.append(img)

        self.index_lista = 0
        self.image = self.coin_girar[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(pygame.transform.scale(self.image, (200 * 0.2, 600 * 0.2)))
        self.rect = (constantes.X_COIN, constantes.Y_COIN)

    def update(self):
        self.index_lista += 0.2
        self.image = self.coin_girar[int(self.index_lista)]
        if self.index_lista > 5:
            self.index_lista = 0
        self.image = pygame.transform.scale(self.image, (200 * 0.2, 600 * 0.2))


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = constantes.SPRITE_BOMB
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(pygame.transform.scale(self.image, (469 * 0.08, 523 * 0.08)))
        constantes.X_BOMB = randrange(120, constantes.WIDTH - 115, 90)
        constantes.Y_BOMB = randrange(120, constantes.HEIGHT - 125, 90)
        self.rect = (constantes.X_BOMB, constantes.Y_BOMB)
        if constantes.X_BOMB == constantes.X_COIN and constantes.Y_BOMB == constantes.Y_COIN:
            constantes.X_BOMB = randrange(120, constantes.WIDTH - 115, 90)
            constantes.Y_BOMB = randrange(120, constantes.HEIGHT - 125, 90)

    def update(self):
        self.image = pygame.transform.scale(self.image, (469 * 0.08, 523 * 0.08))

      