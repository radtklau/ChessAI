from classes.piece import Piece

class Queen(Piece):
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self, board, color,mode=0):
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
        
        edges = [[1,9,17,25,33,41,49,57],[8,16,24,32,40,48,56,64]]
        aux_arr3 = [(8,1),(8,-1),(-8,1),(-8,-1)]
        break_flag = False

        for i in range(4):
            poss_pos = current_pos + aux_arr3[i][0] + aux_arr3[i][1]
            while poss_pos > 0 and poss_pos < 65:
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
                poss_pos += aux_arr3[i][0] + aux_arr3[i][1]
            if break_flag:
                break
            if poss_pos in edges[0] or poss_pos in edges[1]:
                break_flag = True

        return poss_targets

