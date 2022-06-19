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
        #print(str(board.check) + " " + p.name + " PIÜI")
        if board.check != None: #check!
            legal_origins = Player.check_move(self,board) #return legal origins in case of check
            if origin not in legal_origins: 
                return False
        return True
   
    def check_move(self,board): #return legal origins in case of check   
        #get king
        legal_origins = []
        # if self.color == 1:
        #     pos = board.find_pos('k')
        # else:
        #     pos = board.find_pos('K')
        # print("king positions "+str(pos))
        pos = board.check
        king = board.get_piece(pos)
        #can attacking piece be removed?
        attacking_pieces = board.field_attacked(pos, self.color ^ 1) #get attacking pieces

        if attacking_pieces: #if there are attacking pieces (there must be)
            for piece in attacking_pieces:
                attacking_pieces_x2 = board.field_attacked(piece.pos, self.color) #get king-attacking piece attacking pieces
                if attacking_pieces_x2: #if there are pieces which attack the king-attacking piece
                    for piece_x2 in attacking_pieces_x2:
                        legal_origins.append(piece_x2.pos) #append legal origin
        
        #can king escape?
        poss_targets = king.calc_poss_targets(board, self.color)
        if poss_targets:
            legal_origins.append(pos)

        #can friendly piece be moved in the way?
        #only queen,bishop and rook have to be checked for this,...hard task

        board.check = None

        return legal_origins #there are also targets that are not legal in this situation, pieces which should remove king-attacking pieces may not chose a target other than the pos of these pieces

    def move(self,board):
        print("Move:")
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
            print("machine")
            poss_origins = board.available_pieces(self.color) #keys of available pieces
            while True:
                origin = random.choice(poss_origins) #key
                print("origin: "+origin)
                if not Player.origin_valid(self,board,origin):
                    print("Invalid origin")
                    continue
                #origin valid -> get piece
                p = board.get_piece(origin)
                poss_targets = p.calc_poss_targets(board, self.color) #calc poss targets
                if poss_targets: #there are possible targets
                    target = random.choice(poss_targets) #chose target randomly (for now)
                    targeted_piece = board.get_piece(target)
                    if targeted_piece != None:
                        if targeted_piece.name == 'k' or targeted_piece.name == 'K': #target can not be a king
                            continue
                    p.pos = target
                    if board.update(self.color) >= 0:
                        break
                    else:
                        print("Illegal move, king is under attack!")
                        continue
                else:
                    print("list empty")
                    continue #BUG:endless loop possible if every remaining piece has no possible targets

            print("position of piece object changed to "+ target)
            print("Moving "+str(p.name)+ " from " + str(origin) + " to " + str(target))
            board.pretty_print()
        
            


        


        


        