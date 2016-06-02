from board import *
def play_game():
	game_over = 'n'
	ai_hp = 1
	ai_board = create_game_board()
	#print_board(ai_board) #FIXME

	user_board = create_board()
	print('   Here is your game board used for finding the AI\'s battleships: \n')
	print_board(user_board)
	while game_over != 'y':
		guess_row = len(ai_board)
		guess_col = len(ai_board)
		print(' ')
		#get user input and make sure it isn't invalid (outside board or already guessed)
		while guess_row not in range(len(ai_board)) or guess_col not in range(len(ai_board)):
			guess_row = int(input('   Input row to fire at: '))
			guess_col = int(input('   Input column to fire at: '))
			ai_location = ai_board[guess_row][guess_col]
			user_location = user_board[guess_row][guess_col]
			if guess_row not in range(len(ai_board)) or guess_col not in range(len(ai_board)):
				print('   Oops, that\'s not even in the ocean!')
			elif user_location is not '~':
				print('   You have already fired there.')
				guess_row = len(ai_board)
				guess_col = len(ai_board)

		print(ai_board[guess_row][guess_col])
		if ai_location is not '~':
			print('\n   Hit!\n')
			user_board[guess_row][guess_col] = 'X'
			hp -= 1
		else:
			print('\n   Miss\n')
			user_board[guess_row][guess_col] = 'O'
		print_board(user_board)
		print('\n \n') #FIXME
		print_board(ai_board) #FIXME
		if ai_hp == 0:
			print("\n    You win!")
			break
		game_over = input('Enter \"y\" to quit: ')




