def distributeCandies(candies):
    types = set()
    dist = 0
    n = len(candies)/2
    N = len(candies)
    counter = 0
    while(dist < n):
    	print(counter)
    	if(candies[counter] == -1):
    		counter += 1
        	counter = N%(N+counter)-1
        else:
	        types.add(candies[counter])
	        candies[counter] = -1
	        counter += 2
	        counter = N%(N+counter)-1
	        dist += 1
	   	print(candies, counter)
  
    return len(types)

print(distributeCandies([1,1,1,1,2,2,2,3,3,3]))