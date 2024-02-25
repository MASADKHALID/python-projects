import random
class rock_paper_sis:
    def __init__(self):
        self.player_score=0
        self.comp_score=0
        self.move=["ROCK","PAPER","SISSOR"]
        self.user_move=input("ENTER YOUR MOVE::").upper()
        self.check_move()
        self.computer_move()
        self.win_condition()
        self.score_board()
        self.restart()
    def check_move(self):
        if self.user_move not in self.move:
            print("INVALID MOVE")
    def computer_move(self):
        self.comp_move_index=random.randrange(0,3)
        self.comp_move=self.move[self.comp_move_index]
        print(f"COMPUTER MOVE:{self.comp_move}")
    def win_condition(self):
        if (self.user_move == self.move[0] and self.comp_move == self.move[2]) or (self.user_move == self.move[1] and self.comp_move == self.move[0]) or (self.user_move == self.move[2] and self.comp_move == self.move[1]):
            print("PLAYER WON")
            self.player_score+=1
        elif (self.user_move == self.move[0] and self.comp_move == self.move[0]) or (self.user_move == self.move[1] and self.comp_move == self.move[1]) or (self.user_move == self.move[2] and self.comp_move == self.move[2]):
            print("DRAW")
        else:
            print("COMPUTER WON")
            self.comp_score+=1
    def score_board(self):
        print(f"PLAYER SCORE = {self.player_score}\nCOMPUTER SCORE = {self.comp_score}")
    def restart(self):
        self.restart_choice()
        while self.restart_game == True:
            self.user_move=input("ENTER YOUR MOVE::").upper()
            self.computer_move()
            self.win_condition()
            self.score_board()
            self.restart_choice()
    def restart_choice(self):
        self.restart=input("DO YOU WANT TO PLAY AGAIN-YES/NO::").upper()
        if self.restart == "YES":
            self.restart_game = True
        else:
            self.restart_game = False
print("ROCK-PAPER-SISSOR")
test1=rock_paper_sis()
