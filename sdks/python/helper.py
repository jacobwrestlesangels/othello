############# HELPER FILE TO DEFINE ALL FUNCTIONS #############
# DICTIONARY THAT STORES IMPORTANT SQUARES
squares = {
  "corner": [[0,0], [0,7], [7,0], [7,7]],
  "xsquare": [[1,1], [1,6], [6,1],[6,6]],
  "csquare": [[1,0], [6,0], [0,1], [7,1],
              [0,1], [0,6], [1,0], [1,7]],
  "inwall": [[0,3], [0,4], [7,3], [7,4]],
  "outwall": [[0,2], [0,5], [7,2], [7,5]]
}
# "SEARCH" FUNCTIONS TO LOOK FOR A MOVE AROUND A STONE, 
# THEY EACH RETURN A TUPLE CONTAINING BOTH THE NUMBER OF STONES FLIPPED
# AND A LIST OF THE SQUARES CONTAINING SAID STONES
def searchLeft(s, board, player):
  if player == 1: enemy = 2 
  else: enemy=1
  i = s[1]-1
  r = 0
  path = []
  while i > 0:
        if board[s[0]][i] == enemy:
            path.append([s[0], i])
            r +=1
            i-=1
        else: break
  if r == 0 or board[s[0]][i]:
    return None
  path.append([s[0],i])
  return (r, path)

def searchUp(s, board, player):
  if player == 1: enemy = 2 
  else: enemy=1
  i = s[0]-1
  r = 0
  path = []
  while i > 0:
        if board[i][s[1]] == enemy:
            path.append([i, s[1]])
            r +=1
            i-=1
        else: break
  if r == 0 or board[i][s[1]]:
    return None
  path.append([i, s[1]])
  return (r, path)

def searchDown(s, board, player):
  if player == 1: enemy=2 
  else: enemy=1
  i = s[0]+1
  r = 0
  path = []
  while i < 7:
        if board[i][s[1]] == enemy:
            path.append([i,s[1]])
            r+=1
            i+=1
        else: break
  if r == 0 or board[i][s[1]]:
    return None
  path.append([i,s[1]])
  return (r, path)

def searchRight(s, board, player):
  if player == 1: enemy = 2 
  else: enemy=1
  i = s[1]+1
  r = 0
  path = []
  while i < 7:
        if board[s[0]][i] == enemy:
            path.append([s[0], i])
            r+=1
            i+=1
        else: break
  if r == 0 or board[s[0]][i]:
    return None
  path.append([s[0], i])
  return (r, path)

def searchUpLeft(s, board, player):
  if player == 1: enemy = 2 
  else: enemy=1
  i = s[0]-1
  j = s[1]-1
  r = 0
  path = []
  while i > 0 and j > 0:
        if board[i][j] == enemy:
            path.append([i,j])
            r+=1
            i-=1
            j-=1
        else: break
  if r == 0 or board[i][j]:
    return None
  path.append([i,j])
  return (r, path)

def searchDownLeft(s, board, player):
  if player == 1: enemy = 2 
  else: enemy = 1
  i = s[0]+1
  j = s[1]-1
  r = 0
  path = []
  while i < 7 and j > 0:
        if board[i][j] == enemy:
            path.append([i,j])
            r+=1
            i+=1
            j-=1
        else: break
  if r == 0 or board[i][j]:
    return None
  path.append([i,j])
  return (r, path)

def searchUpRight(s, board, player):
  if player == 1: enemy = 2 
  else: enemy = 1
  i = s[0]-1
  j = s[1]+1
  r = 0
  path = []
  while i > 0 and j < 7:
        if board[i][j] == enemy:
            path.append([i,j])
            r+=1
            i-=1
            j+=1
        else: break
  if r == 0 or board[i][j]:
    return None
  path.append([i,j])
  return (r, path)

def searchDownRight(s, board, player):
  if player == 1: enemy = 2 
  else: enemy=1
  i = s[0]+1
  j = s[1]+1
  r = 0
  path = []
  while i < 7 and j < 7:
        if board[i][j] == enemy:
            path.append([i,j])
            r+=1
            i+=1
            j+=1
        else: break
  if r == 0 or board[i][j]:
    return None
  path.append([i,j])
  return (r, path)

