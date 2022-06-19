from classes.piece import Piece

class Knight(Piece):
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self, board, color,mode=0): #BUG: knight can move from g1 to a3
        current_pos = super().notation_converter(self.pos,True)
        p_targets = [current_pos + 15, current_pos + 17, current_pos - 15, current_pos - 17, current_pos + 10, current_pos - 10, current_pos + 6, current_pos - 6]

        p_targets = [target for target in p_targets if target > 0 and target < 65]
        poss_targets = []

        for target in p_targets:
            target_key = super().notation_converter(target,False)
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
