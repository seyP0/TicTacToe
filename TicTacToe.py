# Tic Tac Toe
# GrumpyOgre

import random, os, time

def IntroScreen():
	#Pre: nothing. This gets called immediately upon launch
	#Post: displays the title, pause 3 seonds, ends function
	os.system('color 3')
	print('''
    _  _____ ____  _    _     ____    ____  _  _____  _    
   / |/  __//  _ \/ \  / \ |\/ ___\  / ___\/ \/__ __\/ \ /|
   | ||  \  | | \|| |  | | //|    \  |    \| |  / \  | |_||
/\_| ||  /_ | |_/|| |  | \// \___ |  \___ || |  | |  | | ||
\____/\____\\____/\_/  \__/  \____/  \____/\_/  \_/  \_/ \|
	''')
	print('''
			Tic Tac Toe
	''')
	time.sleep(3)

def ExitScreen(Winner):
	#Pre: Check if there is 'OOO' or 'XXX' on the board 
	#	  or if all the space on the board is filled
	#Post: if'OOO' or 'XXX' on the board is made, display who wins on the screen and end the game.
	#	   if neither of player wins, then display Draw on the screen and end the game
	os.system('CLS')
	if Winner == "XXX": # jedi jEdI 
		os.system('color 2')
		print('''
     ____.          .___.__   __      __.__              ._.
    |    | ____   __| _/|__| /  \    /  \__| ____   _____| |
    |    |/ __ \ / __ | |  | \   \/\/   /  |/    \ /  ___/ |
/\__|    \  ___// /_/ | |  |  \        /|  |   |  \\___ \ \|
\________|\___  >____ | |__|   \__/\  / |__|___|  /____  >__
              \/     \/             \/          \/     \/ \/
		''')
	elif Winner == "OOO":
		os.system('color 5')
		print ('''
  _________.__  __  .__       __      __.__              ._.
 /   _____/|__|/  |_|  |__   /  \    /  \__| ____   _____| |
 \_____  \ |  \   __\  |  \  \   \/\/   /  |/    \ /  ___/ |
 /        \|  ||  | |   Y  \  \        /|  |   |  \\___ \ \|
/_______  /|__||__| |___|  /   \__/\  / |__|___|  /____  >__
        \/               \/         \/          \/     \/ \/
		''')
	else:
		os.system('color 6')
		print('''
 |  __ \                    
 | |  | |_ __ __ ___      __
 | |  | | '__/ _` \ \ /\ / /
 | |__| | | | (_| |\ V  V / 
 |_____/|_|  \__,_| \_/\_/ 
		''')

def PrintBoard():
	#Pre: nothing, when this function is called the board is displayed
	#Post: displays game board and then pauses for 1 seconds before next
	os.system('CLS')
	print('\n\t\t    Jedi Battle!!\n\n')
	print ('\t\t\t' + Board['7'] + '|' + Board['8'] + '|' + Board['9'])
	print ('\t\t\t' + '_+_+_')
	print ('\t\t\t' + Board['4'] + '|' + Board['5'] + '|' + Board['6'])
	print ('\t\t\t' + '_+_+_')
	print ('\t\t\t' + Board['1'] + '|' + Board['2'] + '|' + Board['3'])
	time.sleep(1)

def PlaceMarker(TileChosen, Marker):
	#pre: Tilechosen will be an int indicating cell chosen 
	# and marker iwll be an X or O
	#Post: the global variable Availablespaces gets edited
	Board[TileChosen] = Marker
	global AvailableSpaces 
	AvailableSpaces = AvailableSpaces.replace(TileChosen, '')
	print(AvailableSpaces)
	time.sleep(1)

def Turn(WhoseTurn):
	#PRe: WhoseTurn is a string that is either 'player' or 'computer'
	# we have a different set of code for each of these contingencies
	#Post: The 
	if (WhoseTurn=='player'):
		TileChosen = '-1'
		while TileChosen not in AvailableSpaces:
			TileChosen = input('\n\nIt is your turn. \nUse the numberpad to place your mark: ')
		PlaceMarker(TileChosen, 'X')
	elif (WhoseTurn == 'computer'):
		TileChosen = random.choice(AvailableSpaces)
		TileChosen = PlaySmart(AvailableSpaces)
		print('The Computer has played: ', TileChosen)
		PlaceMarker(TileChosen, 'O')
	time.sleep(1.5)
	PrintBoard()

