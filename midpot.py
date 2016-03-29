##
## The code below solves Steven Halim's CP3
## potentionmeter problem (CP3 p12086)
##
## The chosen datastructure is a Fenwick tree
## or a binary index tree (binex tree)
##
## A Fenwick tree allows for efficient 
## updates of the partial sum of an array
## and efficient lookups of the partial sum
## of an array
##
## update O(log N)
## get_sum O(log N)
## build tree O(N log N)
##

## returns the next index 
def get_next( i ):
	return i + (-i & i)

## returns the parent index
def get_parent( i ):
	return i - (- i &i)

## updates the partial sum
## for all affected nodes
def update ( i , value , binex ) :
	
		while i < len( binex ) :
				binex[i] += value
				i = get_next(i) 

## traverses from node j until
## node i is reached, summating
## partial sums along the way
def get_sum ( i , j , binex ) :
		
		sum = 0

		while  j >= i :
				sum += binex[j]
				j = get_parent(j)

		return sum

## COMMANDS FOR USER: 

## defines a command for measuring
## partial sums between two potmeters
#
## USAGE: M $1 $2
#
## $1 - the index of the potmeter
## to be measured from the left
## $2 - the index of the potmeter
## to be measured from the right

def measure ( param, binex ) : 
		print( get_sum ( int(param[0]) , int(param[1]) , binex ) )  


## defines a command for setting 
## the value of a potmeter
#
## USAGE: S $1 $2
#
## $1 - the index of the potmeter
## to be set
#
## $2 - the value to set potmeter
## to

def set ( param, binex ) :
		
		i = int( param[0] )
		value = int( param[1] )

		update ( i , value - binex[i] , binex )

def main():

	## command map
	commands = {'S' :  set , 'M' : measure }

	run = True
	case = 0

	## 0 to exit run loop
	while run: 
		
			case += 1

			N = int( input() )

			run = N > 0 
		
			if(run == False):
				break

			print("Case %d:" % case ) 

			binex = [0]*(N+1)

			for i in range(1,N+1):
					update ( i , int(input()) , binex)

			test = True

			## END to exit test loop
			while test:
			
					command = input().split(' ') 
					parameters = command[1 : len(command)] 
					command = command[0]

					if command == "END" :
							test = False
					else:
						commands[ command ]( parameters ,  binex )
					
main()
