from random import randint
def create_board():
	b_row = ['~'] * 10
	b_col = [b_row] * 10
	return b_col

def print_board(board):
	for row in board:
		print (" ".join(row))

def rand_boat_5(board):
	#set the 5 long boat
	row = randint(0, len(board) - 1)
	col = randint(0, len(board) - 1)
	print(row)
	print(col)
	#get random row and col and then check if it fits
	direction = 0
	for i in range(4):
		if i == 0:
			#check if it fits going right
			if (col + 5) < len(board):
				print ('right')
				direction = 0
				break

		if i == 1:
			#check if it fits going down
			if (row + 5) < len(board):
				print ('down')
				direction = 1
				break
		if i == 2:
			#check if it fits going left
			if (col - 5) >= 0:
				print('left')
				direction = 2
				break
		if i == 3:
			#check if it fits going up
			if (row - 5) >= 0:
				print('up')
				direction = 3
				break