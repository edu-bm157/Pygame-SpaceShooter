from pygame import*
from random import randint
mixer.init()
font.init()

ancho_ventana = 800
alto_ventana = 900
#Creación de ventana

ventana = display.set_mode((ancho_ventana, alto_ventana))
display.set_caption("Space Shooter")

class Figura(sprite.Sprite):
    def __init__(self, ancho = 0, alto = 0, posicion_x = 0, posicion_y = 0, imagen = "", velocidad = 0):
        sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.alto = alto
        self.image = transform.scale(image.load(imagen), (self.ancho, self.alto))
        self.rect = self.image.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y
        self.velocidad = velocidad

    def dibujarFigura(self):
        ventana.blit(self.image,(self.rect.x, self.rect.y))

class PersonajePrincipal(Figura):

    def movimiento(self):
        keys = key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.rect.x -= self.velocidad
        elif keys[K_RIGHT] or keys[K_d]:
            self.rect.x += self.velocidad

    def disparar(self):
        objetivo_x, objetivo_y = mouse.get_pos()
        bala = Bala(15, 30,self.rect.centerx, self.rect.top, "Bala.png", 15,objetivo_x, objetivo_y)
        balas.add(bala)

    def aumentarPuntaje():
        puntaje += 1

    def colision(self,naves):
        for n in naves:
            if sprite.collide_rect(self,n):
                run = False

class Bala(Figura):
    def __init__(self, ancho, alto, posicion_x, posicion_y, imagen, velocidad, objetivo_x, objetivo_y):
        super().__init__(ancho, alto, posicion_x, posicion_y, imagen, velocidad)

        direccion_x = objetivo_x - posicion_x
        direccion_y = objetivo_y - posicion_y

        distancia = (direccion_x ** 2 + direccion_y ** 2)**0.5
        self.velocidad_x = (direccion_x / distancia) * velocidad
        self.velocidad_y = (direccion_y / distancia) * velocidad

    def mover_arriba(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

class Enemigo(Figura):
    def movimiento(self):
        self.rect.y += self.velocidad
        if self.rect.y > alto_ventana + 10:
            pass

class Fuentes():
    def __init__(self, fuente, tamano, color):
        self.fuente = font.SysFont(fuente, tamano)
        self.color = color

    def renderizarTexto(self, texto, x, y):
        self.texto =self.fuente.render(texto, True, self.color)
        ventana.blit(self.texto, (x, y))

#Configuración necesaria para hacer funcionar el juego
run = True #Control de ciclo de juego
clock = time.Clock() #Control de fps en el juego
puntaje = 0
yellow = (224, 178, 49)
white = (255, 255, 255) 
Nave = PersonajePrincipal(80,80, ancho_ventana//2, 800, "NaveDeCombate.png", 10)
Fondo = transform.scale(image.load("Fondo.jpg"),(ancho_ventana, alto_ventana))
balas = sprite.Group()
enemigos = sprite.Group()
cantidad_de_enemigos = 6
vida = 100
for i in range(cantidad_de_enemigos + 1):
    enemigo = Enemigo(90, 90,randint(50, ancho_ventana-50), 0, "Monstruo.png", randint(1,5))
    enemigos.add(enemigo)
puntaje_texto = Fuentes("Impact", 30, yellow)
vida_texto = Fuentes("Impact", 30, yellow)

titulo_de_juego = Fuentes("Impact",80 , (255,255,255), )
boton_iniciar = Fuentes("Impact", 50 , (255,255,255), )

iniciar_juego = False

#Ciclo de juego
while run:
    for e in event.get():
            if e.type == QUIT:
                run = False
    if not iniciar_juego:
        ventana.blit(Fondo, (0,0))
        titulo_de_juego.renderizarTexto("SPACE-SHOOTER", ancho_ventana//2 - 300, alto_ventana // 2 - 100)
        boton_iniciar.renderizarTexto("START", ancho_ventana//2 - 300,alto_ventana //2 + 100)
        if boton_iniciar.texto.get_rect().collidepoint(mouse.get_pos()):
            if mouse.get_pressed()[0]:
                iniciar_juego = True
    else:      
        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    Nave.disparar()
        ventana.blit(Fondo, (0,0))
        puntaje_texto.renderizarTexto(f"Puntaje: {puntaje}", 10,10)
        vida_texto.renderizarTexto(f"Vida: {vida}", ancho_ventana - 200, 10)
        Nave.dibujarFigura()
        Nave.movimiento()
        #Dibujo de balas y movimiento en Y
        balas.draw(ventana)
        enemigos.draw(ventana)  
        for e in enemigos:
            e.movimiento()
            if e.rect.y > alto_ventana + 10:
                vida -= 10
                enemigos.remove(e)
                enemigo = Enemigo(90, 90,randint(50, ancho_ventana-50), 60, "Monstruo.png", randint(3,5))
        enemigos.add(enemigo)

        for b in balas:
            b.mover_arriba() 
            if b.rect.y < -10:
                balas.remove(b)
            if sprite.spritecollide(b, enemigos, True): 
                enemigo = Enemigo(90, 90,randint(50, ancho_ventana-50),0,"Monstruo.png", randint(3,5))
                enemigos.add(enemigo)
                balas.remove(b)
                puntaje += 10
        #Detección de colisiones entre el personaje y los enemigos
        if sprite.spritecollide(Nave, enemigos, True):
            vida -= 10
            #enemigos.remove(e)
            enemigo = Enemigo(90, 90,randint(50, ancho_ventana-50),0,"Monstruo.png", randint(3,5))
            enemigos.add(enemigo)
            print(vida)
        if vida <= 0:
            run = False

    clock.tick(60)
    display.update()