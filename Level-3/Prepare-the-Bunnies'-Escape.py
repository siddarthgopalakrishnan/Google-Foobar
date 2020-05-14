def shortestPath(sx, sy, maze):
    width = len(maze[0])
    height = len(maze)
    new_board = [[None for i in range(width)] for i in range(height)]
    new_board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          newx, newy = x + i[0], y + i[1]
          if 0 <= newx < height and 0 <= newy < width:
            if new_board[newx][newy] is None:
                new_board[newx][newy] = new_board[x][y] + 1
                if maze[newx][newy] == 1 :
                  continue
                arr.append((newx, newy)) 
                  
    return new_board

def solution(maze):
  width = len(maze[0])
  height = len(maze)
  tb = shortestPath(0, 0, maze)
  bt = shortestPath(height-1, width-1, maze)
  new_board = []

  ans = 2 ** 32-1
  for i in range(height):
      for j in range(width):
          if tb[i][j] and bt[i][j]:
              ans = min(tb[i][j] + bt[i][j] - 1, ans)
  return ans

#maze = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #Answer 21
#maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #Answer 7
#maze = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #Answer 7
#maze = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #Answer 7
#maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #Answer 11
#print answer(maze)