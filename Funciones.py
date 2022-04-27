
import pygame, random

#Definir colores
BLACK=(0,0,0)
WHITE= (255,255,255)
GREEN= (0,255,0)
RED= (255,0,0)
BLUE=(0,0,255)


#        ---------- FUNCIONES  ----------

def contruirMapa(mapa): # Creamos una lista de rectángulos a aprtir de una listaMuros "Mapa"
    """ Creamos una lista de rectángulos a partir de una listaMuros vacia"
    En esa lista se añadirán los cuadrados "Muros", sin imagen incluida.
    Leemos el "mapa" y, por cada "X" que haya, añadiremos un muro a la listaMuros.
    """
    murosLista=[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro =="X":
                murosLista.append(pygame.Rect(x,y,40,40))
            x+=30
        x=0
        y+=30
    return murosLista

def colocarMuro(superficie, rectangulo):
    """Con esta función lo que haremos será dibujar los muros
    con el color indicado"""
    pygame.draw.rect(superficie,BLUE, rectangulo)

def colocarMapa(superficie,murosLista):
    """ Dibujaremos en el mapa los muros y lo colocaremos en el mapa"""
    for muro in murosLista:
        colocarMuro(superficie,muro)

def texto(superficie, texto, tamaño, x, y):
    """ Función necesaria para insertar texto en nuestra pantalla de juego.
    Se utilizará principalmente para escribir en pantalla los valores
    de las vidas y de la puntuación del jugador"""
    font=pygame.font.SysFont("serif",tamaño)
    superficie_texto= font.render(texto, True, WHITE)
    texto_rect = superficie_texto.get_rect()
    texto_rect.midtop=(x,y)
    superficie.blit(superficie_texto,texto_rect)
def cuadrado(x,y):
    """Crear un cuadrado (servirá como base para el movimiento del personaje"""
    cuadrado= pygame.Rect(x,y,40,40) # crear un rectángulo
    return cuadrado


def ficheroPuntuacion(monedas,vidas,nombre):
    """Recibe como parámetro la variable monedas, la variables vidas, y el nombre del fichero.
    Escribe en un fichero la puntuación total del planeta"""
    f=open(str(nombre+".txt"),"w")
    pto=0
    for i in range(0,monedas):
        pto=pto+5
    f.write(str(nombre)+":"+'\n')
    f.write("Monedas recogidas: "+str(monedas)+ '\n' + "Vidas restantes: "+str(vidas)+ '\n' +"Puntos totales: "+str(pto))
    f.close()

def pantallaGameOver(monedas,vidas,nombre):
    #Controlar los FPS
    clock = pygame.time.Clock()
    ANCHO= 800
    ALTO= 600
    pantalla = pygame.display.set_mode((ANCHO,ALTO)) # Iniciarlizar la pantalla.
    pygame.display.set_caption("Space Maze") # Añadir nombre a la ventana de juego.
    gameOverPantalla=pygame.image.load("Planetas/SpaceMaze.png").convert()
    pantalla.blit(gameOverPantalla,[0,0])
    pygame.display.flip() # necesario para mostrar la pantalla
    # Controlamos los eventos
    true=True
    while true:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                true=False
                pygame.quit()
        clock.tick(60)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                true=False
            if event.key == pygame.K_p:
                ficheroPuntuacion(monedas,vidas,nombre)



