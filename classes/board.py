import math
from . import knight,bishop,queen,king,pawn,rook
import time

class Board:
    LETTERS = ["a","b","c","d","e","f","g","h"]
    NUMBERS = ["1","2","3","4","5","6","7","8"]
    c = ["black","white"]
    board = {}
    check = None
    move_no = 1
    game_over = False

    def __init__(self) -> None:
        for number in Board.NUMBERS:
            for letter in Board.LETTERS:
                key = letter + number
                Board.board[key] = None

    def fen_parser(self,fen_string):
        l = fen_string.split(" ")
        positions = l[0].split("/")
        p = 0
        for entry in positions:
            for char in entry:
                if char.isalpha():
                    num = math.floor(p / 8) + 1
                    alpha = Board.LETTERS[p % 8]
                    key = alpha + str(num)
                    Board.board[key] = char
                    p += 1
                if char.isdigit():
                    p += int(char)

    def gen_piece(self,key):
        piece_type = Board.board[key]

        if piece_type == 'r' or piece_type == 'R':
            color = 0
            if piece_type.islower():
                color = 1
            return rook.Rook(color,key,piece_type)

        elif piece_type == 'n' or piece_type ==  'N':
            color = 0
            if piece_type.islower():
                color = 1
            return knight.Knight(color,key,piece_type)

        elif piece_type == 'b' or piece_type ==  'B':
            color = 0
            if piece_type.islower():
                color = 1
            return bishop.Bishop(color,key,piece_type)

        elif piece_type == 'q' or piece_type ==  'Q':
            color = 0
            if piece_type.islower():
                color = 1
            return queen.Queen(color,key,piece_type)

        elif piece_type == 'k' or piece_type ==  'K':
            color = 0
            if piece_type.islower():
                color = 1
            return king.King(color,key,piece_type)

        elif piece_type == 'p' or piece_type ==  'P':
            color = 0
            if piece_type.islower():
                color = 1
            return pawn.Pawn(color,key,piece_type)

    def setup(self,fen_string):
        fs = fen_string
        Board.fen_parser(self,fs)
        for key in Board.board:
            if Board.board[key] is not None:
                piece = Board.gen_piece(self,key)
                Board.board[key] = piece

    def pretty_print(self):
        for i in range(8,0,-1): 
            for h in Board.LETTERS:
                key = h + str(i)
                if Board.board[key] is not None:
                    print("|",end="")
                else:
                    print("|/",end="")
                if Board.board[key] is not None:
                    print(Board.board[key].name,end="")
            print("|",end="")
            print(i)
        print(" a b c d e f g h")
        print("___________________")
        #time.sleep(5)

    def update(self,color):
        self.move_no += 1
        for key in Board.board: #go through all fields
            if Board.board[key] is not None: #if there is a piece on this field
                piece = Board.board[key]

                #check if king is attacked and if last move was illegal because king was uncovered
                if piece.name == 'k' or piece.name == 'K': #king
                    attacking_pieces = Board.field_attacked(self,piece.pos,piece.color ^ 1)
                    if attacking_pieces: #king is in check (attacked by enemy color)
                        print(str(self.c[piece.color])+" King is attacked by "+str(attacking_pieces)+", check!")
                        if color == piece.color: #check if attacked king has same color as last moves player, if yes -> move was illegal!
                            print("last move uncovered king")
                            return -1
                        else:
                            print("check")
                            Board.check = key #check TODO Fix this in player.check_move()

                if piece.pos != key: #change position of piece
                    piece.moves += 1
                    if Board.board[piece.pos] != None:
                        print("Beat piece at "+str(piece.pos))
                    Board.board[piece.pos] = piece #move piece to new position
                    Board.board[key] = None #remove from old position
                    
        return 1

    def checkmate(self,color): #check if no checkmate or draw or player surrendered
        print("check mate, " + self.c[color ^ 1] + " wins.")
        self.game_over = True

    def get_piece(self,pos):
        return Board.board[pos]

    def available_pieces(self,color): #returns keys of available pieces in a list (e.g. [a4,b2,h6,e1])
        available_pieces = []
        for field in Board.board.items():
            if field[1] != None:
                key = field[0]
                piece = field[1]
                if piece.color == color:
                    available_pieces.append(key)

        return available_pieces

    def find_pos(self,piece_name): #find position by name
        positions = []
        for field in Board.board.items():
            print(str(field[1]),str(piece_name))
            if field[1] == piece_name:
                positions.append(field[0])
                
        return positions #return key(s)

    def field_attacked(self,field,color): #calculate if field is attacked by any piece with color color, returns attacking pieces or false
        attacking_pieces = []
        for piece in Board.board.values():
            if piece != None:
                if piece.color == color:
                    attacked_fields = piece.calc_poss_targets(self,piece.color,mode=1)
                    if field in attacked_fields:
                        print(str(piece.name)+" at "+str(piece.pos)+ " attacks "+str(attacked_fields))
                        attacking_pieces.append(piece)
        if attacking_pieces:
            return attacking_pieces
        else:
            return False



