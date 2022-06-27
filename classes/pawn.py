from classes.piece import Piece

class Pawn(Piece):
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self,board,color,mode=0): #BUG pawn can skip other pieces with first 2field move
        current_pos = super().notation_converter(self.pos,True)
        if color == 1:
            p_targets = [current_pos + 8, current_pos + 7, current_pos + 9]
            if self.moves == 0: 
                p_targets.append(current_pos + 16)
        else:
            p_targets = [current_pos - 8, current_pos - 7, current_pos - 9]
            if self.moves == 0:
                p_targets.append(current_pos - 16)   

        p_targets = [target for target in p_targets if target > 0 and target < 65]
        poss_targets = []

        for target in p_targets:
            target_key = super().notation_converter(target,False)
            if board.board[target_key] is not None:
                if target_key[0] != self.pos[0]:
                    piece = board.board[target_key]
                    if piece.color != color: 
                        poss_targets.append(super().notation_converter(target,False))
            else:
                if target_key[0] == self.pos[0] and mode == 0:
                        poss_targets.append(super().notation_converter(target,False))
                if mode == 1:
                    poss_targets.append(super().notation_converter(target,False))
        return poss_targets
    
    

