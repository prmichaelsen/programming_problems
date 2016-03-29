from sys import exit

## The code below solves Steven Halim's CP3
## potentionmeter problem (CP3 p12086)
##
## The chosen datastructure is a Fenwick tree
## or a binary index tree (binex tree)
##
## A Fenwick tree allows for efficient 
## updates of the partial sum of an array
## and efficient lookups of the partial sum
## of an array (prefix sum)
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
## node 0 is reached, summating
## partial sums along the way
def get_sum ( j , binex ) :
		
		sum = 0

		while  j > 0 :
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

def measure ( param, binex , values) : 
		
		## measure the prefix sum for the right potmeter
		sum_high = get_sum( int( param[1] ) , binex )
		
		## measure the prefix sum for the
		## left potmeter
		## $1 - 1 allows for measurement 
		## from the "left terminal"
		sum_low = get_sum( int( param[0] ) - 1 , binex )
		
		## print the values
		## this is bad practice,
		## as this method is called "measure"
		## not "measure_and_print
		print( sum_high - sum_low )  
		


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

def set ( param, binex , values) :
		
		## node to be updated
		i = int( param[0] )
		
		## new value is the value
		## to set, save old value
		## and update table of values 
		## with new value
		new_value = int( param[1] )
		old_value = values[i]
		values[i] = new_value

		## update the tree with the 
		## change in values
		update ( i , new_value - old_value , binex )

## testing utility
def print_binex ( param, binex , values) : 
		print(binex)

def quit( param, binex , values) :
		exit()

def main():

	## command map
	commands = { 
					'S' :  set ,
					'M' : measure,
					'P' : print_binex,
					'Q' : quit }

	run = True
	case = 0

	## 0 to exit run loop
	while run: 
	
			case += 1

			## input the size of next 
			## fenwick tree
			N = int( input() )

			## do not run on N = 0
			run = N > 0 
		
			## lazy loop exit
			## this is not good practice
			if(run == False):
				break

			print("Case %d:" % case ) 

			## binex is the fenwick tree
			## N+1 because binex[0] is
			## a dummy element. This is
			## similar to many implementations
			## of a binary heap
			binex = [0]*(N+1)
			
			## values is the table of values
			## it is useful to keep this
			## information as it improves
			## the implementation of the "set"
			## command
			values = [0]*(N+1)

			## read in the table of values
			for i in range(1,N+1):
					value = int( input() )
					
					## update the fenwick tree
					update ( i , value , binex)
					
					## update table of values
					values[i] = value

			test = True

			## END to exit test loop
			while test:
			
					## input next command
					command = input().split(' ') 
					parameters = command[1 : len(command)] 
					command = command[0]

					## run command if not END
					if command == "END" :
							test = False
					else:
						commands[ command ]( parameters ,  binex , values)
					
main()
