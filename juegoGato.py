
import pygame, sys, time
from gatoIA import *



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
           
    def update(self,pantalla,cursor):
        #si colisiona con el cursor se cambia de imagen
        if cursor.colliderect(self.rect):
            print 'si'
            self.imagen_actual =self.imagen_X
            pantalla.blit(self.imagen_actual,self.rect)
            pygame.display.flip()
        """
        else:
            self.imagen_actual =self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)
        """




#-----Estados del juego
MENU_INICIAL=0
MENU_TURNO=1
JUGAR=2
OPCIONES=3
SALIR=4
GANA_JUGADOR=5
GANA_MAQUINA=6
GANA_EMPATE=7
#-----Turnos
MAQUINA=0
HUMANO=1

#----------


def main():
    A.reiniciarJuego()

    pygame.mixer.music.play(-1)#para que se ejecute la musica idefinidamente
        
    estadoJuego=MENU_INICIAL
    sonidoActivado=True
    miCursor=Cursor()
    evento=True
    turno=MAQUINA
    
    while 1:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)        
            if event.type == pygame.MOUSEBUTTONDOWN:                
                miCursor.update()

                """
                if estadoJuego==JUGAR:
                    casilla0.update(screen,miCursor)
                    casilla1.update(screen,miCursor)
                    casilla2.update(screen,miCursor)
                    casilla3.update(screen,miCursor)
                    casilla4.update(screen,miCursor)
                    casilla5.update(screen,miCursor)
                    casilla6.update(screen,miCursor)
                    casilla7.update(screen,miCursor)
                    casilla8.update(screen,miCursor)
                """

                if estadoJuego==OPCIONES:
                    if SIRect.colliderect(miCursor) and sonidoActivado==False:
                        sonidoActivado=True
                        evento=True
                    if NORect.colliderect(miCursor) and sonidoActivado==True:
                        sonidoActivado=False
                        evento=True
                        
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
                    A.seleccionarTurno(MAQUINA)
                    evento=True
                    break

                if estadoJuego == MENU_TURNO and humanoRect.colliderect(miCursor):
                    estadoJuego=JUGAR
                    turno=HUMANO
                    A.seleccionarTurno(HUMANO)
                    evento=True
                    break

                if estadoJuego== MENU_TURNO and regresar_menuTurnoRect.colliderect(miCursor):
                    estadoJuego=MENU_INICIAL
                    evento=True
                    break
                
                if estadoJuego == JUGAR and regresar_jugarRect.colliderect(miCursor):                    
                    estadoJuego= MENU_TURNO
                    evento=True
                    break
                
                if estadoJuego == OPCIONES and regresar_opcionesRect.colliderect(miCursor):
                    estadoJuego = MENU_INICIAL
                    evento=True
                    break


        A.actualizarTablero(0)
        posiciones=list(A.regresarTablero())
        
        if posiciones[0]=='X':
            casilla0.setImagenX(screen)
        if posiciones[0]=='O':
            casilla0.setImagenO(screen)
                                            
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
                screen.blit(humano,humanoRect)
                screen.blit(maquina,maquinaRect)
                screen.blit(regresar_menuTurno,regresar_menuTurnoRect)
                

            if estadoJuego == JUGAR:
                screen.fill(black)
                screen.blit(tablero,tableroRect)
                screen.blit(regresar_jugar,regresar_jugarRect)

            if estadoJuego == OPCIONES:
                screen.fill(black)
                screen.blit(menuOpciones,menuOpcionesRect)
                screen.blit(SI,SIRect)
                screen.blit(NO,NORect)
                if sonidoActivado==True:
                    screen.blit(palomitaSI,palomitaSIRect)
                    if pygame.mixer.music.get_busy() == False: #si el sonido  no se esta reproduciendo
                        pygame.mixer.music.play(-1)
                else:
                    if pygame.mixer.music.get_busy(): #si el sonido se esta reproduciendo
                        pygame.mixer.music.stop()
                    screen.blit(palomitaNO,palomitaNORect)
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

menuGanaHumano=pygame.image.load("menuGanaHumano.png")
menuGanaMaquina=pygame.image.load("menuGanaMaquina.png")
menuEmpatan=pygame.image.load("menuEmpatan.png")                                  

tablero=pygame.image.load("tablero.png")

jugar=pygame.image.load("jugar.png")
opciones=pygame.image.load("iconOpciones.png")
salir=pygame.image.load("salir.png")
humano=pygame.image.load("humano.png")
maquina=pygame.image.load("maquina.png")
palomitaSI=pygame.image.load("palomita.png")
palomitaNO=pygame.image.load("palomita.png").convert_alpha()


regresar_jugar=pygame.image.load("regresar_jugando.png")
regresar_opciones=pygame.image.load("regresar_opciones.png")
regresar_menuTurno=pygame.image.load("regresar_opciones.png").convert_alpha()


X=pygame.image.load("X.png")
O=pygame.image.load("O.png")
invisible=pygame.image.load("invisible.png")

SI=pygame.image.load("SI.png")
NO=pygame.image.load("NO.png")

pygame.mixer.music.load("musicmenu.mp3")


casilla0=Kasilla(invisible,X,O,459,150)
casilla1=Kasilla(invisible,X,O,636,150)
casilla2=Kasilla(invisible,X,O,811,150)
casilla3=Kasilla(invisible,X,O,459,309)
casilla4=Kasilla(invisible,X,O,636,309)
casilla5=Kasilla(invisible,X,O,811,309)
casilla6=Kasilla(invisible,X,O,459,471)
casilla7=Kasilla(invisible,X,O,636,471)
casilla8=Kasilla(invisible,X,O,811,471)

#creamos los rectangulos de la imagenes, contienen X,Y,Width,Height
menuInicialRect = menuInicial.get_rect()
menuOpcionesRect = menuOpciones.get_rect()
menuTurnoRect= menuTurno.get_rect()
tableroRect=tablero.get_rect()
menuGanaHumanoRect=menuGanaHumano.get_rect()
menuGanaMaquinaRect=menuGanaMaquina.get_rect()
menuEmpatanRect=menuEmpatan.get_rect()                                  

jugarRect= jugar.get_rect()
jugarRect.top,jugarRect.left  = (300,900)

salirRect = salir.get_rect()
salirRect.top , salirRect.left = (500,900)

opcionesRect=opciones.get_rect()
opcionesRect.top , opcionesRect.left = (400, 900)
                                  
humanoRect=humano.get_rect()
humanoRect.top, humanoRect.left = (286,305)

maquinaRect=maquina.get_rect()
maquinaRect.top , maquinaRect.left = (291,867)

regresar_menuTurnoRect=regresar_menuTurno.get_rect()
regresar_menuTurnoRect.top , regresar_menuTurnoRect.left = (544,1017)

regresar_jugarRect = regresar_jugar.get_rect()
regresar_jugarRect.top , regresar_jugarRect.left = (550,1100)

regresar_opcionesRect=regresar_opciones.get_rect()
regresar_opcionesRect.top , regresar_opcionesRect.left =(511,993)

SIRect=SI.get_rect()
SIRect.top , SIRect.left = (170,710)

NORect=NO.get_rect()
NORect.top , NORect.left = (170,1028)

palomitaSIRect=palomitaSI.get_rect()
palomitaSIRect.top , palomitaSIRect.left = (176,634)

palomitaNORect=palomitaNO.get_rect()
palomitaNORect.top , palomitaNORect.left = (180,926)



main()
            
        
