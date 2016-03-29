def get_next( i ):
	return i + (-i & i)

def get_parent( i ):
	return i - (- i &i)

def update ( i , value , binex ) :
	
		while i < len( binex ) :
				print("Updating index %d by %d" % (i, value))
				binex[i] += value
				i = get_next(i) 

def get_sum ( i , j , binex ) :
		
		sum = 0

		while  j >= i :
				print("Adding %d at index %d to sum %d to yield %d" % (binex[j], j, sum, sum + binex[j])) 
				sum += binex[j]
				j = get_parent(j)

		return sum

def measure ( param, binex ) : 
		print( get_sum ( int(param[0]) , int(param[1]) , binex ) )  

def set ( param, binex ) :
		i = int( param[0] )
		value = int( param[1] )

		update ( i , value - binex[i] , binex )

def main():
	commands = {'S' :  set , 'M' : measure }

	run = True
	case = 0

	while run: 
		
			case += 1

			print("Case %d:" % case ) 

			N = int( input() )

			run = N > 0 

			binex = [0]*(N+1)

			print(binex)

			for i in range(1,N+1):
					print("Set potmeter %d to: " % i)
					update ( i , int(input()) , binex)
					print(binex)

			test = True

			while test:
			
					print("Enter command S or M")
					command = input().split(' ') 
					parameters = command[1 : len(command)] 
					command = command[0]

					if command == "END" :
							test = False
					else:
						commands[ command ]( parameters ,  binex )
					
					print(binex)

main()
