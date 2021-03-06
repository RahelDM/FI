# Clase Jugador
import pygame, random, Planeta2,Funciones, GameOver

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

#Crear un cuadrado (servir?? como base para el movimiento del personaje
cuadrado= pygame.Rect(90,470,40,40) # crear un rect??ngulo
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
pygame.display.set_caption("Space Maze") # A??adir nombre a la ventana de juego.
fondo=pygame.image.load("Planetas/Mapa1.png").convert()
bordes=pygame.image.load("Elementos/DecoracionMapa1.png").convert()
# Funci??n que elimina de la imagen el color pasado como par??metro.
bordes.set_colorkey(GRIS)
marcador=pygame.image.load("Elementos/Marcador.png").convert()
# Funci??n que elimina de la imagen el color pasado como par??metro.
marcador.set_colorkey(GRIS)
gameOverPantalla=pygame.image.load("Planetas/Mapa1GameOver.png").convert()

#Marcadorer necesarios para el recuento dde vidas y monedas.
monedas=0 # La cantidad incial ser?? de 0.
vidas=3 # La cantidad inicial ser?? de 3.

#Necesario para poner m??sica.
pygame.mixer.init()
pygame.mixer.music.set_volume(1) # Funci??n para controlar el volumen
muerteSonido= pygame.mixer.Sound("M??sica/Muerte.wav")
monedaSonido=pygame.mixer.Sound("M??sica/Moneda1.wav")
comidaSonido=pygame.mixer.Sound("M??sica/Comida.wav")
nivelCompletadoSonido=pygame.mixer.Sound("M??sica/NivelCompletado1.wav")
vidaSonido=pygame.mixer.Sound("M??sica/Vida.wav")
gameOverSonido=pygame.mixer.Sound("M??sica/GameOver1.wav")

#M??sica de fondo:
musicaFondo=pygame.mixer.Sound("M??sica/M??sica1.mp3") #Cargamos la m??sica.
musicaFondo.play() #Activamos la m??sica de fondo.

#Controlar los FPS
clock = pygame.time.Clock()

#Variable GAME_OVER
game_over=False

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


