def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    pairs = {}
    for letter in s:
        if(letter in pairs):
            pairs[letter] += 1
        else:
            pairs[letter] = 1
    vals = []
    for key,value in pairs.items():
        vals.append((key, value))
    
    for i in range(0, len(vals), 1):
        min_val = vals[i]
        for j in range(i, len(vals), 1):
            if min_val[1]<vals[j][1]:
                min_val = vals[j]
                vals[j] = vals[i]
                vals[i] = min_val
    ret_str = ""
    for each in vals:
        ret_str+= each[1]*each[0]
    return ret_str

print(frequencySort("tree"))