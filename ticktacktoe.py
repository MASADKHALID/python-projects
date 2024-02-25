class tick_tack_toe:

    def __init__(self):
        self.player_1=input("ENTER PLAYER 1 CHARACTER X OR O::")
        self.player_2=input("ENTER PLAYER 2 CHARACTER X OR O::")
        self.list_0=[" "," "," "]
        self.list_1=[" "," "," "]
        self.list_2=[" "," "," "]
        self.win = False
        self.valid_move=False

    def display_board(self):
        print(f"{self.list_0[0]}|{self.list_0[1]}|{self.list_0[2]}|")
        print("------")
        print(f"{self.list_1[0]}|{self.list_1[1]}|{self.list_1[2]}|")
        print("------")
        print(f"{self.list_2[0]}|{self.list_2[1]}|{self.list_2[2]}|")
        print("------")

    def choice_area_player_1(self):
        row=int(input("ENTER ROW::"))
        col=int(input("ENTER COLUMN::"))
        row-=1
        col-=1
        self.check_move(row,col)
        if self.valid_move:
            if row == 0:
                self.list_0[col]=self.player_1
            elif row == 1:
                self.list_1[col]=self.player_1
            elif row == 2:
                self.list_2[col]=self.player_1
            self.display_board()
            self.win_condition()
    
    def choice_area_player_2(self):
        row=int(input("ENTER ROW::"))
        col=int(input("ENTER COLUMN::"))
        row-=1
        col-=1
        self.check_move(row,col)
        if self.valid_move == True:
            if row == 0:
                self.list_0[col]=self.player_2
            elif row == 1:
                self.list_1[col]=self.player_2
            elif row == 2:
                self.list_2[col]=self.player_2
            self.display_board()
            self.win_condition()
    
    def check_move(self,row,col):
        if row == 0:
            if self.list_0[col]==" ":
                self.valid_move=True
            else:
                self.valid_move = False
                print("INVALID MOVE")
        elif row == 1:
            if self.list_1[col]==" ":
                self.valid_move=True
            else:
                self.valid_move = False
                print("INVALID MOVE")        
        elif row == 2:
            if self.list_2[col]==" ":
                self.valid_move=True
            else:
                self.valid_move = False
                print("INVALID MOVE")
        else:
            self.valid_move = False
            print("INVALID MOVE")
    
    def choice_area(self):
        while self.win == False:
            print("PLAYER 1 TURN")
            self.choice_area_player_1()
            if self.win == True:
                break
            print("PLAYER 2 TURN")
            self.choice_area_player_2()

    def win_condition(self):
        #player 1
        if self.list_0[0] == self.player_1 and self.list_0[1] == self.player_1 and self.list_0[2] == self.player_1:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_1[0] == self.player_1 and self.list_1[1] == self.player_1 and self.list_1[2] == self.player_1:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_2[0] == self.player_1 and self.list_2[1] == self.player_1 and self.list_2[2] == self.player_1:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_0[0] == self.player_1 and self.list_1[1] == self.player_1 and self.list_2[2] == self.player_1:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_0[2] == self.player_1 and self.list_1[1] == self.player_1 and self.list_2[0] == self.player_1:
            self.win = True
            print("PLAYER 1 WIN")
        #player2
        elif self.list_0[0] == self.player_2 and self.list_0[1] == self.player_2 and self.list_0[2] == self.player_2:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_1[0] == self.player_2 and self.list_1[1] == self.player_2 and self.list_1[2] == self.player_2:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_2[0] == self.player_2 and self.list_2[1] == self.player_2 and self.list_2[2] == self.player_2:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_0[0] == self.player_2 and self.list_1[1] == self.player_2 and self.list_2[2] == self.player_2:
            self.win = True
            print("PLAYER 1 WIN")
        elif self.list_0[2] == self.player_2 and self.list_1[1] == self.player_2 and self.list_2[0] == self.player_2:
            self.win = True
            print("PLAYER 1 WIN")

test1=tick_tack_toe()
test1.display_board()
test1.choice_area()
