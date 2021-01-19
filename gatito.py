
import random
import unittest
class ticTacToe:
    def __init__(self):
        self.tablero = [" " for x in range(10)]

    def meterMarcaEnTablero(self, lettra, posicion):
        self.tablero[posicion] = lettra

    def espacioDisponible(self, posicion):
        return self.tablero[posicion] == " "

    def imprimirTablero(self):






        t=self.tablero
        print(' ' + t[1] + ' | ' + t[2] + ' | ' + t[3])
        print('-----------')
        print(' ' + t[4] + ' | ' + t[5] + ' | ' + t[6])
        print('-----------')
        print(' ' + t[7] + ' | ' + t[8] + ' | ' + t[9])

    def esGanador(self, tablero, jugador):
        return (tablero[7] == jugador and tablero[8] == jugador and tablero[9] == jugador) or (tablero[4] == jugador and tablero[5] == jugador and tablero[6] == jugador) or(tablero[1] == jugador and tablero[2] == jugador and tablero[3] == jugador) or(tablero[1] == jugador and tablero[4] == jugador and tablero[7] == jugador) or(tablero[2] == jugador and tablero[5] == jugador and tablero[8] == jugador) or(tablero[3] == jugador and tablero[6] == jugador and tablero[9] == jugador) or(tablero[1] == jugador and tablero[5] == jugador and tablero[9] == jugador) or(tablero[3] == jugador and tablero[5] == jugador and tablero[7] == jugador)
        
    def movimientoJugador(self, modo=0, meterMarca=1):
        ciclo=True

        while ciclo:
            if modo==0:
                marcar = input("Ingresa la posición donde quieres marcar \'X\' (1-9): ")
            elif modo==1:
                marcar = random.randrange(0,10)
            elif modo==2:
                marcar = self.movimientoCPU()
            elif modo==3:
                marcar = meterMarca
            try:
                marcar = int(marcar)
                if marcar>0 and marcar<10:
                    if self.espacioDisponible(marcar):
                        ciclo = False
                        self.meterMarcaEnTablero("X", marcar)
                else:
                    print("El espacio ya se encuentra marcado, intenta otro")
            except:
                print("Ingresa un número")

    def movimientoCPU(self):
        movimientosPosibles = [x for x, letra in enumerate(self.tablero) if letra == " " and x!=0]#Crea un arreglo de tuplas que tienen el indice y el valor
        marcar = 0

        if 5 in movimientosPosibles:
            marcar = 5
            return marcar

        for simbolo in ["O", "X"]:
            for i in movimientosPosibles:
                copiaTablero = self.tablero[:]
                copiaTablero[i] = simbolo
                if self.esGanador(copiaTablero, simbolo):
                    marcar = i
                    return marcar
        
        centrosLinea = []
        esquina = []

        if self.tablero[2] == "X" and self.tablero[4] == "X":
            return 1
        if self.tablero[4] == "X" and self.tablero[8] == "X":
            return 7
        if self.tablero[8] == "X" and self.tablero[6] == "X":
            return 9
        if self.tablero[6] == "X" and self.tablero[2] == "X":
            return 3

        for i in movimientosPosibles:
            if i in [2, 4, 6, 8]:
                centrosLinea.append(i)

        if len(centrosLinea)>0:
            marcar = self.tomarRandom(centrosLinea)
            return marcar
        for i in movimientosPosibles:
            if i in [1,3,7,9]:
                esquina.append(i)
        if len(esquina) > 0:
            marcar = self.tomarRandom(esquina)
            return marcar


        return marcar
        
    def tomarRandom(self, array):
        return array[random.randrange(0, len(array))]

    
    def tableroLleno(self):
        if self.tablero.count(" ") > 1:
            return False
        else:
            return True

    def ejecutarJuego(self):
        print("Bienvenido!")
        self.imprimirTablero()

        while not(self.tableroLleno()):
            if not self.esGanador(self.tablero, "O"):
                self.movimientoJugador()
                self.imprimirTablero()
            else:
                print("EL CPU gano :D")
                break

            if not self.esGanador(self.tablero, "X"):
                marcar = self.movimientoCPU()
                if marcar == 0:
                    print("Empate!!")
                else:
                    self.meterMarcaEnTablero("O", marcar)
                    print("La CPU ha marcado en ", marcar)
                    self.imprimirTablero()
            else:
                print("Me jakiaron, amor")
                break

        if self.tableroLleno():
            print("Empate!!")

while True:
    decision = input("Quiere jugar? (Y/N)")
    juego = ticTacToe()
    if decision.lower() == "y" or decision.lower() == "yes":
        juego.ejecutarJuego()
    else:
        break