def CheckWinner():
	#Pre: Check the board if 'OOO' or 'XXX' is made.
	#Post: If 'OOO' or 'XXX' is made, return the display of who wins and end the game
	#	   if neither of player wins and the board is filled, display Draw and end the game
	#	   During the game, display 'NoWinnerYet' until someone wins or the board is filled

	Row1 = Board['7']+Board['8']+Board['9']
	Row2 = Board['4']+Board['5']+Board['6']
	Row3 = Board['1']+Board['2']+Board['3']
	
	Col1 = Board['7']+Board['4']+Board['1']
	Col2 = Board['8']+Board['5']+Board['2']
	Col3 = Board['9']+Board['6']+Board['3']
	
	Dia1 = Board['7']+Board['5']+Board['3']
	Dia2 = Board['9']+Board['5']+Board['1']
	
	#Part 1 code
	Together = [Row1, Row2, Row3, Col1, Col2, Col3, Dia1, Dia2]
	
	for ele in Together: # Who wins, computer? or human player?
		if ele == "OOO" or ele == "XXX":
			return ele #Game ends
			
	if len(AvailableSpaces) == 0: # Nobody wins, Draw
		ExitScreen('Draw')
		quit() #Game ends
		
	else: # Still playing, no wins or draw
		print('NoWinnerYet')
		return
		
def PlaySmart(AvailableSpaces):
	#Pre: Check the board if there is ' XX', 'X X', 'XX ' made
	#	   so that computer blocks the human player to win.
	#Post: Go through each row, col and dia 
	#		find the index of a space if there is one of ' XX', 'X X', 'XX '.
	#		After finding the index of the space, place ComputerMarker in the index of space
	#		Place ComputerMarker when ' OO', "O O", "OO " so that computer can win. 


	Row1 = Board['7']+Board['8']+Board['9']
	Row2 = Board['4']+Board['5']+Board['6']
	Row3 = Board['1']+Board['2']+Board['3']
	
	Col1 = Board['7']+Board['4']+Board['1']
	Col2 = Board['8']+Board['5']+Board['2']
	Col3 = Board['9']+Board['6']+Board['3']
	
	Dia1 = Board['7']+Board['5']+Board['3']
	Dia2 = Board['9']+Board['5']+Board['1']
	#Part 2 code
	R1 = ['7', '8', '9']
	R2 = ['4', '5', '6']
	R3 = ['1', '2', '3']
	
	C1 = ['7', '4', '1']
	C2 = ['8', '5', '2']
	C3 = ['9', '6', '3']
	
	D1 = ['7', '5', '3']
	D2 = ['9', '5', '1']
	
	# List of markers in each Row, Col and Dia
	Together = [Row1, Row2, Row3, Col1, Col2, Col3, Dia1, Dia2]

	# List of position # of each Row, Col and Dia
	KEY = [R1, R2, R3, C1, C2, C3, D1, D2]
	
	
	ComputMarker = [" OO", "O O", "OO "]
	PlayMarker = [' XX', 'X X', 'XX ']
	PosIndex = 0 # Determine where the markers above are in Together list
	PosSpace = 0 # index position of a space
	TileChosen = ''
	for i in range(len(Together)): 
		if Together[i] in ComputMarker:
			# Computer looks for any ComputMarker on the board first
			#	this will raise the chance for computer to win. 
			PosSpace = list(Together[i]).index(' ')
			PosIndex = i
			TileChosen = KEY[PosIndex][PosSpace]
			return TileChosen
			
		elif Together[i] in PlayMarker:
			# After checking for ComputMarker, then check for PlayMarker on the board
			#	to block the human player to win. 
			PosSpace = list(Together[i]).index(' ')
			PosIndex = i
			TileChosen = KEY[PosIndex][PosSpace]
			return TileChosen
	
	# When there is no markers like above,
	# computer picks a random number to put its marker
	if TileChosen == '':
		TileChosen = random.choice(AvailableSpaces)
	return TileChosen

# Global Declarations and Storage Space
PlayerMarker = 'X'
ComputerMarker = 'O'
AvailableSpaces = '123456789'

Board = {'7':' ', '8':' ','9':' ',
		'4':' ', '5':' ','6':' ',
		'1':' ', '2':' ','3':' '}

IntroScreen()
CoinToss = random.choice('12')

if CoinToss == 1: Turn('player')


while len(AvailableSpaces) > 0:
	PrintBoard()
	
	# Computer Turn
	Win = CheckWinner()
	if Win == "XXX" or Win == "OOO":
		break	
	Turn('computer')
	
	# Player Turn
	Win = CheckWinner()
	if Win == "XXX" or Win == "OOO":
		break
	Turn('player')
	
ExitScreen(Win)

