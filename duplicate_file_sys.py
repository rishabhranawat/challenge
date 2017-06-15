def findDuplicate(paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    all_paths_content = {}
    for each_path in paths:
        dets = each_path.split(" ")
        base_addr = dets[0]
        for i in range(1, len(dets), 1):
            all_dets = dets[i].split("(")
            addr = all_dets[0]
            cont = all_dets[1]
            if(cont in all_paths_content):
                all_paths_content[cont].append(base_addr+"/"+addr)
            else:
                all_paths_content[cont] = [base_addr+"/"+addr]
    ret = []
    for cont, path in all_paths_content.items():
        if(len(path) > 1):
            ret.append(path)
    return ret                
    
print(findDuplicate(['root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)', \
    'root/c/d 4.txt(efgh)', 'root 4.txt(efgh)']))