class pruebasUnitarias(unittest.TestCase):
    def testTurnoCorrecto(self):
        juego = ticTacToe()
        
        juego.imprimirTablero()
        #juego.tablero[0]="X" con este ocasiones error
        while not(juego.tableroLleno()):
            if (juego.tablero.count("X")-1<juego.tablero.count("O") and juego.tablero.count("O")+1 == juego.tablero.count("X")) or (not juego.tablero.count("O") == juego.tablero.count("X") and juego.tablero.count("O")+1 == juego.tablero.count("X")):
                juego.imprimirTablero()
                self.assertTrue( False, "Se está jugando en un turno incorrecto")

            if not juego.esGanador(juego.tablero, "O"):
                juego.movimientoJugador(1)
                juego.imprimirTablero()
            else:
                print("EL CPU gano :D")
                break

            if not juego.esGanador(juego.tablero, "X"):
                marcar = juego.movimientoCPU()
                if marcar == 0:
                    print("Empate!!")
                else:
                    juego.meterMarcaEnTablero("O", marcar)
                    print("La CPU ha marcado en ", marcar)
                    juego.imprimirTablero()
            else:
                print("Me jakiaron, amor")
                break
        if juego.tableroLleno():
            print("Empate!!")

    def testValidarEmpate(self):
        juego = ticTacToe()
        
        juego.imprimirTablero()
        while not(juego.tableroLleno()):#Agregar True a la condición para el error
            
            if juego.tableroLleno():
                self.assertTrue( False, "Hay empate más aún no se acaba el juego, error!!")

            if not juego.esGanador(juego.tablero, "O"):
                juego.movimientoJugador(2)
                juego.imprimirTablero()
            else:
                print("EL CPU gano :D")
                break#quitar para el error

            if not juego.esGanador(juego.tablero, "X"):
                marcar = juego.movimientoCPU()
                if marcar == 0:
                    print("Empate!!")
                else:
                    juego.meterMarcaEnTablero("O", marcar)
                    print("La CPU ha marcado en ", marcar)
                    juego.imprimirTablero()
            else:
                print("Me jakiaron, amor")
                break#quitar para el error
        if juego.tableroLleno():
            print("Empate!!")
            
    def testDireccionValida(self):
        juego = ticTacToe()
        
        juego.imprimirTablero()
        while not(juego.tableroLleno()):

            if not juego.esGanador(juego.tablero, "O"):
                meterDireccion = random.randrange(1,9)
                #meterDireccion = random.randrange(100,500)# descomentar para causar el error
                if not meterDireccion in [1,2,3,4,5,6,7,8,9]:
                    self.assertTrue( False, "Has Ingresado una casilla no valida")

                juego.movimientoJugador(1, meterDireccion)
                juego.imprimirTablero()
            else:
                print("EL CPU gano :D")
                break

            if not juego.esGanador(juego.tablero, "X"):
                marcar = juego.movimientoCPU()
                if marcar == 0:
                    print("Empate!!")
                else:
                    juego.meterMarcaEnTablero("O", marcar)
                    print("La CPU ha marcado en ", marcar)
                    juego.imprimirTablero()
            else:
                print("Me jakiaron, amor")
                break
        if juego.tableroLleno():
            print("Empate!!")

    def testNoSobreescribir(self):
        juego = ticTacToe()
        
        juego.imprimirTablero()
        #juego.tablero[0]="X"# con este ocasiones error
        while not(juego.tableroLleno()):
            if (juego.tablero.count("X")-1<juego.tablero.count("O") and juego.tablero.count("O")+1 == juego.tablero.count("X")) or (not juego.tablero.count("O") == juego.tablero.count("X") and juego.tablero.count("O")+1 == juego.tablero.count("X")):
                juego.imprimirTablero()
                self.assertTrue( False, "Se ha sobreescrito una dirección")
            if not juego.esGanador(juego.tablero, "O"):
                juego.movimientoJugador(1)
                juego.imprimirTablero()
            else:
                print("EL CPU gano :D")
                break

            if not juego.esGanador(juego.tablero, "X"):
                marcar = juego.movimientoCPU()
                if marcar == 0:
                    print("Empate!!")
                else:
                    juego.meterMarcaEnTablero("O", marcar)
                    print("La CPU ha marcado en ", marcar)
                    #juego.imprimirTablero()
            else:
                print("Me jakiaron, amor")
                break

        if juego.tableroLleno():
            print("Empate!!")

    def testValidacionGanador(self):
        juego = ticTacToe()
        
        juego.imprimirTablero()
        contador=0
        while not(juego.tableroLleno()):
            if juego.esGanador(juego.tablero, "X") or juego.esGanador(juego.tablero, "O"):
                if contador==1:
                    self.assertTrue( False, "Ya hay un ganador y el juego no ha acabado")
                else:
                    contador+=1

            if not juego.esGanador(juego.tablero, "O"):
                juego.movimientoJugador(1)
                juego.imprimirTablero()
            else:
                print("EL CPU gano :D")
                break#comenta está linea para lanzar el error

            if not juego.esGanador(juego.tablero, "X"):
                marcar = juego.movimientoCPU()
                if marcar == 0:
                    print("Empate!!")
                else:
                    juego.meterMarcaEnTablero("O", marcar)
                    print("La CPU ha marcado en ", marcar)
                    juego.imprimirTablero()
            else:
                print("Me jakiaron, amor")
                break#comenta está linea para lanzar el error

        if juego.tableroLleno():
            print("Empate!!")

 
#if __name__ == '__main__':
#unittest.main()