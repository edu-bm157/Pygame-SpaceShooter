import pygame

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
shift = 0
background_speed = 0

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

class Objeto(pygame.sprite.Sprite):
    def __init__(self, posicion_x:int=0,posicion_y:int=0,ancho:int=0, alto:int=0,imagen:str="",velocidad:int=0):
        super().__init__()
    
        self.image = pygame.transform.scale(pygame.image.load(imagen),(ancho,alto))
        self.rect = self.image.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y
        self.velocidad = velocidad
    
    def dibujar(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))

class Jugador(Objeto):
    def __init__(self, posicion_x:int=0, posicion_y:int=0, ancho:int=0, alto:int=0, imagen:str="", velocidad:int=0):
        super().__init__(posicion_x, posicion_y, ancho, alto, imagen, velocidad)
        self.contador_salto = 2  # Inicializamos el contador de saltos

    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocidad
            background_speed = -5
        if not keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            background_speed = 0

    def gravedad(self, plataformas):
        gravedad = 5
        self.rect.y += gravedad
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                self.rect.y = plataforma.rect.top - self.rect.height
                self.contador_salto = 2  # Reiniciamos el contador al tocar una plataforma
                break

    def saltar(self):
        if self.contador_salto > 0:  # Verificamos si aún puede saltar
            self.rect.y -= 100
            self.contador_salto -= 1  # Reducimos el contador de saltos
            self.gravedad([])

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, posicion_x:int=0,posicion_y:int=0,ancho:int=0, alto:int=0,color:tuple = (0,0,0)):#Con color
        super().__init__()
        self.image = pygame.Surface((ancho,alto))
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = posicion_x
        self.rect.y = posicion_y

    def crear_plataforma(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))

reloj = pygame.time.Clock()
run = True

jugador = Jugador(0,0,60,60, "Arcade/Personaje.png",5)

#Plataformas
plataformas = pygame.sprite.Group() #

plataforma1 = Plataforma(0, 100, 200, 5, (151, 121, 22))
plataforma2 = Plataforma(400,200,200,5, (255, 0, 0))
plataforma3 = Plataforma(0, 600, ANCHO_VENTANA*5, 5, (255,0,0))
plataformas.add(plataforma1) #
plataformas.add(plataforma2)
plataformas.add(plataforma3)
fondo = pygame.transform.scale(pygame.image.load("Arcade/Fondo.jpg"),(ANCHO_VENTANA,ALTO_VENTANA))
contador_salto = 2

while run:
    shift += background_speed
    local_shift = shift % ANCHO_VENTANA
    ventana.blit(fondo, (local_shift,0))
    if local_shift != 0:
        ventana.blit(fondo, (local_shift - ANCHO_VENTANA,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jugador.saltar()
    borde_izquierdo = ANCHO_VENTANA/40
    borde_derecho = ANCHO_VENTANA - 8 * borde_izquierdo
    if jugador.rect.x > borde_derecho:
        jugador.rect.x = borde_derecho
        shift -= jugador.velocidad*1.5
    elif jugador.rect.x < borde_izquierdo:
        jugador.rect.x = borde_izquierdo
        shift += jugador.velocidad*1.5
    jugador.dibujar()
    jugador.mover()

    jugador.gravedad(plataformas)
    for plataforma in plataformas:
        plataforma.crear_plataforma()
    pygame.display.update()
    reloj.tick(60)