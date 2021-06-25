board = [["U","R","L","P","M"], ["X","P","R","E","T"], ["G","I","A","E","T"], ["X","T","N","Z","Y"], ["X","O","Q","R","S"]]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def hasWord(y, x, word):
    if y<0 or y>4 or x<0 or x>4:
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for i in range(8):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if hasWord(new_y, new_x, word[1:]):
            return True
    return False

print(hasWord(1,1,"PRETTY"))
