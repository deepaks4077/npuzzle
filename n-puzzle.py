import heapq
from random import shuffle

fBoard = [1,2,3
		  4,5,6
		  7,8,0]

n=3
board = [i for i in range(9)]
shuffle(board)

class Board:

	def __init__(self,boardList,cost):
		self._array = boardList
		self.heuristic = calcHeuristic(self._array)
		self.cost = cost
		self.totalCost = self.cost + self.heuristic
		self.parent = None

	def _printBoard(self):
		for var in self._array:
			if var%3==0:
				print("\n")
			else:
				print(var+", ")

	def __hash__(self):
		t = tuple(self._array)
		return hash(t)

	def __eq__(self,other):
		return self._array == other._array

def aStar():
	pq = []
	cost = {}
	visted = {}
	start = Board(board)
	end = Board(fBoard)
	heapq.push(pq,(start.totalCost,start))
	while not pq.empty():
		tmp_board = heapq.heappop(pq)
		if tmp_board.heuristic == 0:
			end = Board(tmp_board)
			break
		
		index = tmp_board._array.index(0)
		x = index/3
		y = index%3
		listOfMoves = checkMove(x,y)

		for move in listOfMoves:
			moveBoard = tmp_board._array[:]
			moveIndex = move[0]*3 + move[1]
			moveBoard[index],moveBoard[moveIndex] = moveBoard[moveIndex],moveBoard[index]
			newBoard = Board(moveBoard)
			new_cost = newBoard.totalCost
			if newBoard._array not in visited or new_cost < cost[newBoard]:
				cost[newBoard] = new_cost
				visited{newBoard} = 1
				newBoard.parent = tmp_board
				heapq.push(pq,(newBoard.totalCost,newBoard))

	while var != start:
		print(var,end="\n")
		var = var.parent


def manhattanDist(index,element):
	idx = fBoard.index(element)
	manhattan = 0
	fBoard_x = idx/3
	fBoard_x = idx%3
	x = index/3
	y = index%3
	manhattan += math.fabs(x-fBoard_x)
	manhattan += math.fabs(y-fBoard_y)
	return manhattan

		 
def calcHeuristic(array):
	boardList = array
	heuristic = 0
	for var in boardList:
		x = var/3
		y = var%3
		if fBoard.index(var) != boardList.index(var):
			heuristic+=1
		heuristic+=manhattanDist(boardList.index(var),var)
	return heuristic


def checkMove(x,y):
	listOfMoves = [[x,y]]
	if(x+1<n):
		listOfMoves.append([x+1,y])
	if(x-1>=0):
		listOfMoves.append([x-1,y])
	if(y-1>=0):
		listOfMoves.append([x,y-1])
	if(y+1<n):
		listOfMoves.append([x,y+1])

	return listOfMoves




	