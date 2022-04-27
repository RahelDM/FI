import pygame, SpaceMaze


def gameOver():
    pygame.init() # Necesario para inicializar el juego

    #Definir medidas de la pantalla
    ANCHO= 800
    ALTO= 600
    pantalla = pygame.display.set_mode((ANCHO,ALTO)) # Iniciarlizar la pantalla
    pygame.display.set_caption("Space Maze") # Añadir nombre a la ventana de juego
    fondo=pygame.image.load("Planetas/Mapa1GameOver.png").convert()


    #Necesario para poner música.
    pygame.mixer.init()

    #Controlar los FPS
    clock = pygame.time.Clock()

    #Variable GAME_OVER
    game_over=False

    #Bucle fundamental para el buen funcionamiento del juego

    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over=True

    #-------- ZONA DE DIBUJO------------#
        pantalla.blit(fondo,[0,0])
        clock.tick(60)

        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_m]:
                import SpaceMaze

    #-------- ZONA DE DIBUJO------------#

        pygame.display.flip()
    pygame.quit()