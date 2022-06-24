import math

class Piece:
    poss_targets = []
    moves = 0

    def __init__(self,color,pos,name) -> None:
        self.color = color
        self.pos = pos
        self.name = name

    def print_info(self):
        print(self.color,self.pos,self.name)

    def calc_poss_targets(self,board,color,mode): #returns keys of possible targets BUG: color unnecessary because piece already knows own color
        return [] 

    def notation_converter(self,inp,alpha_num_to_num):
        #print(inp)
        d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        if alpha_num_to_num:
            alpha = inp[0]
            num = int(inp[1])
            outp = ((num - 1) * 8) + d[alpha]
        else:
            z = inp / 8
            if (z).is_integer():
                num = int(z)
            else:
                num = int(math.ceil(z))
            a = inp - (num - 1) * 8
            alpha = list(d.keys())[list(d.values()).index(a)] 
            outp = alpha + str(num)
        return outp




