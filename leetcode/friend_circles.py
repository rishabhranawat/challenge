def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    friends = {}
    for k in range(0, len(M), 1):
        friends[(k)] = []
    
    for i in range(0, len(M), 1):
        curr_friend = (i)
        for j in range(0, len(M), 1):
            if(M[i][j] == 1):
                friends[curr_friend].append(j)
                
    circles = []
    print(friends)
    for f, m in friends.items():
        ms = set(m)
        if(len(circles) == 0):
            circles.append(m)
        else:
            found = False
            print(f, circles)
            for i in range(0, len(circles), 1):
                c = circles[i]
                if((f) in c):
                    cs = set(c)
                    circles[i] = cs or ms
                    found = True
            if(found == False):
                circles.append(m)

    return len(circles)



print(findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))

# ip = [[1,1,0],
#  [1,1,1],
#  [0,1,1]]

# print(findCircleNum(ip))
