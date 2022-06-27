from classes.piece import Piece

class Bishop(Piece):
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self, board, color,mode=0):     
        current_pos = self.pos
        poss_targets = []     

        aux_arr = [(8,1),(8,-1),(-8,1),(-8,-1)]

        for i in aux_arr: #x
            poss_target = super().notation_converter(current_pos,True)
            while True:
                poss_target += i[0]
                if poss_target < 1 or poss_target > 64:
                    break
                poss_target = super().notation_converter(poss_target,False)
                x = poss_target[1]
                poss_target = super().notation_converter(poss_target,True)
                poss_target += i[1]
                if poss_target < 0 or poss_target > 64:
                    break
                poss_target = super().notation_converter(poss_target,False)
                if x != poss_target[1]:
                    break

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
        break_flag = False

        edges = [[1,9,17,25,33,41,49,57],[8,16,24,32,40,48,56,64]]
        aux_arr1 = [(8,1),(8,-1),(-8,1),(-8,-1)]
        for i in range(4):
            poss_pos = current_pos + aux_arr1[i][0] + aux_arr1[i][1]
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
                poss_pos += aux_arr1[i][0] + aux_arr1[i][1]
            if break_flag:
                break
            if poss_pos in edges[0] or poss_pos in edges[1]:
                break_flag = True
        '''
        
