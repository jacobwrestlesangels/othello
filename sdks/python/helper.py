# HELPER FILE TO DEFINE USEFUL FUNCTIONS
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

def flanks(s, board, player):
  r = []
  moves = (searchLeft(s, board, player), searchUpLeft(s, board, player), searchUp(s, board, player), searchUpRight(s, board, player), 
          searchRight(s, board, player), searchDownRight(s, board, player), searchDown(s, board, player), searchDownLeft(s, board, player))
  
  # PRUNING NONE RESULTS FROM LIST OF MOVES
  for i in moves:
    if i:
      r.append(i)
  return r

def findMoves(player, board):
  m = []
  for r in range(0, len(board)):
    for c in range(0, len(board[r])):
      if board[r][c] == player:
        m += flanks([r,c], board, player)
  return m

def stableLeft(s, player, board):
  r = s[0]
  c = s[1]
  if (c-1 < 0): return True
  elif board[r][c-1] != player: return False 
  return stableLeft([r, c-1], player, board)

def stableUpLeft(s, player, board):
  if player == 1: enemy = 2 
  else: enemy = 1
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

def isStable(s, player, board):
  if player == 1: enemy = 2 
  else: enemy = 1
  r = s[0]
  c = s[1]
  #if board[r][c] == enemy: return False
  return (stableVertical(s,player,board) and stableHorizontal(s, player, board) and stableDiagonal1(s, player, board) and stableDiagonal2(s, player, board))

def findStable(player, board):
    s = []
    for r in range(0, len(board)):
      for c in range(0, len(board[r])):
        if isStable([r,c], player, board):
          s.append([r,c])
    return s

def numStable(player, board):
  n = 0
  for r in range(0, len(board)):
   for c in range(0, len(board[r])):
     if board[r][c] == player:
       if isStable([r,c], player, board):
         n+=1
  return n

def flipSquares(squares, player, board):
  for i in squares:
    board[i[0]][i[1]] = player
  return board
  
def findBest(player, board):
  moves = findMoves(player, board)
  print(moves)
  m = 0
  r = []
  for i in moves:
    if m < numStable(player, flipSquares(i[1], player, board)):
        m = numStable(player, flipSquares(i[1], player, board))
        r = i[1][-1]
  if r: 
    return r
  elif moves:
    m = min(moves)[0]
    for i, move in enumerate(moves):
      if move[0] == m:
        return list(moves[i][1][-1])
  else: return None

board = [
  [0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 2], 
  [0, 0, 2, 0, 0, 0, 0, 1], 
  [0, 0, 0, 1, 0, 0, 0, 0], 
  [0, 0, 0, 1, 2, 0, 0, 0], 
  [0, 0, 0, 2, 1, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0]
  ]

print(findBest(1,board))