#        ---------- LISTAS ----------
"""
Utilizaremos las listas para almacenar nuestros sprites de forma ordenadas
,de esa manera, disminuiremos c??digo a la hora de representar los sprites en
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
pizza=Comida(430,160,"Elementos/Pizza.png")
listaComida.add(pizza)

#Moneda (creamos las 5 monedas) Cada una de ellas tendr?? un valor de 5 puntos.
# Les pasaremos como par??metros la posici??n (x,y) en la que estar?? situada.
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
allElementos.add(player) # A??adimos el jugador a la lista de elementos
allElementos.add(enemigoAzul)# A??adimos el jugador a la lista de elementos
allElementos.add(enemigoMorado)# A??adimos el jugador a la lista de elementos
# A??adimos las monedas a la lista de elementos
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
#A??adimos la comida a la lista de elementos:
allElementos.add(pizza)




#  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
#                     ---------- EVENTOS ----------


while not game_over:
    #Programaremos todos los eventos que se lleven a cabo en el juego:
    for event in pygame.event.get():
        print(event) #Imprimr en pantalla los eventos es ??til para conocer TODOS
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
    cuadrado.x+= velx
    cuadrado.y+= vely
     # Asignaremos la posici??n del cuadrado a la del jugador.
    player.rect.x= cuadrado.x
    player.rect.y=cuadrado.y

#  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
#                    ---------- COLISIONES ----------

    #Colisiones con las monedas:
    """ Llamando al m??todo spritecollide conseguimos que se produzca
    una colision entre el jugador (primer par??metro) y las monedas
    (todas ellas, ya que usamos para ello la listaMonedas).
    Si luego le damos el valor True la moneda desaparecer??.
    """
    colisionesMonedas= pygame.sprite.spritecollide(player,listaMonedas,True)
    if colisionesMonedas:
        monedas=monedas+5 # Cada moneda tendr?? el valor de 5 puntos.
        monedaSonido.play()
##        print(monedas) # Podemos imprimir la puntuaci??n de puntos.


  #Colisiones con los enemigos:
    """Llamando al m??todo spritecollide conseguimos que se produzca
    una colision entre el jugador (primer par??metro) y los enemigos
    (todos ellos, ya que usamos para ello la listaEnemigos).
    Si luego le damos el valor False el enemigo NO desaparecer??.
    """
    colisionesEnemigos= pygame.sprite.spritecollide(player,listaEnemigos,False)
    if colisionesEnemigos:
        cuadrado= pygame.Rect(90,470,40,40) #El jugador volver?? al punto inicial.
        vidas=vidas-1 # El marcador de las vidas disminuir??.
##        print(vidas) # Imprimimos las vidas restantes conforme se pierda una.
        muerteSonido.play()


      #Colisiones con la comida:
    """Llamando al m??todo spritecollide conseguimos que se produzca
    una colision entre el jugador (primer par??metro) y la comida
    (todos ellos, ya que usamos para ello la listaComida).
    Si luego le damos el valor True la comida desaparecer??.
    """

    if vidas!=3:
        colisionesComida= pygame.sprite.spritecollide(player,listaComida,True)
        if colisionesComida:
            vidas=vidas+1 # El marcador de las vidas aumentar??
            comidaSonido.play()
            vidaSonido.play()
    else:
        colisionesComida= pygame.sprite.spritecollide(player,listaComida,False)
        vidas=vidas

    #Colsiones contra los muros:
    #Recorremos cada cuadrado de la lista para comporbar las colisiones.
    """Llamando al m??todo colliderect y pasando como par??metro un muro de la
    listaMuros (estos son cuadrados base, sin imagen alguna, distintos que las
    paredes), podremos comprobar si el jugador (cuadrado) colisiona o no"""
    for muro in listaMuros:
         if cuadrado.colliderect(muro): # Si el jugador colisiona:
            cuadrado.x -= velx #Se producir?? una inversi??n de la velocidad
            cuadrado.y -= vely

    allElementos.update() # Llamando a este m??todo actualizamos todos los sprites


#  ---------- BUCLE PRINCIPAL PARA EL FUNCIONAMIENTO DEL JUEGO ----------
#                    ---------- ZONA DE DIBUJO ----------

    #Pantalla de Game Over
    if vidas!=0:
        pantalla.blit(fondo,[0,0])
    else:
        gameOverSonido.play()
        Funciones.gameOver()
    if monedas==50:
        Planeta2.planeta2()
    clock.tick(60)
    Funciones.dibujarMapa(pantalla,listaMuros)# Se dibujan los rect??ngulos en la pantalla

    #Con lo siguiente, dibujaremos encima de cada muro la pared correspondiente:
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro=="X": # Si la linea en mapa es una "X":
                pared.rect.x=x # Almacenamos las coordenadas de x
                pared.rect.y=y # Almacenamos las coordenadas de y
                listaPared.add(pared) # A??adimos una pared a la lista pared.
                listaPared.draw(pantalla) #Dibujamos la pared sobre el muro.
            x+=30
        x=0
        y+=30
    pantalla.blit(bordes,[0,0]) # Dibujamos tambi??n el decorado del planeta.
    pantalla.blit(marcador,[0,0]) # Por ??ltimo, dibujamos, en lo alto del nivel,
    # el marcador.

    #Dibujar los valores del marcador, para ello, llamamos a la funci??n texto:
    #Inficamos primero el lugar donde lo vamos a dibujar (en la pantalla),
    # despu??s el qu?? queremos dibujar, su tama??o, y posici??n.
    Funciones.texto(pantalla,(str(monedas))+" =",25,395,15)
    Funciones.texto(pantalla,(str(vidas))+" =",25,320,15)


    allElementos.draw(pantalla) #Dibujamos TODOS los elementos.
    pygame.display.flip()

pygame.quit()




