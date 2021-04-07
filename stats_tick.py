class tik_tak_toe_game():
    def __init__(self):
        self.board=[["","",""],
                    ["","",""],
                    ["","",""]]
    

    def check_game_over(self):
        if(self.board[0][0]==self.board[1][1]==self.board[2][2]!=""):
            return True
        elif(self.board[0][2]==self.board[1][1]==self.board[2][0]!=""):
            return True
        elif(self.board[0][0]==self.board[1][0]==self.board[2][0]!=""):
            return True
        elif(self.board[0][1]==self.board[1][1]==self.board[2][1]!=""):
            return True
        elif(self.board[0][2]==self.board[1][2]==self.board[2][2]!=""):
            return True
        elif(self.board[0][0]==self.board[0][1]==self.board[0][2]!=""):
            return True
        elif(self.board[1][0]==self.board[1][1]==self.board[1][2]!=""):
            return True
        elif(self.board[2][0]==self.board[2][1]==self.board[2][2]!=""):
            return True
        else:
            return False

    def clear_all(self):
        self.board=[["","",""],
                    ["","",""],
                    ["","",""]]
                
    
    
    def print_board(self):
        for row in self.board:
            print("+---+---+---+")
            for sign in row:
                print("|",end=" ")
                if sign=="":
                    print(" ",end=" ")
                else:
                    print(sign,end=" ")
            print("|")
        print("+---+---+---+")

    def make_move(self,arg1,move):
        if (arg1=="x"):
            if(move==1):
                if(self.board[0][0]==""):
                    self.board[0][0]="x"
            elif(move==2):
                if(self.board[0][1]==""):
                    self.board[0][1]="x"
            elif(move==3):
                if(self.board[0][2]==""):
                    self.board[0][2]="x"
            elif(move==4):
                if(self.board[1][0]==""):
                    self.board[1][0]="x"
            elif(move==5):
                if(self.board[1][1]==""):
                    self.board[1][1]="x"
            elif(move==6):
                if(self.board[1][2]==""):
                    self.board[1][2]="x"
            elif(move==7):
                if(self.board[2][0]==""):
                    self.board[2][0]="x"
            elif(move==8):
                if(self.board[2][1]==""):
                    self.board[2][1]="x"
            elif(move==9):
                if(self.board[2][2]==""):
                    self.board[2][2]="x"
        else:
            if(move==1):
                if(self.board[0][0]==""):
                    self.board[0][0]="o"
            elif(move==2):
                if(self.board[0][1]==""):
                    self.board[0][1]="o"
            elif(move==3):
                if(self.board[0][2]==""):
                    self.board[0][2]="o"
            elif(move==4):
                if(self.board[1][0]==""):
                    self.board[1][0]="o"
            elif(move==5):
                if(self.board[1][1]==""):
                    self.board[1][1]="o"
            elif(move==6):
                if(self.board[1][2]==""):
                    self.board[1][2]="o"
            elif(move==7):
                if(self.board[2][0]==""):
                    self.board[2][0]="o"
            elif(move==8):
                if(self.board[2][1]==""):
                    self.board[2][1]="o"
            elif(move==9):
                if(self.board[2][2]==""):
                    self.board[2][2]="o"
