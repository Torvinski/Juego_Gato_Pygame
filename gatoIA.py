#Aqui tenemos todo el codigo para que funcione
import random


PRIMERO=1
SEGUNDO=0

CUADROVACIO=" "
EQUIS="X"
CERO="O"



def gano(x, tablero):
    for i in range(3):
        if (x==tablero[i*3+0]==tablero[i*3+1]==tablero[i*3+2]) or (x==tablero[i]==tablero[i+3]==tablero[i+6]):

            return True
        elif x==tablero[0]==tablero[4]==tablero[8] or x==tablero[2]==tablero[4]==tablero[6]:
            return True
    return False


class Reloj:
    def __init__(self,contador):
        self.contador=contador

    def iniciarConteo(self):
        None

    def actualizarContador(self):
        None

    def regresarTiempoTranscurrido(self):
        segundos=0
        return segundos

class Casilla:
    def __init__(self):
         self.ficha=None

    def asignarValorACasilla(self,ficha):
        self.ficha=ficha

    def ocupado(self):
        if self.ficha==None:
            return False
        else:
            return True

    def get_ficha():
        return self.ficha

    def destruirCasilla(self):
        None


class Ficha:
    def __init__(self,valor):
        self.valor=valor

    def regresarValor(self):
        return self.valor

    def crearFicha(self):
        None

    def destruirFicha(self):
        None

    def colocarFicha(self,Tablero,posicion):
        return Tablero.colocarEnPosicion(posicion, self)


class Tablero:
    def __init__(self):
        self.cuadro=[]
        for i in range(9):
            self.cuadro.append(Casilla())
        None

    def colocarEnPosicion(self,posicion,ficha):
        if self.cuadro[posicion].ocupado():

            return False
        else:
            self.cuadro[posicion].asignarValorACasilla(ficha)
            return True


    def regresarPosicion(self,posicion):
        if self.cuadro[posicion].ocupado():
            return self.cuadro[posicion].ficha.regresarValor()
        return CUADROVACIO




    def crearTablero(self):
        None

    def destruirTablero(self):
        None



class Jugador:
    def escogerPosicion(self):
        None
    def __init__(self, turno,ficha):
        self.turno=turno
        self.ficha=ficha
    def destruirJugador(self):
        None

class Humano(Jugador):

    def escogerPosicion(self,posicion):
        return posicion

class Virtual(Jugador):

    def calcularPosicion(self, oponente, tablero):
        f=self.ficha.regresarValor()
        t=list(tablero)
        celdasA=[0,2,4,6,8]
        celdasB=[1,3,5,7]
        random.shuffle(celdasA)
        random.shuffle(celdasB)
        print(celdasA)
        for i in range(9):
            if tablero[i] == CUADROVACIO:
                h=t[:]
                h[i]=f

                if gano(f,h):
                    return i
        for i in range(9):
            if tablero[i] == CUADROVACIO:
                h=t[:]
                h[i]=oponente

                if gano(oponente,h):
                    return i
        for i in celdasA:
            if tablero[i] == CUADROVACIO:
                return i
        for i in celdasB:
            if tablero[i] == CUADROVACIO:
                return i


class Ambiente:
    def __init__(self):
        self.reloj=Reloj(1)
        self.tablero=Tablero()
        self.turno=1
        self.juego_terminado=False
        self.ganador=""

    def seleccionarTurno(self,bandera):#Puedes usar esta funcion
        if bandera==0:
            self.iniciaMaquina()
        else:
            self.iniciaHumano()


    def iniciaHumano(self):
        self.jugadorH=Humano(PRIMERO, Ficha(EQUIS))
        self.jugadorV=Virtual(SEGUNDO, Ficha(CERO))

    def iniciaMaquina(self):
        self.jugadorH=Humano(SEGUNDO, Ficha(CERO))
        self.jugadorV=Virtual(PRIMERO, Ficha(EQUIS))
        self.tablero.colocarEnPosicion(self.jugadorV.calcularPosicion(self.jugadorH.ficha.regresarValor(), self.regresarTablero()),self.jugadorV.ficha)
        self.turno=self.turno+1

    def colocarM(self):
        return self.tablero.colocarEnPosicion(self.jugadorV.calcularPosicion(self.jugadorH.ficha.regresarValor() ,self.regresarTablero()),self.jugadorV.ficha)

    def colocarH(self,pos):
        return self.tablero.colocarEnPosicion(self.jugadorH.escogerPosicion(pos),self.jugadorH.ficha)


    def actualizarTablero(self, pos_jugador):#Puedes usar esta funcion
        if not self.juego_terminado:
            if self.turno%2==self.jugadorH.turno and self.colocarH(pos_jugador):
                self.turno=self.turno+1
                #implementar aqui actualizarInterfaz( pos_jugador, self.jugadorH.ficha.regresarValor())
                if gano(self.jugadorH.ficha.regresarValor(),self.regresarTablero()):
                    self.juego_terminado=True
                    self.ganador="Humano"

                elif self.turno==10:
                    self.juego_terminado=True
                    self.ganador="Empate"



        if not self.juego_terminado:
            if self.turno%2==self.jugadorV.turno and self.colocarM():
                self.turno=self.turno+1
                if gano(self.jugadorV.ficha.regresarValor(),self.regresarTablero()):
                    self.juego_terminado=True
                    self.ganador="Maquina"
                elif self.turno==10:
                    self.juego_terminado=True
                    self.ganador="Empate"

        return(self.juego_terminado)

    def identificarGanador(self):#Puedes usar esta funcion
        return self.ganador

    def regresarTablero(self):#Puedes usar esta funcion
        cadena=""
        for i in range(9):
            cadena=cadena+self.tablero.regresarPosicion(i)

        return cadena

    def reiniciarJuego(self):#Puedes usar esta funcion
        self.reloj=Reloj(1)
        self.tablero=Tablero()
        self.turno=1
        self.juego_terminado=False

    def finDeJuego(self):
        None


#comentar desde aqui
A=Ambiente() #Crea el objeto de ambiente
print (A.regresarTablero()) #Regresara un string del tablero del gato, en este caso sera una cadena vacia
A.seleccionarTurno(1) #Selecciona el turno, ya sea maquina o humano (maquina es 0 por default, cualquier otro valor es para elegir al humano).
print (A.regresarTablero()) 

A.actualizarTablero(1) #Actualiza el tablero, aqui entra el funcionamiento del gato. Se mete un numero que es la posicion del tablero. Regresa un valor booleano.
#if A.actualizarTablero(X)==True: #Si este valor es verdadero, el juego termina, si es falso, el juego sigue
#    print (A.regresarTablero) 
#    A.identificarGanador() #Aqui te regresara un string del ganador del juego, sea humano, maquina o empate
#    A.reiniciarJuego() #Aqui reinicia todos los valores a un estado predeterminado.
print (A.regresarTablero()) #Regresara un string del tablero.
A.actualizarTablero(4)

print (A.regresarTablero())
A.actualizarTablero(7)
print (A.regresarTablero())
#comentar hasta aca
