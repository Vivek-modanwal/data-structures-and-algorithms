def selectnext(board):
	for x in range(len(board)):
		if 1 not in board[x]:
			return x
	return -1

def issafe(board,row,column):
	for i in range(row-1,-1,-1):
		if board[i][column]==1:
			return False
	x=row-1
	y=column+1
	while x >=0 and y<len(board):
		if board[x][y]==1:
			return False
		x-=1
		y+=1
	x=row-1
	y=column-1
	while x >=0 and y>=0:
		if board[x][y]==1:
			return False
		x-=1
		y-=1
	return True


def Nqueensolver(board):
	row=selectnext(board)
	if row==-1:
		return True
	for column in range(len(board)):
		check=issafe(board,row,column)
		if check:
			board[row][column]=1
			nextqueen=Nqueensolver(board)
			if nextqueen:
				return True
			else:
				board[row][column]=0
		else:
			continue
	else:
		return False


def Nqueens(n):
	A=[0]*n
	board=[A.copy() for _ in range(n)]
	Nqueensolver(board)
	return board

if __name__=='__main__':
	board=Nqueens(38)
	for x in board:
		for y in x:
			print(y,end='  ')
		print()

