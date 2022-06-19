from classes.piece import Piece
class King(Piece):
    check = False
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)
    
    def calc_poss_targets(self,board,color,mode=0): #calc poss targets based on position and color
        current_pos = super().notation_converter(self.pos,True)
        p_targets = [current_pos + 1,current_pos - 1,current_pos - 8,current_pos + 8, current_pos - 8 + 1, current_pos - 8 - 1, current_pos + 8 + 1, current_pos + 8 - 1]
        p_targets = [target for target in p_targets if target > 0 and target < 65]
        poss_targets = []

        for target in p_targets: #check if field is occupied by piece of same color
            target_key = super().notation_converter(target,False)
            if board.board[target_key] is not None:
                piece = board.board[target_key]
                if piece.color != color: #occupied by enemy color, check is field is attacked
                    if mode == 0:
                        if board.field_attacked(target_key, piece.color):
                            continue
                        else:
                            poss_targets.append(target_key)
                    if mode == 1:
                        poss_targets.append(target_key)
            else:
                if mode == 0:
                    if board.field_attacked(target_key, color ^ 1): #check if attacked by enemy color
                        continue
                    else:
                        poss_targets.append(target_key)
                if mode == 1:
                    poss_targets.append(target_key) 
        return poss_targets




                                                                                                                                                                                   


