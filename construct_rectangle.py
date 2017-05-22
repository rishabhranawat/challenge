def constructRectangle(area):
    """
    :type area: int
    :rtype: List[int]
    """
    pairs = []
    for i in range(1, area+1, 1):
        if(area % i == 0):
            if(i >= area/i):
                pairs.append((i, area/i))
    
    min_pair = None
    min_pair_dist = 10000001
    for pair in pairs:
        dist = abs(pair[0] - pair[1])
        if(dist < min_pair_dist):
            min_pair_dist = dist
            min_pair = pair
    return min_pair

def constructRectangle2(area):
    """
    :type area: int
    :rtype: List[int]
    """
    min_pair = None
    min_pair_dist = 10000001
    for i in range(1, (area+1)/2+1, 1):
        if(area % i == 0):
            w = i
            l = area/i
            if(l >= w):
                dist = abs(l - w)
                if(dist < min_pair_dist):
                    min_pair_dist = dist
                    min_pair = (l, w)
    return min_pair
print(constructRectangle2(9999994))