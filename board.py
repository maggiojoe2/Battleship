from random import randint

def create_board():
	board = []

	for x in range(10):
		board.append(["~"] * 10)
	
	return board

def print_board(board):
	print ('          ',  " ".join(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
	for i in range(len(board)):
		print ('        ', i, " ".join(board[i]))
	# for row in board:
	# 	p_board.append(row)
	# p_board.insert(0,['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) #Add numbers
	# for i in range(len(pboard)): #add row #s
	# 	if i == 0:
	# 		p_board[i].insert(0,' ')
	# 	else:
	# 		num = str(i - 1)
	# 		p_board[i].insert(0, num)
	# for row in p_board:
	# 	print ("          ", " ".join(row))
	# return board
	#for row in board:
		#print ("          ", " ".join(row))

def rand_boat_5(board):
	#MUST BE GENERATED FIRST
	#set the 5 long boat
	row = randint(0, len(board) - 1)
	col = randint(0, len(board) - 1)
	#print(row)
	#print(col)
	#get random row and col and then check if it fits
	direction = 0
	for i in range(4):
		if i == 0:
			#check if it fits going right
			if (col + 5) < len(board):
				# print ('right')
				direction = 0
				break

		if i == 1:
			#check if it fits going down
			if (row + 5) < len(board):
				# print ('down')
				direction = 1
				break
		if i == 2:
			#check if it fits going left
			if (col - 5) >= 0:
				# print('left')
				direction = 2
				break
		if i == 3:
			#check if it fits going up
			if (row - 5) >= 0:
				# print('up')
				direction = 3
				break
	#Check direction and update board
	for i in range(5):
		if direction == 0:
			#right
			board[row][col + i] = 'C'
			# print ('right')
		if direction == 1:
			#down
			board[row + i][col] = 'C'
			# print ('down')
		if direction == 2:
			#left
			# print('left')
			board[row][col - i] = 'C'
		if direction == 3:
			#up
			# print('up')
			board[row - i][col] = 'C'
		#print_board(board)

	return board

def rand_boat_4(board):
	#set the 4 long boat
	done = 0 #Variable is 1 when spot for boat has been found
	while done != 1:
		row = randint(0, len(board) - 1)
		col = randint(0, len(board) - 1)
		# print(row)
		# print(col)
		#get random row and col and then check if it fits
		direction = 0
		for i in range(4):
			if i == 0:
				#check if it fits going right
				if (col + 4) < len(board):
					for i in range(4):
						if board[row][col + i] != '~':
							# print('doesnt fit right')
							break
					else:
						#print ('right')
						direction = 0
						done = 1
						break	

			if i == 1:	
				#check if it fits going down
				if (row + 4) < len(board):
					for i in range(4):
						if board[row + i][col] != '~':
							# print('doesnt fit down')
							break
					else:				
						#print ('down')
						direction = 1
						done = 1
						break
			if i == 2:
				#check if it fits going left
				if (col - 4) >= 0:
					for i in range(4):
						if board[row][col - i] != '~':
							# print('doesnt fit left')
							break
					else:				
						#print('left')
						direction = 2
						done = 1
						break
			if i == 3:
				#check if it fits going up
				if (row - 4) >= 0:
					for i in range(5):
						if board[row][col - i] != '~':
							# print('doesnt fit up')
							break
					else:				
						#print('up')
						direction = 3
						done = 1
						break
		
	#Check direction and update board
	for i in range(4):
		if direction == 0:
			#right
			board[row][col + i] = 'B'
			# print ('right')
		if direction == 1:
			#down
			board[row + i][col] = 'B'
			# print ('down')
		if direction == 2:
			#left
			# print('left')
			board[row][col - i] = 'B'
		if direction == 3:
			#up
			# print('up')
			board[row - i][col] = 'B'

	return board

def rand_boat_3(board):
	#set the 3 long boat
	done = 0 #Variable is 1 when spot for boat has been found
	while done != 1:
		row = randint(0, len(board) - 1)
		col = randint(0, len(board) - 1)
		# print(row)
		# print(col)
		#get random row and col and then check if it fits
		direction = 0
		for i in range(3):
			if i == 0:
				#check if it fits going right
				if (col + 3) < len(board):
					for i in range(3):
						if board[row][col + i] != '~':
							# print('doesnt fit right')
							break
					else:
						#print ('right')
						direction = 0
						done = 1
						break	

			if i == 1:	
				#check if it fits going down
				if (row + 3) < len(board):
					for i in range(3):
						if board[row + i][col] != '~':
							# print('doesnt fit down')
							break
					else:				
						#print ('down')
						direction = 1
						done = 1
						break
			if i == 2:
				#check if it fits going left
				if (col - 3) >= 0:
					for i in range(3):
						if board[row][col - i] != '~':
							# print('doesnt fit left')
							break
					else:				
						#print('left')
						direction = 2
						done = 1
						break
			if i == 3:
				#check if it fits going up
				if (row - 3) >= 0:
					for i in range(3):
						if board[row][col - i] != '~':
							# print('doesnt fit up')
							break
					else:				
						#print('up')
						direction = 3
						done = 1
						break
		
	#Check direction and update board
	for i in range(3):
		if direction == 0:
			#right
			board[row][col + i] = 'D'
			# print ('right')
		if direction == 1:
			#down
			board[row + i][col] = 'D'
			# print ('down')
		if direction == 2:
			#left
			# print('left')
			board[row][col - i] = 'D'
		if direction == 3:
			#up
			# print('up')
			board[row - i][col] = 'D'

	return board

def rand_boat_2(board):
	#set the 2 long boat
	done = 0 #Variable is 1 when spot for boat has been found
	while done != 1:
		row = randint(0, len(board) - 1)
		col = randint(0, len(board) - 1)
		# print(row)
		# print(col)
		#get random row and col and then check if it fits
		direction = 0
		for i in range(2):
			if i == 0:
				#check if it fits going right
				if (col + 3) < len(board):
					for i in range(2):
						if board[row][col + i] != '~':
							# print('doesnt fit right')
							break
					else:
						#print ('right')
						direction = 0
						done = 1
						break	

			if i == 1:	
				#check if it fits going down
				if (row + 2) < len(board):
					for i in range(2):
						if board[row + i][col] != '~':
							# print('doesnt fit down')
							break
					else:				
						#print ('down')
						direction = 1
						done = 1
						break
			if i == 2:
				#check if it fits going left
				if (col - 2) >= 0:
					for i in range(2):
						if board[row][col - i] != '~':
							# print('doesnt fit left')
							break
					else:				
						#print('left')
						direction = 2
						done = 1
						break
			if i == 3:
				#check if it fits going up
				if (row - 2) >= 0:
					for i in range(2):
						if board[row][col - i] != '~':
							# print('doesnt fit up')
							break
					else:				
						#print('up')
						direction = 3
						done = 1
						break
		
	#Check direction and update board
	for i in range(2):
		if direction == 0:
			#right
			board[row][col + i] = 'P'
			# print ('right')
		if direction == 1:
			#down
			board[row + i][col] = 'P'
			# print ('down')
		if direction == 2:
			#left
			# print('left')
			board[row][col - i] = 'P'
		if direction == 3:
			#up
			# print('up')
			board[row - i][col] = 'P'

	return board

def create_game_board():
	#generates a board with ships
	board = create_board()
	board = rand_boat_5(board)
	board = rand_boat_4(board)
	board = rand_boat_3(board)
	board = rand_boat_3(board)
	board = rand_boat_2(board)
	return board
