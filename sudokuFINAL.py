import collections

bottom50 = open("bot50.txt").read().split('\n')
ezpuzzles = open('easy.txt').read().split('\n')

top95 = open('top95.txt').read().split('\n')

backtracking = 0

global nbrs
nbrs = collections.OrderedDict()
matrix = collections.OrderedDict()
posse = collections.OrderedDict()

spuzzl = collections.OrderedDict()


#	puzzle = top95[x]
def readpuzzle(x):
    puzzle = bottom50[x]
    for row in range(0, 9):
        for col in range(0, 9):
		#if(puzzle[row*9+col]!= '.'):
            spuzzl[(row, col)]=puzzle[(row*9+col)]

#def getposse():
#	for row in range(0, 9):
#		for col in range(0, 9):




#for row in range(0, 9):
#	print('\n')
#	for col in range(0, 9):
#		print(matrix[(row, col)]),
#print('\n')

def getnbrs(nbrs, spuzzl, posse, matrix):
	for rr in range(0, 9):
		for cc in range(0, 9):
			matrix.clear()
			r = rr
			c = cc
			nbrs[(r, c)] = []
			for row in range(0, 9):
				for col in range(0, 9):
					(matrix[(row, col)])= '.'
			for rowrow in range(0, 9):
				matrix[(rowrow, c)] = 'X'
				nbrs[(r, c)].append((rowrow, c))
			for colcol in range(0, 9):
				matrix[(r, colcol)] = 'X'
				nbrs[(r, c)].append((r, colcol))
			matrix[(r, c)] = 'O'
			arr = nbrs[(r, c)]
			arr.remove((r, c))
			arr.remove((r, c))
			if r%3==0:
				if c%3==0:
					matrix[(r+1, c+1)] = 'X'
					matrix[(r+1, c+2)] = 'X'
					matrix[(r+2, c+1)] = 'X'
					matrix[(r+2, c+2)] = 'X'
					nbrs[(r, c)].append((r+1, c+1))
					nbrs[(r, c)].append((r+1, c+2))
					nbrs[(r, c)].append((r+2, c+1))
					nbrs[(r, c)].append((r+2, c+2))
				elif c%3==1:
					matrix[(r+1, c+1)] = 'X'
					matrix[(r+1, c-1)] = 'X'
					matrix[(r+2, c+1)] = 'X'
					matrix[(r+2, c-1)] = 'X'
					nbrs[(r, c)].append((r+1, c+1))
					nbrs[(r, c)].append((r+1, c-1))
					nbrs[(r, c)].append((r+2, c+1))
					nbrs[(r, c)].append((r+2, c-1))
				elif c%3==2:
					matrix[(r+1, c-1)] = 'X'
					matrix[(r+1, c-2)] = 'X'
					matrix[(r+2, c-1)] = 'X'
					matrix[(r+2, c-2)] = 'X'
					nbrs[(r, c)].append((r+1, c-1))
					nbrs[(r, c)].append((r+1, c-2))
					nbrs[(r, c)].append((r+2, c-1))
					nbrs[(r, c)].append((r+2, c-2))
			elif r%3==1:
				if c%3==0:
					matrix[(r+1, c+1)] = 'X'
					matrix[(r+1, c+2)] = 'X'
					matrix[(r-1, c+1)] = 'X'
					matrix[(r-1, c+2)] = 'X'
					nbrs[(r, c)].append((r+1, c+1))
					nbrs[(r, c)].append((r+1, c+2))
					nbrs[(r, c)].append((r-1, c+1))
					nbrs[(r, c)].append((r-1, c+2))
				elif c%3==1:
					matrix[(r+1, c+1)] = 'X'
					matrix[(r+1, c-1)] = 'X'
					matrix[(r-1, c+1)] = 'X'
					matrix[(r-1, c-1)] = 'X'
					nbrs[(r, c)].append((r+1, c+1))
					nbrs[(r, c)].append((r+1, c-1))
					nbrs[(r, c)].append((r-1, c+1))
					nbrs[(r, c)].append((r-1, c-1))
				elif c%3==2:
					matrix[(r+1, c-1)] = 'X'
					matrix[(r+1, c-2)] = 'X'
					matrix[(r-1, c-1)] = 'X'
					matrix[(r-1, c-2)] = 'X'
					nbrs[(r, c)].append((r+1, c-1))
					nbrs[(r, c)].append((r+1, c-2))
					nbrs[(r, c)].append((r-1, c-1))
					nbrs[(r, c)].append((r-1, c-2))
			elif r%3==2:
				if c%3==0:
					matrix[(r-2, c+1)] = 'X'
					matrix[(r-2, c+2)] = 'X'
					matrix[(r-1, c+1)] = 'X'
					matrix[(r-1, c+2)] = 'X'
					nbrs[(r, c)].append((r-2, c+1))
					nbrs[(r, c)].append((r-2, c+2))
					nbrs[(r, c)].append((r-1, c+1))
					nbrs[(r, c)].append((r-1, c+2))
				elif c%3==1:
					matrix[(r-2, c+1)] = 'X'
					matrix[(r-2, c-1)] = 'X'
					matrix[(r-1, c+1)] = 'X'
					matrix[(r-1, c-1)] = 'X'
					nbrs[(r, c)].append((r-2, c+1))
					nbrs[(r, c)].append((r-2, c-1))
					nbrs[(r, c)].append((r-1, c+1))
					nbrs[(r, c)].append((r-1, c-1))
				elif c%3==2:
					matrix[(r-2, c-1)] = 'X'
					matrix[(r-2, c-2)] = 'X'
					matrix[(r-1, c-1)] = 'X'
					matrix[(r-1, c-2)] = 'X'
					nbrs[(r, c)].append((r-2, c-1))
					nbrs[(r, c)].append((r-2, c-2))
					nbrs[(r, c)].append((r-1, c-1))
					nbrs[(r, c)].append((r-1, c-2))