# FINDS ALL "FLANKS" OR LEGAL MOVES FROM A STONE FOR A PLAYER, RETURNS LIST OF TUPLES FROM SEARCH
def flanks(s, board, player):
  r = []
  moves = (searchLeft(s, board, player), searchUpLeft(s, board, player), searchUp(s, board, player), searchUpRight(s, board, player), 
          searchRight(s, board, player), searchDownRight(s, board, player), searchDown(s, board, player), searchDownLeft(s, board, player))
  
  # PRUNING NONE RESULTS FROM LIST OF MOVES
  for i in moves:
    if i:
      r.append(i)
  return r

# FINDS ALL MOVES FOR A PLAYER IN A POSITION
def findMoves(player, board):
  m = []
  for r in range(0, len(board)):
    for c in range(0, len(board[r])):
      if board[r][c] == player:
        m += flanks([r,c], board, player)
  return m

# "STABILITY" FUNCTIONS TO DETERMINE IF A SQUARE IS STABLE IN A SPECIFIC DIRECTION
# (BEING "STABLE" MEANS NO OPPONENT PIECE COULD TAKE IT)
def stableLeft(s, player, board):
  r = s[0]
  c = s[1]
  if (c-1 < 0): return True
  elif board[r][c-1] != player: return False 
  return stableLeft([r, c-1], player, board)

def stableUpLeft(s, player, board):
  r = s[0]
  c = s[1]
  if (c-1 < 0 or r-1 < 0): return True
  elif board[r-1][c-1] != player: return False 
  return stableUpLeft([r-1, c-1], player, board)

def stableUp(s, player, board):
  r = s[0]
  c = s[1]
  if (r-1 < 0): return True
  elif board[r-1][c] != player: return False 
  return stableUp([r-1, c], player, board)

def stableUpRight(s, player, board):
  r = s[0]
  c = s[1]
  if (r-1 < 0 or c+1 > 7): return True
  elif board[r-1][c+1] != player: return False 
  return stableUpRight([r-1, c+1], player, board)

def stableRight(s, player, board):
  r = s[0]
  c = s[1]
  if (c+1 > 7): return True
  elif board[r][c+1] != player: return False 
  return stableRight([r, c+1], player, board)

def stableDownRight(s, player, board):
  r = s[0]
  c = s[1]
  if (r+1 > 7 or c+1 > 7): return True
  elif board[r+1][c+1] != player: return False 
  return stableDownRight([r+1, c+1], player, board)

def stableDown(s, player, board):
  r = s[0]
  c = s[1]
  if (r+1 > 7): return True
  elif board[r+1][c] != player: return False 
  return stableDown([r+1, c], player, board)

def stableDownLeft(s, player, board):
  r = s[0]
  c = s[1]
  if (r+1 > 7 or c-1 < 0): return True
  elif board[r+1][c-1] != player: return False 
  return stableDownLeft([r+1, c-1], player, board)

def stableVertical(s, player, board):
  return (stableUp(s,player,board) or stableDown(s,player,board))

def stableHorizontal(s, player, board):
  return (stableLeft(s,player,board) or stableRight(s,player,board))

def stableDiagonal1(s, player, board):
  return (stableUpLeft(s,player,board) or stableDownRight(s,player,board))

def stableDiagonal2(s, player, board):
  return (stableUpRight(s,player,board) or stableDownLeft(s,player,board))

# WRAPPER FUNCTION TO DETERMINE IF A SQUARE IS STABLE FOR A PLAYER
def isStable(s, player, board):
  return (stableVertical(s,player,board) and stableHorizontal(s, player, board) and stableDiagonal1(s, player, board) and stableDiagonal2(s, player, board))

# RETURNS NUMBER OF STABLE STONES A PLAYER HAS ON THE BOARD
def numStable(player, board):
  n = 0
  for r in range(0, len(board)):
   for c in range(0, len(board[r])):
     if board[r][c] == player:
       if isStable([r,c], player, board): n+=1
  return n

# RETURNS IF A DISC IS A FRONTIER DISC OR NOT
def isFrontier(s, board):
  r = s[0]
  c = s[1]
  if not board[r][c] or r <= 0 or c <= 0 or r >= 7 or c >= 7: return False
  if not board[r+1][c]: return True
  if not board[r-1][c]: return True
  if not board[r][c+1]: return True
  if not board[r][c-1]: return True
  if not board[r+1][c+1]: return True
  if not board[r+1][c-1]: return True
  if not board[r-1][c+1]: return True
  if not board[r-1][c-1]: return True
  return False

