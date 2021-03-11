import pyxel
import random

pyxel.init(48, 48, caption="Conway's game of life", fps=30)

board = []
board_change = []
run = False
gen = 0

for i in range(pyxel.width * pyxel.height):
	board.append(0)
board_change = board.copy()

def randomise():
	board.clear()
	for i in range(pyxel.width * pyxel.height):
		board.append(random.randint(0, 1))
	board_change = board.copy()
	
	
def update():
	global run, board, board_change, gen
	if pyxel.btnp(pyxel.KEY_Q):
		pyxel.quit()
	if pyxel.btnp(pyxel.KEY_R):
		randomise()
	if pyxel.btnp(pyxel.KEY_C):
		board.clear()
		for i in range(pyxel.width * pyxel.height):
			board.append(0)
		board_change = board.copy()
	if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and run == False and not pyxel.mouse_x > pyxel.width and not pyxel.mouse_y > pyxel.height:
		board.pop(pyxel.mouse_x + pyxel.width * pyxel.mouse_y)
		board.insert(pyxel.mouse_x + pyxel.width * pyxel.mouse_y, 1)
		board_change = board.copy()
	if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON) and run == False:
		board.pop(pyxel.mouse_x + pyxel.width * pyxel.mouse_y)
		board.insert(pyxel.mouse_x + pyxel.width * pyxel.mouse_y, 0)
		board_change = board.copy()
	if pyxel.btnp(pyxel.KEY_ENTER):
		run = not run
		gen = 0
		
	# cell logic
	if run or pyxel.btnp(pyxel.KEY_RIGHT):
		for c in range(len(board)):
			cell_sum = 0
			#cell_sum = board[c - 1] + board[c + 1] + board[c - pyxel.width] + board[c - pyxel.width - 1] + board[c - pyxel.width + 1] + board[c + pyxel.width] + board[c + pyxel.width + 1] + board[c + pyxel.width - 1]
			
			if not c - 1 < 0:
				cell_sum += board[c - 1]
			if not c + 1 > (len(board) - 1):
				cell_sum += board[c + 1]
			if not c - pyxel.width - 1 < 0:
				cell_sum += board[c - pyxel.width - 1]
			if not c - pyxel.width + 1 < 0:
				cell_sum += board[c - pyxel.width + 1]
			if not c + pyxel.width + 1 > (len(board) - 1):
				cell_sum += board[c + pyxel.width + 1]
			if not c + pyxel.width - 1 > (len(board) - 1):
				cell_sum += board[c + pyxel.width - 1]
			if not c - pyxel.width < 0:
				cell_sum += board[c - pyxel.width]
			if not c + pyxel.width > (len(board) - 1):
				cell_sum += board[c + pyxel.width]
			
			# rules of life
			if cell_sum < 2:
				board_change[c] = 0
			elif (board[c] == 1 and cell_sum == 2) or cell_sum == 3:
				board_change[c] = 1
			elif cell_sum > 3:
				board_change[c] = 0
			elif board[c] == 0 and cell_sum == 3:
				board_change[c] = 1
			else:
				board_change[c] = 0
		
		for p in range(len(board) - 1):
			board[p] = board_change[p]
	
		gen += 1
		#print(gen)
		
def draw():
	pyxel.cls(0)
	for y in range(pyxel.height):
		for x in range(pyxel.width):
			if board[x + pyxel.width * y] == 1:
				pyxel.pset(x, y, 7)
	# draw cursor
	pyxel.pset(pyxel.mouse_x, pyxel.mouse_y, 10)
	if run:
		pyxel.line(0, 0, pyxel.width, 0, 11)
	
pyxel.run(update, draw)