from classes.piece import Piece

class Queen(Piece): 
    def __init__(self,color,pos,name) -> None:
        super().__init__(color,pos,name)

    def calc_poss_targets(self, board, color, mode=0):
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

        aux_arr1 = [(8,1),(8,-1),(-8,1),(-8,-1)]

        for i in aux_arr1: #x
            poss_target = super().notation_converter(current_pos,True)
            while True:
                poss_target += i[0]
                if poss_target < 1 or poss_target > 64:
                    break
                poss_target = super().notation_converter(poss_target,False)
                x = poss_target[1]
                poss_target = super().notation_converter(poss_target,True)
                poss_target += i[1]
                if poss_target < 1 or poss_target > 64:
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
         
        ##################Code below is buggy
        #BUG queen at d2 can attack ['d3, 'e2', a8', 'g6', 'f7', 'e8'] but not c2
        '''
        |R|N|B|Q|K|B|N|R|8
        |P|P|P|P|P|/|P|P|7
        |/|/|/|/|/|P|/|/|6
        |/|/|/|/|/|/|/|/|5
        |/|/|/|/|/|/|/|/|4
        |/|/|/|p|/|/|/|/|3
        |p|p|p|q|p|p|p|p|2
        |r|n|b|/|k|b|n|r|1
        a b c d e f g h

        current_pos = super().notation_converter(self.pos,True)

        poss_targets = []

        aux_arr1 = [8,-8,1,-1]
        aux_arr2 = [(current_pos,1,0,65),(current_pos,1,0,0),(1,8,8,8),(1,8,8,0)]

        for i in range(4): #+
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

        for i in range(4): #x
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
        '''
        
        