# FUNCTIONS TO COUNT NUMBER OF FRONTIER AND INTERIOR DISCS FOR A PLAYER
def numFrontier(player, board):
  n = 0
  for r in range(0, len(board)):
   for c in range(0, len(board[r])):
     if r > 0 and c > 0 and r < 7 and c < 7 and board[r][c] == player:
       if isFrontier([r,c], board): n+=1
  return n

def numInterior(player, board):
  n = 0
  for r in range(0, len(board)):
   for c in range(0, len(board[r])):
     if r > 0 and c > 0 and r < 7 and c < 7 and board[r][c] == player:
       if not isFrontier([r,c], board): n+=1
  return n

# RETURNS HOW "CONNECTED" A PLAYERS STONES ARE, I.E HOW MANY SIDES OF YOUR 
# STONES TOUCH ANOTHER ONE OF YOUR STONES
def stoneConnectivity(player, board):
  n = 0
  for r in range(1, len(board)-1):
   for c in range(1, len(board[r])-1):
     if board[r][c] == player:
      if board[r+1][c] == player: n+=1
      if board[r-1][c] == player: n+=1
      if board[r][c+1] == player: n+=1
      if board[r][c-1] == player: n+=1
      if board[r+1][c+1] == player: n+=1
      if board[r+1][c-1] == player: n+=1
      if board[r-1][c+1] == player: n+=1
      if board[r-1][c-1] == player: n+=1
  return n

# FLIPS LIST OF SQUARES TO THE PLAYERS COLOR AND RETURNS THE NEW BOARD
def flipSquares(squares, player, board):
  for i in squares:
    board[i[0]][i[1]] = player
  return board

 # RETURNS THE NUMBER OF SQUARES NOT OCCUPIED BY EITHER PLAYER
def openSquares(board):
  n = 0
  for r in range(0, len(board)):
   for c in range(0, len(board[r])):
    if not board[r][c]: n +=1
  return n

# WEIGHS A MOVE BASED ON HOW IT WILL CHANGE THE POSITION
def weighMove(move, player, board):
  if player == 1: enemy = 2 
  else: enemy=1
  newBoard = flipSquares(move, player, board)
  # INITIALIZE WEIGHT BY MULTIPLYING THE NUMBER OF NEW STABLE SQUARES BY 100
  weight = (numStable(player, newBoard) - numStable(player, board)) * 100
  for i in move:
    if i in squares["corner"]: weight += 100
    # IF THE NEW STONE IS A C-SQUARE OR AN X-SQUARE, WEIGHT IT DOWN, 
    # UNLESS ITS STABLE, IN WHICH CASE WEIGHT IT UP
    elif i in squares["csquare"]: 
      if isStable(i,player,newBoard): weight+=10
      else: weight-=20
    elif i in squares["xsquare"]:
      if isStable(i,player,newBoard): weight+=25
      else: weight-=50
    elif i in squares["inwall"]: weight+= 5
    elif i in squares["outwall"]: weight+= 10
    else: weight -= 1.5
  # REDUCE WEIGHT FOR ALLOWING OPPONENT MOVES
  weight -= len(findMoves(player, newBoard))
  # REDUCE WEIGHT FOR INCREASING OPPONENT CONNECTIVITY, ADD WEIGHT FOR INCREASING PERSONAL CONNECTIVITY
  weight -= stoneConnectivity(enemy, newBoard) - stoneConnectivity(enemy, board)
  weight += stoneConnectivity(player, newBoard) - stoneConnectivity(player, board)
  # REDUCE WEIGHT FOR MOVES THAT INCREASE NUMBER OF FRONTIER DISCS,
  # INCREASE WEIGHT FOR MOVES THAT INCREASE NUMBER OF INTERIOR DISCS
  weight -= (numFrontier(player, newBoard) - numFrontier(player, board))
  weight += (numInterior(player, newBoard) - numInterior(player, board))
  return weight

# CALCULATE AND RETURN THE "BEST" MOVE OUT OF ALL POSSIBLE MOVES FOR A PLAYER
def findBest(player, board):
  moves = findMoves(player, board)
  weights = {}
  if not moves: return None
  for i in moves:
    # IF THERE ARE 15 OR LESS OPEN SQUARES, FLIPPING STONES IS GOOD INSTEAD OF BAD
    if openSquares(board) <=15: 
      weight = weighMove(i[1], player, board) + i[0]
    else: weight = weighMove(i[1], player, board) - i[0]
    weights[str(i[1][-1])]= weight
  print(max(weights.values()))
  return max(weights, key=weights.get)
