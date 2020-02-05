# - game
#     - attribute
#         - board instance
#         - player instances (int between the people vs player obj)
#         - cur player
#         - validate play - win or tie
#    - method
#        - play
#        - init board
#        - play round - place piece
#        - switch player
#        - print scores
#        - print current player
#        - print winner statemnt
#        - print tie decloration
#        - print invalid input

# - need board - (2 D matrix )
#     - attribute
#         - number of moves remaining
#         - pieces
#     - method
#        - print board
#        - place piece
#        - can place piece
#        - check win

class Board:
  def __init__(self):
    self.board1 = [' '][' '] * 3
    
  def printBoard(self):
    print('-------------')
    print('| ' + self.board1[0][0] + ' | ' + self.board1[0][1] + ' | ' + self.board1[0][2] + ' | ')
    print('------------')
    print('| ' + self.board1[1][0] + ' | ' + self.board1[1][1] + ' | ' + self.board1[1][2] + ' | ')
    print('------------')
    print('| ' + self.board1[2][0] + ' | ' + self.board1[2][1] + ' | ' + self.board1[2][2] + ' | ')
    print('------------')

  def enterMove(self, sym, position):
    self.board1[position] = sym
    #board1.remove(postion)
    #board1.insert(postion, sym)

class Player:
  def __init__(self, id, symbol):
    self.id =id
    self.symbol = symbol
    self.move = None
    # self.name = name
         
  def getPlayerMove(self):
    self.move = int(input("Enter your move\n"))
    print(self.move)
    
    
class Game:
  def __init__(self,gameid):
      self.gameid=gameid
      board = Board()
      board.printBoard()
      player1 = Player(1,'x')
      player2 = Player(2,'o')

      while (not(winCondition(board.board1)) and not(tieCondition(board.board1))):
        player1.getPlayerMove()
        board.enterMove(player1.symbol, player1.move)
        board.printBoard()
        if (not winCondition(board.board1) and (not tieCondition(board.board1))):
          player2.getPlayerMove()
          board.enterMove(player2.symbol, player2.move)
          board.printBoard()


     
   def winCondition(self, board1):
     flag = False
      for i in range(2):
        if (board1[i][0] == board1[i][1] == board1[i][2] == 'x' or board1[0][i] == board1[1][i] == board1[2][i] == 'x' or board1[0][0] == board1[1][1] == board1[2][2] == 'x'or board1[0][2] == board1[1][1] == board1[2][0] == 'x'):
                 print('Player1 wins')
                 flag=True
        elif (board1[i][0] == board1[i][1] == board1[i][2] == 'o' or board1[0][i] == board1[1][i] == board1[2][i] == 'o' or board1[0][0] == board1[1][1] == board1[2][2] == 'o' or board1[0][2] == board1[1][1] == board1[2][0] == 'o')
                print('Player2 wins')
                flag = True
      return flag
  
  def tieCondition(self,board):
    flag = False
    for i in range(2):
      if (board1[i][0] != board1[i][1] != board1[i][2] and board1[0][i] != board1[1][i] != board1[2][i] and board1[1][1] != board1[2][2] != board1[0][0]):
                 print('Tie !!!!!!!!')
                 flag=True
    return flag

  #Call recursive;y until we reach win/tie state
  #win/tie state
  # 0 1 2
  # i0 i1 i2    | 10 11 12

  #0i 1i 2i
  #ii ii ii
  # for i from 0 to 2:
  # if i0 & i1 & i2 has same symbol || 0i 1i 2i has same sym ||
  # ii ii ii has same symbol 
  # if i0 & i1 & i2 doesnt same symbol && 0i 1i 2i doesnt has # # same sym && ii ii ii doesnt has same symbol
  # 
  #
  # Do not allow user to enter already taken position
  #Maintain a visited array

  
      


  
    
    
    
    

newGame = Game(1)

#board1 = Board()
#board2 = [' '] * 9

#board1.createBoard(board2)

