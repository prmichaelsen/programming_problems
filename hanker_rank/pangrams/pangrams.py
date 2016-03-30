## solution to hanker rank's pangram problem
## URL : https://www.hackerrank.com/challenges/pangrams/submissions/code/18846135

## Author: Patrick Michaelsen 
## Email: patrickmichaelsen@patrickmichaelsen.com
## Website: patrickmichaelsen.com
## Description : uses bitmasks to find pangram

def find( sentence ):

		## bitmask which represents 26 on bits
		## eg, one on bit for each letter of the
		## alphabet
		pan_mask = int('0b11111111111111111111111111', 2)
		sentence_mask = 0

		sentence = sentence.lower()

		## look through each letter
		## and turn on the n'th bit 
		## of sentence_mask where
		## n = letter - 'a'
		for i in range( len( sentence ) ) :
			
				current_character = sentence[i] 

				## examine only letter characters
				if 'a' <= current_character and current_character <= 'z':

						## turn on n'th bit
						sentence_mask |= 1 <<  ( ord( current_character ) - ord('a') )  

		## if pan_mask == sentence_mask then 
		## it is a pangram
		return sentence_mask == pan_mask

pangram = find ( input () ) 

if pangram:
    print( "pangram" )
else:
    print( "not pangram" )