def setposse(spuzzl, nbrs, posse):
    for row in range(0, 9):
        for col in range(0, 9):
            posse[(row, col)]=[]
            if((spuzzl[(row, col)])=='.'):
                for x in range(1, 10):
                    posse[(row, col)].append(str(x))


def makeposse(posse, spuzzl, nbrs):
    for x in range(0, 9):
        for y in range(0,9):
            if((len(posse[(x, y)]))>0):
                #print('a')
                for nbr in nbrs[(x, y)]:
                    if(spuzzl[nbr]!='.'):
                        kk = spuzzl[nbr]
                        #print('b')
                        if (kk in posse[(x, y)]):
                            posse[(x, y)].remove(kk)
                            #print('something')

#def getposse(spuzzl, nbrs):
 #   for row in range(0, 9):
  #      for col in range(0, 9):
   #	        posse[(row, col)] = []
    #        if((spuzzl[(row, col)])=='.')
	 #      		for(x in range(1, 10)):
	#				posse[(row, col)].append(x)
#		for row in range(0, 9):
#			print('\n')
#			for col in range(0, 9):
#				print(matrix[row, col]),
#		print('\n')

def checksolution(spuzzl):
    for row in range(0, 9):
        for col in range(0, 9):
            thetup = spuzzl[(row, col)]
            if(thetup=='.'):
                return False
            for nbr in nbrs[(row, col)]:
                if(spuzzl[nbr]==thetup):
                    return False
    return True

def chooseslot(posse):
    min = 10
    theone = (0,0)
    for key in posse:
        if(spuzzl[key]=='.' and (len(posse[key])<min)):
                min = len(posse[key])
                theone = key
    return theone


#def ordervalues(slot, posse, nbrs):
#    possibles = posse[slot]
 #   numbaofvalues = collections.OrderedDict()
#    for val in posse[slot]:
#        numbaofvalues[val] = 0
#    for nbr in nbrs[slot]:
#       for littlenumba in posse[nbr]:
#            if littlenumba in numbaofvalues:
#                numbaofvalues[littlenumba]+=1
#   sorted(numbaofvalues.values())
#    print(numbaofvalues)
#    arr = []
#    for lilvalue in numbaofvalues:
#        finalmax = max((numbaofvalues[lilvalue]))
#        arr.append(lilvalue)

#   posse[slot] = arr




def update(integer, listo):
    if(integer in listo):
        listo.remove(integer)




def printsolution(spuzzl):
    for row in range(0,9):
        print('\n')
        for col in range(0, 9):
			print spuzzl[(row, col)],



def recur(spuzzl, nbrs, posse):
    global backtracking
    if(checksolution(spuzzl)):
        printsolution(spuzzl)
        return True
    else:
        slot = chooseslot(posse)
        nbrlist = []
        #ordervalues(slot, posse, nbrs)
        for slotval in posse[slot]:
            spuzzl[slot] = slotval
            #posse[slot] = []
            nbrlist = []
            for nbr in nbrs[slot]:
                if(slotval in posse[nbr]):
                    nbrlist.append(nbr)
                    posse[nbr].remove(slotval)
               # update(slotval, posse[nbr])
            x=recur(spuzzl, nbrs, posse)
            if x: return True
            else:
                backtracking+=1
                for nbr in nbrlist:
                    posse[nbr].append(slotval)
            #
            # BACKtrack... undo update on nbrs that had slotval removed from their posse
            #
        spuzzl[slot]='.'
        return False
#return False





readpuzzle(49)
getnbrs(nbrs, spuzzl, posse, matrix)
setposse(spuzzl, nbrs, posse)
makeposse(posse, spuzzl, nbrs)

recur(spuzzl, nbrs, posse)
print('\n')
print(backtracking)


#print(chooseslot(posse)),
#spuzzl[(0,0)]='3'
#spuzzl[(0,1)]='2'
#spuzzl[(0,2)]='5'
#posse
#print(chooseslot(posse))
#print (spuzzl),
#print(nbrs[(0,0)]),
#print(posse[(0,0)])
#print(posse[(0,6)])
#ordervalues((0, 1), posse, nbrs)
#print(posse[(0,6)])
#print(posse[(0, 8)])
#print(checksolution(spuzzl))
#spuzzl[(0,0)] = '4'
#print(checksolution(spuzzl))
#spuzzl[(0,0)] = '7'
#print(checksolution(spuzzl))
#print(chooseslot(posse))
#printsolution(spuzzl)

