from classes.piece import Piece

class Rook(Piece):
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self,board,color,mode=0):
        current_pos = self.pos
        poss_targets = []

        aux_arr = [8,-8,1,-1]

        for i in aux_arr: #+
            poss_target = super().notation_converter(current_pos,True)
            while True:
                if i < 2 and i > -2:
                    poss_target = super().notation_converter(poss_target,False)
                    x = poss_target[1]
                    poss_target = super().notation_converter(poss_target,True)
                    poss_target += i
                    if poss_target < 1 or poss_target > 64:
                        break
                    poss_target = super().notation_converter(poss_target,False)
                    if x != poss_target[1]:
                        break
                else:
                    poss_target += i
                    if poss_target < 1 or poss_target > 64:
                        break
                    poss_target = super().notation_converter(poss_target,False)

                if board.board[poss_target] == None:
                    poss_targets.append(poss_target)
                else:
                    if mode == 1:
                        poss_targets.append(poss_target)   
                    piece = board.board[poss_target]
                    if piece.color != color:
                        poss_targets.append(poss_target)
                    break
                poss_target = super().notation_converter(poss_target,True)

        return poss_targets
        '''

        current_pos = super().notation_converter(self.pos,True)
        poss_targets = []

        aux_arr1 = [8,-8,1,-1]
        aux_arr2 = [(current_pos,1,0,65),(current_pos,1,0,0),(1,8,8,8),(1,8,8,0)]

        for i in range(4):
            poss_pos = current_pos + aux_arr1[i]
            while poss_pos < (int((current_pos - aux_arr2[i][0]) / aux_arr2[i][1]) * aux_arr2[i][2]) + aux_arr2[i][3] and poss_pos > 0 and poss_pos < 65:
                target_key = super().notation_converter(poss_pos,False)
                if board.board[target_key] is not None:
                    piece = board.board[target_key]
                    if piece.color != color:
                        poss_targets.append(super().notation_converter(poss_pos,False))
                        break
                    else:
                        if mode == 1:
                            poss_targets.append(super().notation_converter(poss_pos,False))    
                        break
                else:
                    poss_targets.append(super().notation_converter(poss_pos,False))
                poss_pos += aux_arr1[i]
        '''





        