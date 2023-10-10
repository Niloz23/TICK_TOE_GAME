print('''Это игра крестики-нолики
Для удобства я сделал расстановку координат не по "питонскому", 
а по нормальному, то есть 1,1 координата это не 2,2 переводя на наш язык, а так же 1,1 для питона.
Игроки ходят поочереди, правила стандартные: игрок 1 играет за крестик, а игрок 2 за нолик.
Также прошу играть честно, иначе игра остановится, и вы сможете вводить координаты до появления зеленого, так что следите за игрой и следуйте правилам, приятной игры!!!!
''')

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def vivod_polia():
    for row in board:
        print(" | ".join(row))
        print("__________")

def vivod_result():
    pl1 = int(input('player1 введите строку: '))
    pl2 = int(input('player1 введите столбец: '))
    if pl1 > 3 or pl2 > 3:
        print('вы ввели неправильные координаты')
        return False
    if board[pl1 - 1][pl2 - 1] == ' ':
        board[pl1 - 1][pl2 - 1] = 'X'
    else:
        print('Не пытайтесь жульничать, на этом месте уже стоит знак другого игрока')
        return False
    vivod_polia()

    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or \
       (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or \
       (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or \
       (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or \
       (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or \
       (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or \
       (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
       (board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X'):
        print('player 1 выиграл!')
        return False

    if draw(board):
        print("Ничья!")
        return False

    igr1 = int(input('player2 введите строку: '))
    igr2 = int(input('player2 введите столбец: '))
    if igr1 > 3 or igr2 > 3:
        print('вы ввели неправильные координаты')
        return False
    if board[igr1 - 1][igr2 - 1] == ' ':
        board[igr1 - 1][igr2 - 1] = 'O'
    else:
        print('Не пытайтесь жульничать, на этом месте уже стоит знак другого игрока')
        return False
    vivod_polia()

    if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or \
       (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or \
       (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or \
       (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or \
       (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or \
       (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or \
       (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
       (board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O'):
        print('player 2  выиграл!')
        return False

    if draw(board):
        print("Ничья!")
        return False

    return True

while True:
    if not vivod_result():
        break