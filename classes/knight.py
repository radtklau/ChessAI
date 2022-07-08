from classes.piece import Piece
import math

class Knight(Piece): #BUG can attack like bishop e.g. e2 to g4
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self, board, color, mode=0): #BUG: knight can move from g1 to a3
        d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        current_pos = super().notation_converter(self.pos,True)
        p_targets = [current_pos + 15, current_pos + 17, current_pos - 15, current_pos - 17, current_pos + 10, current_pos - 10, current_pos + 6, current_pos - 6]

        p_targets = [target for target in p_targets if target > 0 and target < 65]
        poss_targets = []

        for target in p_targets:
            target_key = super().notation_converter(target,False)

            target_key_alpha = target_key[0]
            current_pos_alpha = self.pos[0]
            target_key_num = target_key[1]
            current_pos_num = self.pos[1]

            if (math.fabs(d[target_key_alpha] - d[current_pos_alpha]) > 3 and math.fabs(int(target_key_num) - int(current_pos_num)) > 2) or (math.fabs(d[target_key_alpha] - d[current_pos_alpha]) > 2 and math.fabs(int(target_key_num) - int(current_pos_num)) > 3): 
                continue

            if board.board[target_key] is not None:
                piece = board.board[target_key]
                if piece.color != color: 
                    poss_targets.append(super().notation_converter(target,False))
                else:
                    if mode == 1:
                        poss_targets.append(super().notation_converter(target,False))
            else:
                poss_targets.append(super().notation_converter(target,False))

        return poss_targets #return keys of possible targets
