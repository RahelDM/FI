# Clase Jugador
import pygame, Funciones

pygame.init() # Necesario para inicializar el juego

#        ---------- CLASES DEL JUEGO ----------

"""                    CLASE JUGADOR                   """
# Clase Jugador.
class Player(pygame.sprite.Sprite): # Cargamos imagen sprite
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("Elementos/Jugador.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect() #convertirlo en un cuadrado
    def update(self):
        #Limites derechos e izquierdos del mapa
        if self.rect.right > 750:
            self.rect.right = 750
        if self.rect.left < 25:
            self.rect.left = 25
        #limites inferiores y superiores del mapa
        if  self.rect.top<30:
            self.rect.top=30
        elif self.rect.top>510:
             self.rect.top=510

"""                    CLASES ENEMIGOS                   """

# Clase Enemigo Azul (una clase aparte para casa enemigo)
class EnemigoAzul(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("Elementos/EnemigoAzulBlanco.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.centerx= 248
        self.rect.bottom= 242
        self.speedX= -1
    def update(self):
        self.rect.x += self.speedX
        if  self.rect.left <70:
            self.speedX= 1
        if self.rect.right>280:
             self.speedX= -1
class EnemigoMorado(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("Elementos/EnemigoMoradoBlanco.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.centerx=600
        self.rect.bottom= 450
        self.speedY= -1
    def update(self):
        self.rect.y += self.speedY
        if  self.rect.top<220:
            self.speedY= 1
        elif self.rect.top>400:
             self.speedY= -1

"""                    CLASE PARED                   """

class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Elementos/RocaMapa1.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()

"""                    CLASE MONEDA                   """

class Moneda(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("Elementos/Moneda.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.centerx= x # Centro del objeto

"""                    CLASE COMIDA                   """

class Comida(pygame.sprite.Sprite):
    def __init__(self,x,y,imagen):
        super().__init__()
        self.image=pygame.image.load(imagen).convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.centerx=x # Centro del objeto


#        ---------- VARIABLES ----------

#Definir medidas de la pantalla
ANCHO= 800
ALTO= 600

#Crear un cuadrado (servirá como base para el movimiento del personaje
cuadrado= pygame.Rect(90,470,15,15) # crear un rectángulo
x=0
y=0
velx=0 # velocidad inicial en las x del cuadrado
vely=0 # velocidad inicial en las y del cuadrado

#Definir colores
BLACK=(0,0,0)
WHITE= (255,255,255)
GREEN= (0,255,0)
RED= (255,0,0)
BLUE=(0,0,255)
BLUEGREEN=(0,187,194)
GRIS=(129,132,136)

# Creamos la ventana, sus ajustes y las respectivas imagenes que necesitaremos

pantalla = pygame.display.set_mode((ANCHO,ALTO)) # Iniciarlizar la pantalla.
pygame.display.set_caption("Space Maze") # Añadir nombre a la ventana de juego.
fondo=pygame.image.load("Planetas/Mapa1.png").convert()
bordes=pygame.image.load("Elementos/DecoracionMapa1.png").convert()
# Función que elimina de la imagen el color pasado como parámetro.
bordes.set_colorkey(GRIS)
marcador=pygame.image.load("Elementos/Marcador.png").convert()
# Función que elimina de la imagen el color pasado como parámetro.
marcador.set_colorkey(GRIS)

#Necesario para poner música.
pygame.mixer.init()
pygame.mixer.music.set_volume(1) # Función para controlar el volumen
muerteSonido= pygame.mixer.Sound("Música/Muerte.wav")
monedaSonido=pygame.mixer.Sound("Música/Moneda1.wav")
comidaSonido=pygame.mixer.Sound("Música/Comida.wav")
nivelCompletadoSonido=pygame.mixer.Sound("Música/NivelCompletado1.wav")
vidaSonido=pygame.mixer.Sound("Música/Vida.wav")
gameOverSonido=pygame.mixer.Sound("Música/GameOver1.wav")

#Música de fondo:
musicaFondo=pygame.mixer.Sound("Música/Música2.mp3") #Cargamos la música.
musicaFondo.play() #Activamos la música de fondo.


#Controlar los FPS
clock = pygame.time.Clock()

#Variable GAME_OVER
game_over=True
start=True

# Creamos la estructura del mapa que utilizaremos en el laberinto. Cada "X" es
# un bloque a construir :
mapa = [

    "                        ",
    " XXXXXXXXXXXXXXXXXXXXXXX",
    " X          XX     XX  X",
    " X         XXX     XX  X",
    " XXXXXX   XXXXXXX  XX  X",
    " X       XXXX  X   XX  X",
    " X             X   XX  X",
    " X                     X",
    " XXXXXXXXX             X",
    " X      XX       X     X",
    " X      XX    X  X   XXX",
    " X  XXXXXX    X  X     X",
    " X            X  X     X",
    " X            X  X   XXX",
    " XXXXXXXXXXX  XXXX     X",
    " X            XXXX     X",
    " X            XXXX   XXX",
    " XXXXXXXXXXXXXXXXXXXXXXX",

]


#  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
#                     ---------- EVENTOS ----------


while start:
    if game_over:

  #Marcadores necesarios para el recuento de vidas y monedas.
        monedas=0 # La cantidad incial será de 0.
        vidas=3 # La cantidad inicial será de 3.

        Funciones.pantallaGameOver(monedas,vidas,"Planeta1")
        game_over=False


        #  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
        #        ---------- LISTAS ----------
        """
        Utilizaremos las listas para almacenar nuestros sprites de forma ordenadas
        ,de esa manera, disminuiremos código a la hora de representar los sprites en
        la pantalla. Guardaremos TODOS en una lista llamada "allElementos"

        """
        #Paredes
        listaPared= pygame.sprite.Group()
        pared=Pared()
        listaPared.add(pared)
        listaMuros= Funciones.contruirMapa(mapa)

        #Jugador
        player= pygame.sprite.Group()
        player=Player()

        #Enemigos
        listaEnemigos=pygame.sprite.Group()
        enemigoAzul= EnemigoAzul()
        enemigoMorado= EnemigoMorado()
        listaEnemigos.add(enemigoAzul)
        listaEnemigos.add(enemigoMorado)

        #Comida (pizza y donuts)
        listaComida=pygame.sprite.Group()
        pizza=Comida(430,170,"Elementos/Pizza.png")
        listaComida.add(pizza)

        #Moneda (creamos las 5 monedas) Cada una de ellas tendrá un valor de 5 puntos.
        # Les pasaremos como parámetros la posición (x,y) en la que estará situada.
        moneda1=Moneda(100,200)
        moneda2=Moneda(190,200)
        moneda3=Moneda(460,75)
        moneda4=Moneda(100,75)
        moneda5=Moneda(220,285)
        moneda6=Moneda(490,375)
        moneda7=Moneda(670,345)
        moneda8=Moneda(670,75)
        moneda9=Moneda(670,440)
        moneda10=Moneda(593,460)
        listaMonedas= pygame.sprite.Group()
        listaMonedas.add(moneda1)
        listaMonedas.add(moneda2)
        listaMonedas.add(moneda3)
        listaMonedas.add(moneda4)
        listaMonedas.add(moneda5)
        listaMonedas.add(moneda6)
        listaMonedas.add(moneda7)
        listaMonedas.add(moneda8)
        listaMonedas.add(moneda9)
        listaMonedas.add(moneda10)

        # Introducimos en "allElementos" todos los elementos (sprites) del juego.
        allElementos= pygame.sprite.Group()
        allElementos.add(player) # Añadimos el jugador a la lista de elementos
        allElementos.add(enemigoAzul)# Añadimos el jugador a la lista de elementos
        allElementos.add(enemigoMorado)# Añadimos el jugador a la lista de elementos
        # Añadimos las monedas a la lista de elementos
        allElementos.add(moneda1)
        allElementos.add(moneda2)
        allElementos.add(moneda3)
        allElementos.add(moneda4)
        allElementos.add(moneda5)
        allElementos.add(moneda6)
        allElementos.add(moneda7)
        allElementos.add(moneda8)
        allElementos.add(moneda9)
        allElementos.add(moneda10)
        #Añadimos la comida a la lista de elementos:
        allElementos.add(pizza)


    #Programaremos todos los eventos que se lleven a cabo en el juego:
    for event in pygame.event.get():
        print(event) #Imprimr en pantalla los eventos es útil para conocer TODOS
    # lo que ocurre en el juego.
        if event.type == pygame.QUIT:
            game_over=True
        #Movimiento del personaje:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velx=-3
            elif event.key == pygame.K_RIGHT:
                velx=3
            elif event.key == pygame.K_UP:
                vely=-3
            elif event.key == pygame.K_DOWN:
                vely=3
        else:
            velx=0
            vely=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_p]:
                Funciones.ficheroPuntuacion(monedas,vidas,"Planeta1")

    cuadrado.x+= velx
    cuadrado.y+= vely
     # Asignaremos la posición del cuadrado a la del jugador.
    player.rect.x= cuadrado.x
    player.rect.y=cuadrado.y

#  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
#                    ---------- COLISIONES ----------

    #Colisiones con las monedas:
    """ Llamando al método spritecollide conseguimos que se produzca
    una colision entre el jugador (primer parámetro) y las monedas
    (todas ellas, ya que usamos para ello la listaMonedas).
    Si luego le damos el valor True la moneda desaparecerá.
    """
    colisionesMonedas= pygame.sprite.spritecollide(player,listaMonedas,True)
    if colisionesMonedas:
        monedas=monedas+1 # Cada moneda tendrá el valor de 5 puntos.
        monedaSonido.play()
##        print(monedas) # Podemos imprimir la puntuación de puntos.


  #Colisiones con los enemigos:
    """Llamando al método spritecollide conseguimos que se produzca
    una colision entre el jugador (primer parámetro) y los enemigos
    (todos ellos, ya que usamos para ello la listaEnemigos).
    Si luego le damos el valor False el enemigo NO desaparecerá.
    """
    colisionesEnemigos= pygame.sprite.spritecollide(player,listaEnemigos,False)
    if colisionesEnemigos:
        cuadrado= pygame.Rect(90,470,40,40) #El jugador volverá al punto inicial.
        vidas=vidas-1 # El marcador de las vidas disminuirá.
##        print(vidas) # Imprimimos las vidas restantes conforme se pierda una.
        muerteSonido.play()


      #Colisiones con la comida:
    """Llamando al método spritecollide conseguimos que se produzca
    una colision entre el jugador (primer parámetro) y la comida
    (todos ellos, ya que usamos para ello la listaComida).
    Si luego le damos el valor True la comida desaparecerá.
    """

    if vidas!=3:
        colisionesComida= pygame.sprite.spritecollide(player,listaComida,True)
        if colisionesComida:
            vidas=vidas+1 # El marcador de las vidas aumentará
            comidaSonido.play()
            vidaSonido.play()
    else:
        colisionesComida= pygame.sprite.spritecollide(player,listaComida,False)
        vidas=vidas

    #Colsiones contra los muros:
    #Recorremos cada cuadrado de la lista para comporbar las colisiones.
    """Llamando al método colliderect y pasando como parámetro un muro de la
    listaMuros (estos son cuadrados base, sin imagen alguna, distintos que las
    paredes), podremos comprobar si el jugador (cuadrado) colisiona o no"""
    for muro in listaMuros:
         if cuadrado.colliderect(muro): # Si el jugador colisiona:
            cuadrado.x -= velx #Se producirá una inversión de la velocidad
            cuadrado.y -= vely

    allElementos.update() # Llamando a este método actualizamos todos los sprites


#  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
#                    ---------- ZONA DE DIBUJO ----------

    #Pantalla de Game Over
    if vidas!=0:
        pantalla.blit(fondo,[0,0])
    else:
        game_over=True
        gameOverSonido.play()
    if monedas==10:
        import Planeta2


    clock.tick(60)
    Funciones.colocarMapa(pantalla,listaMuros)# Se dibujan los rectángulos en la pantalla

    #Con lo siguiente, dibujaremos encima de cada muro la pared correspondiente:
    posX=0
    posY=0
    for fila in mapa:
        for muro in fila:
            if muro=="X": # Si la linea en mapa es una "X":
                pared.rect.x=posX # Almacenamos las coordenadas de x
                pared.rect.y=posY # Almacenamos las coordenadas de y
                listaPared.add(pared) # Añadimos una pared a la lista pared.
                listaPared.draw(pantalla) #Dibujamos la pared sobre el muro.
            posX+=30
        posX=0
        posY+=30
    pantalla.blit(bordes,[0,0]) # Dibujamos también el decorado del planeta.
    pantalla.blit(marcador,[0,0]) # Por último, dibujamos, en lo alto del nivel,
    # el marcador.

    #Dibujar los valores del marcador, para ello, llamamos a la función texto:
    #Inficamos primero el lugar donde lo vamos a dibujar (en la pantalla),
    # después el qué queremos dibujar, su tamaño, y posición.
    Funciones.texto(pantalla,(str(monedas))+" =",25,395,15)
    Funciones.texto(pantalla,(str(vidas))+" =",25,320,15)


    allElementos.draw(pantalla) #Dibujamos TODOS los elementos.
    pygame.display.flip()

pygame.quit()




