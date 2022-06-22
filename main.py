from classes import *
import time

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

if __name__ == "__main__": #main
    b = board.Board()
    b.setup(START_FEN)

    player1 = player.Player(human=False,color=1) #white
    player2 = player.Player(human=False,color=0) #black

    b.pretty_print()

    while True:
        if player1.color == 1:
            print("player 1 (white)")
            player1.move(b)
            time.sleep(2)

            if b.game_over:
                break

            print("player 2 (black)")
            player2.move(b)
            time.sleep(2)

            if b.game_over:
                break

        else:
            print("player 2 (white)")
            player2.move(b)
            time.sleep(2)

            if b.game_over:
                break

            print("player 1 (black)")
            player1.move(b)
            time.sleep(2)

            if b.game_over:
                break




