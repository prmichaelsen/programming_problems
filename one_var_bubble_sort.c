//************************************************************************//
//	one_var_bubble_sort.c                                             //
//************************************************************************//
//									 
//	AUTHOR: 		Patrick Michaelsen
//	EMAIL: 			PatrickMichaelsen@PatrickMichaelsen.com 
//				MichaelsenPatrick@gmail.com
//	WEBSITE:		PatrickMichaelsen.com
//	
//	DESCRIPTION:		This algorithm bubble sorts an array of 
//				integers with the use of only one local 
//				variable in O(n²) time
//
//************************************************************************//

#include <stdio.h>
#include <stdlib.h> 

int main()
{

	//************************************************************************//
	//	END INITIALIZATION						  //
	//************************************************************************//
	//	This code is considered preparatory and is not
	//	part of the algorithm. 
	//************************************************************************//
   
	 int arr[10] = {5,9,1,4,7,8,6,3,2,0};
    
    	for( int k = 0; k < sizeof(arr)/sizeof(int); k++ )
      	  printf(" %d ",arr[k]);
    	printf("\n");
   
	//************************************************************************//
	//	END INITIALIZATION						  //
	//************************************************************************//
 
    	//********************// 
   	//  BEGIN ALGORITHM   //
    	//********************//
  
   	//i is the index and flag
    	int i = 1;

    	//loop while no swaps 
    	//made in last iteration
    	while ( i )
    	{ 
		//loop through list
		//to compare every pair 
    		while ( abs(i) < (sizeof(arr)/sizeof(int)) )
  		{	
			//if pair is out of order 
   			if ( arr[abs(i)-1] > arr[abs(i)] )
            		{
				//swap
                		arr[abs(i)-1] = arr[abs(i)] ^ arr[abs(i)-1];
                		arr[abs(i)]   = arr[abs(i)] ^ arr[abs(i)-1];
                		arr[abs(i)-1] = arr[abs(i)] ^ arr[abs(i)-1];
				
				//set swap flag
				i = -abs(i);
       	   		}
		
			//increment i	
			i += abs(i+1) - abs(i);
		}

		if( i == sizeof(arr)/sizeof(int) )
			i = 0;
		else if ( -i == sizeof(arr)/sizeof(int) )
			i = 1;
    }

    //********************// 
    //  END ALGORITHM     //
    //********************//

   
    printf("\n");
    for( int k = 0; k < sizeof(arr)/sizeof(int); k++ )
        printf(" %d ",arr[k]);
    printf("\n");

    return 0;
}
