import random

class Player:
    def __init__(self,human,color) -> None:
        self.human = human
        self.color = color #white == 1 == lower case

    def origin_valid(self,board,origin): #takes key to check if valid origin
        if origin not in board.board:
            return False
        p = board.get_piece(origin)
        if p is None: #no piece at origin key
            return False
        if p.color != self.color: #piece at origin has wrong color
            return False
        return True
   
    def check_move(self,board): #return legal origins in case of check   
        #get king
        legal_moves = [] #first list for origins that need to attack certain field, 
        pos = board.check
        king = board.get_piece(pos)
        
        attacking_pieces = board.field_attacked(pos, self.color ^ 1) #get attacking pieces

        #can attacking piece be removed?
        if attacking_pieces: #if there are attacking pieces (there must be)
            for piece in attacking_pieces:
                attacking_pieces_x2 = board.field_attacked(piece.pos, self.color) #get king-attacking piece attacking pieces of own color
                if attacking_pieces_x2: #if there are pieces which attack the king-attacking piece
                    for piece_x2 in attacking_pieces_x2:
                        legal_moves.append((piece_x2.pos,piece.pos)) #append legal origin
        
        #can king escape?
        poss_targets = king.calc_poss_targets(board, self.color)
        if poss_targets:
            for target in poss_targets:
                legal_moves.append((pos,target))

        #can friendly piece be moved in the way? only queen,bishop and rook have to be checked for this
        for piece in attacking_pieces:
            if piece.name == "n" or piece.name == "N" or piece.name == "p" or piece.name == "P": #cant be blocked
                continue
            path = piece.calc_poss_targets(board,self.color ^ 1) #possible places for interception
            cleared_path = []
            for field in path:
                if board.get_piece(field) != None:
                    continue
                cleared_path.append(field)

            available_pieces = board.available_pieces(self.color)

            for available_piece_key in available_pieces: #check if paths of available pieces and path of king attacking piece cross
                available_piece = board.get_piece(available_piece_key)
                ap_path = available_piece.calc_poss_targets(board,self.color)
                for field in ap_path:
                    for f in cleared_path:
                        if field == f: #cross
                            legal_moves.append((available_piece_key,field))

        if not legal_moves:
            board.checkmate(self.color)

        board.check = None

        return legal_moves #there are also targets that are not legal in this situation, pieces which should remove king-attacking pieces may not chose a target other than the pos of these pieces

    def move(self,board):
        if self.human: #human
            print("human")
            while True:
                origin = input("origin: ")
                if not Player.origin_valid(self,board,origin):
                    print("Invalid origin")
                    continue
                p = board.get_piece(origin)
                if not p.calc_poss_targets(board,self.color) and board.check == None:
                    print("no target available, choose different piece")
                    continue
                break
            target = input("target: ")
            p = board.get_piece(origin)
            poss_targets = p.calc_poss_targets(board, self.color)
            while target not in poss_targets:
                print("Illegal target, try again")
                target = input("target: ")
            p.pos = target 
            print("Moved from " + origin + " to " + target)

        else: #machine
            print("machine is moving")
            if board.check != None: #check
                print("check move")
                legal_moves = Player.check_move(self,board)

                if not legal_moves:
                    print("no legal moves -> checkmate")
                    return

                move = random.choice(legal_moves)
                print("move is "+move)

                p = board.get_piece(move[0])
                p.pos = move[1]

                if board.update(self.color) >= 0:
                    pass
                else:
                    print("last move was illegal (should not happen)")

                return
                
            else: #regular move
                print("regular move")
                poss_origins = board.available_pieces(self.color) #keys of available pieces
                while True:
                    origin = random.choice(poss_origins) #key
                    if not Player.origin_valid(self,board,origin):
                        continue
                    #origin valid -> get piece
                    print("origin: "+origin)
                    p = board.get_piece(origin)
                    poss_targets = p.calc_poss_targets(board, self.color) #calc poss targets
                    if poss_targets: #there are possible targets
                        target = random.choice(poss_targets) #chose target randomly (for now)
                        targeted_piece = board.get_piece(target)
                        if targeted_piece != None:
                            if targeted_piece.name == 'k' or targeted_piece.name == 'K': #target can not be a king
                                continue
                        
                        print("target: "+target)
                        p.pos = target
                        if board.update(self.color) >= 0:
                            print("update succesful")
                            break
                        else:
                            print("Illegal move, king is under attack!")
                            continue
                    else:
                        print("no possible targets")
                        continue #BUG:endless loop possible if every remaining piece has no possible targets

            print("Moving "+str(p.name)+ " from " + str(origin) + " to " + str(target))
            board.pretty_print()
        
            


        


        


        