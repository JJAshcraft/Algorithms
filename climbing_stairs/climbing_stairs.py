#!/usr/bin/python

import sys


ways = []

def climbing_stairs(n): #n is the number of stairs
  #how many ways can the child climb the stairs
  #for each permutation, push to ways array
  if n == 0:
    ways.append(1)
    return ways[0]
  else:
    while n is not 0:
      for i in range(n):
        ways.append((n, n - i))
        # climbing_stairs(n - 1)
      print(ways)    
    return ways  
  #n=4 c:1,1,1,1  c:1,2,1   c:1,1,2  c:2,1,1  c:4  c:3,1   c:1,3   c:2,2



if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')