
import pygame, sys, time



#Clase para el control de mouse
class Cursor(pygame.Rect):
    #se crea un rectangulo pequeno
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    #obtiene la posicion del mouse y la guarda en la del rectangulo
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()




#-----Estados del juego
MENU_INICIAL=0
JUGAR=1
OPCIONES=2
SALIR=3
#----------------

def main():
    estadoJuego=MENU_INICIAL
    miCursor=Cursor()
    evento=True
    
    while 1:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)        
            if event.type == pygame.MOUSEBUTTONDOWN:                
                miCursor.update()
                                
                if estadoJuego == JUGAR and regresar_jugarRect.colliderect(miCursor):
                    estadoJuego= MENU_INICIAL
                    evento=True
                    break
                if estadoJuego == OPCIONES and regresar_opcionesRect.colliderect(miCursor):
                    estadoJuego = MENU_INICIAL
                    evento=True
                    break
                if estadoJuego == MENU_INICIAL and jugarRect.colliderect(miCursor):
                    estadoJuego= JUGAR
                    evento=True
                if estadoJuego == MENU_INICIAL and opcionesRect.colliderect(miCursor):
                    estadoJuego= OPCIONES
                    evento=True
                    break
                if estadoJuego == MENU_INICIAL and salirRect.colliderect(miCursor):                                            
                    sys.exit(0)
                    break

        if evento==True:           
            if estadoJuego == MENU_INICIAL:
                screen.fill(black)
                screen.blit(menuInicial,menuInicialRect)#agregamos a la pantalla la imagen y deacuerdo a su rectangulo                
                screen.blit(jugar,jugarRect)
                screen.blit(opciones, opcionesRect)
                screen.blit(salir,salirRect)                

            if estadoJuego == JUGAR:
                screen.fill(black)
                screen.blit(tablero,tableroRect)
                screen.blit(regresar_jugar,regresar_jugarRect)

            if estadoJuego == OPCIONES:
                screen.fill(black)
                screen.blit(menuOpciones,menuOpcionesRect)                
                screen.blit(regresar_opciones,regresar_opcionesRect)
                

            pygame.display.flip() #actualizamos la pantalla
            evento=False
    



pygame.init()

pygame.display.set_caption('Juego gato')

black = (0, 0, 0)
size =width,height= 1366, 643

screen=pygame.display.set_mode(size)


"""
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

"""



menuInicial = pygame.image.load("menuInicial.png")
menuOpciones = pygame.image.load("menuOpciones.png")
tablero=pygame.image.load("tablero.png")

jugar=pygame.image.load("jugar.png")
opciones=pygame.image.load("iconOpciones.png")
salir=pygame.image.load("salir.png")
regresar_jugar=pygame.image.load("regresar_jugando.png")
regresar_opciones=pygame.image.load("regresar_opciones.png")


#creamos los rectangulos de la imagenes, contienen X,Y,Width,Height
menuInicialRect = menuInicial.get_rect()
menuOpcionesRect = menuOpciones.get_rect()
tableroRect=tablero.get_rect()

jugarRect= jugar.get_rect()
jugarRect.top,jugarRect.left  = (300,900)

salirRect = salir.get_rect()
salirRect.top , salirRect.left = (500,900)

opcionesRect=opciones.get_rect()
opcionesRect.top , opcionesRect.left = (400, 900)

regresar_jugarRect = regresar_jugar.get_rect()
regresar_jugarRect.top , regresar_jugarRect.left = (550,1100)

regresar_opcionesRect=opciones.get_rect()
regresar_opcionesRect.top , regresar_opcionesRect.left =(550,900)



main()
            
        
