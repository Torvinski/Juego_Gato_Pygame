
import pygame, sys, time



#Clase para el control de mouse
class Cursor(pygame.Rect):
    #se crea un rectangulo pequeno
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    #obtiene la posicion del mouse y la guarda en la del rectangulo
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()


#Clase boton para los menus        
class Kasilla(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,imagen3,x=200,y=200):
        self.imagen_vacia =imagen1
        self.imagen_X = imagen2
        self.imagen_O = imagen3
        self.imagen_actual = self.imagen_vacia
        self.rect = self.imagen_vacia.get_rect()
        self.rect.left,self.rect.top = x,y


    def setImagenVacia(self,pantalla):
        self.imagen_actual=self.imagen_vacia
        pantalla.blit(self.imagen_actual,self.rect)
        

    def setImagenX(self,pantalla):
        self.imagen_actual=self.imagen_X
        pantalla.blit(self.imagen_actual,self.rect)

    def setImagenO(self,pantalla):
        self.imagen_actual=self.imagen_O
        pantalla.blit(self.imagen_actual,self.rect)
        
"""    
    def update(self,pantalla,cursor):
        #si colisiona con el cursor se cambia de imagen
        if cursor.colliderect(self.rect):
            self.imagen_actual =self.imagen_selec
        else:
            self.imagen_actual =self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)  """




#-----Estados del juego
MENU_INICIAL=0
MENU_TURNO=1
JUGAR=2
OPCIONES=3
SALIR=4
#-----Turnos
MAQUINA=0
HUMANO=1

#----------


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

                if estadoJuego == MENU_INICIAL and jugarRect.colliderect(miCursor):
                    estadoJuego= MENU_TURNO
                    evento=True
                    break
                
                if estadoJuego == MENU_INICIAL and opcionesRect.colliderect(miCursor):
                    estadoJuego= OPCIONES
                    evento=True
                    break
                
                if estadoJuego == MENU_INICIAL and salirRect.colliderect(miCursor):                                            
                    sys.exit(0)
                    break

                if estadoJuego == MENU_TURNO and maquinaRect.colliderect(miCursor):
                    estadoJuego=JUGAR
                    turno=MAQUINA
                    evento=True
                    break

                if estadoJuego == MENU_TURNO and humanoRect.colliderect(miCursor):
                    estadoJuego=JUGAR
                    turno=HUMANO
                    evento=True
                    break

                if estadoJuego== MENU_TURNO and regresar_menuTurnoRect.colliderect(miCursor):
                    estadoJuego=MENU_INICIAL
                    evento=True
                    break
                
                if estadoJuego == JUGAR and regresar_jugarRect.colliderect(miCursor):
                    estadoJuego= MENU_INICIAL
                    evento=True
                    break
                
                if estadoJuego == OPCIONES and regresar_opcionesRect.colliderect(miCursor):
                    estadoJuego = MENU_INICIAL
                    evento=True
                    break
                


        if evento==True:           
            if estadoJuego == MENU_INICIAL:
                screen.fill(black)
                screen.blit(menuInicial,menuInicialRect)#agregamos a la pantalla la imagen y deacuerdo a su rectangulo                
                screen.blit(jugar,jugarRect)
                screen.blit(opciones, opcionesRect)
                screen.blit(salir,salirRect)

            if estadoJuego == MENU_TURNO:
                screen.fill(black)
                screen.blit(menuTurno,menuTurnoRect)
                

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
#pygame.display.set_icon(icono) #icono de la ventana

black = (0, 0, 0)
size =width,height= 1366, 643

screen=pygame.display.set_mode(size)

#cargamos las imagenes
menuInicial = pygame.image.load("menuInicial.png")
menuOpciones = pygame.image.load("menuOpciones.png")
menuTurno = pygame.image.load("menuTurno.png")
tablero=pygame.image.load("tablero.png")

jugar=pygame.image.load("jugar.png")
opciones=pygame.image.load("iconOpciones.png")
salir=pygame.image.load("salir.png")
humano=pygame.image.load("humano.png")
maquina=pygame.image.load("maquina.png")

regresar_jugar=pygame.image.load("regresar_jugando.png")
regresar_opciones=pygame.image.load("regresar_opciones.png")
regresar_menuTurno=pygame.image.load("regresar_opciones.png").convert_alpha()


X=pygame.image.load("X.png")
O=pygame.image.load("O.png")
invisible=pygame.image.load("invisible.png")


"""
casilla0=Kasilla(invisible,X,O,459,150)
casilla1=Kasilla(invisible,X,O,636,150)
casilla2=Kasilla(invisible,X,O,811,150)
casilla3=Kasilla(invisible,X,O,459,309)
casilla4=Kasilla(invisible,X,O,636,309)
casilla5=Kasilla(invisible,X,O,811,309)
casilla6=Kasilla(invisible,X,O,459,471)
casilla7=Kasilla(invisible,X,O,636,471)
casilla7=Kasilla(invisible,X,O,811,471)

"""

#creamos los rectangulos de la imagenes, contienen X,Y,Width,Height
menuInicialRect = menuInicial.get_rect()
menuOpcionesRect = menuOpciones.get_rect()
menuTurnoRect= menuTurno.get_rect()
tableroRect=tablero.get_rect()

jugarRect= jugar.get_rect()
jugarRect.top,jugarRect.left  = (300,900)

salirRect = salir.get_rect()
salirRect.top , salirRect.left = (500,900)

opcionesRect=opciones.get_rect()
opcionesRect.top , opcionesRect.left = (400, 900)

humanoRect=humano.get_rect()
humanoRect.top, humanoRect.left =

maquinaRect=maquina.get_rect()
maquinaRect.top , maquinaRect.left =

regresar_menuTurnoRect=regresar_menuTurno.get_rect()
regresar_menuTurnoRect.top , regresar_menuTurnoRect.left = 

regresar_jugarRect = regresar_jugar.get_rect()
regresar_jugarRect.top , regresar_jugarRect.left = (550,1100)

regresar_opcionesRect=regresar_opciones.get_rect()
regresar_opcionesRect.top , regresar_opcionesRect.left =(550,900)



main()
            
        
