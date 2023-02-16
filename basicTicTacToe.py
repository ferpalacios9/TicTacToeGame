from random import randrange

circulo = "O"
cruz = "X"

board = []

for i in range(3):
    if i == 0:
        fila = [x for x in range(1, 4)]
        board.append(fila)
    if i == 1:
        fila = [x for x in range(4, 7)]
        board.append(fila)
    if i == 2:
        fila = [x for x in range(7, 10)]
        board.append(fila)

board[1][1] = "X" # board[row][column] - rows y columns from 0-2

def DisplayBoard(board):
# the function accept a parameter that is actually the board current status and displays it
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0],"  |  ", board[0][1],"  |  ", board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0],"  |  ", "X","  |  ", board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0],"  |  ", board[2][1],"  |  ", board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):
# the function accept the current board status and request the user to enter a move
    while True:
        try:
            global movimientoDe
            movimientoUsuario = movimientoDe = int(input("Please enter a position from 1-9 (you are 'O'): "))
            if movimientoUsuario > 0 and movimientoUsuario < 10: #Actualizar Board
                sign = "O"
                if movimientoUsuario == 1 and movimientoUsuario == isFreeField(board, sign):
                    board[0][0] = circulo
                    break
                elif movimientoUsuario == 2 and movimientoUsuario == isFreeField(board, sign):
                    board[0][1] = circulo  
                    break
                elif movimientoUsuario == 3 and movimientoUsuario == isFreeField(board, sign):
                    board[0][2] = circulo  
                    break
                elif movimientoUsuario == 4 and movimientoUsuario == isFreeField(board, sign):
                    board[1][0] = circulo  
                    break
                elif movimientoUsuario == 5:  
                    True
                elif movimientoUsuario == 6 and movimientoUsuario == isFreeField(board, sign):
                    board[1][2] = circulo  
                    break
                elif movimientoUsuario == 7 and movimientoUsuario == isFreeField(board, sign):
                    board[2][0] = circulo  
                    break
                elif movimientoUsuario == 8 and movimientoUsuario == isFreeField(board, sign):
                    board[2][1] = circulo  
                    break
                elif movimientoUsuario == 9 and movimientoUsuario == isFreeField(board, sign):
                    board[2][2] = circulo  
                    break
            else: 
                True
        except:
            True


def MakeListOfFreeFields(board):
# the function make a list of empty places
    lugaresVacios = []
    Encontrado = False
    for fila in range(len(board)):
        for columna in range(3):
            Encontrado = board[fila][columna] != cruz and board[fila][columna] != circulo
            if Encontrado:
                tupla = (fila, columna)
                lugaresVacios.append(tupla)
    return lugaresVacios

def VictoryFor(board, sign):
# the function analyzes if someone has won the game
    return ((board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or 
    (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or  
    (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or  
    (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or  
    (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or  
    (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or  
    (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or  
    (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign)) 

def DrawMove(board):
# the function draws the computer´s move and updates the board
    while True:
        global movimientoDe
        movimientoMaquina = movimientoDe = randrange(1, 10)
        sign = "X"
        if movimientoMaquina == 1 and movimientoMaquina == isFreeField(board, sign):
            board[0][0] = cruz  
            break
        elif movimientoMaquina == 2 and movimientoMaquina == isFreeField(board, sign):
            board[0][1] = cruz  
            break
        elif movimientoMaquina == 3 and movimientoMaquina == isFreeField(board, sign):
            board[0][2] = cruz  
            break
        elif movimientoMaquina == 4 and movimientoMaquina == isFreeField(board, sign):
            board[1][0] = cruz  
            break
        elif movimientoMaquina == 5 and movimientoMaquina == isFreeField(board, sign):
            True
        elif movimientoMaquina == 6 and movimientoMaquina == isFreeField(board, sign):
            board[1][2] = cruz  
            break
        elif movimientoMaquina == 7 and movimientoMaquina == isFreeField(board, sign):
            board[2][0] = cruz  
            break
        elif movimientoMaquina == 8 and movimientoMaquina == isFreeField(board, sign):
            board[2][1] = cruz  
            break
        elif movimientoMaquina == 9 and movimientoMaquina == isFreeField(board, sign):
            board[2][2] = cruz  
            break
        else: 
            True

def isFreeField(board, sign):
    MakeListOfFreeFields(board)
    lugaresBoard = []
    for fila in range(3):
        for columna in range(3):
            tupla = (fila, columna)
            lugaresBoard.append(tupla)
    lugaresBoard.insert(0, "Valor recorrido") 
    
    if lugaresBoard[movimientoDe] in MakeListOfFreeFields(board):
        return movimientoDe
    else:
        return False
    

            
def main():
    print("Welcome to TikTakToe... Creator: Fernando Palacios")
    DisplayBoard(board)

    while (len(MakeListOfFreeFields(board))>0):
        if VictoryFor(board, "O"):
            print("Player with O has won")
            break
        else:
            EnterMove(board)
            DisplayBoard(board)
            if VictoryFor(board, "X"):
                print("Player with X has won")
                break

        if VictoryFor(board, "X"):
            print("Player with X has won")
            break
        else:
            sign = "X"
            DrawMove(board)
            print("COMPUTER'S MOVE: ", movimientoDe)
            DisplayBoard(board)
            if VictoryFor(board, "X"):
                print("Player with X has won")
                break
        
    if len(MakeListOfFreeFields(board)) == 0 and VictoryFor(board, sign) != True:
        print("It's a tie!")


main()