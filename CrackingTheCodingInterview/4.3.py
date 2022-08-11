def depths(tree,level,lists):
    if not tree:
        return
    
    lst = []
    if len(lists) == level:
        lst.append(tree)
        lists.append(lst)
    else:
        lst = lists[level]
        lst.append(tree)
        
    depths(tree.left,level+1,lists)
    depths(tree.right,level+1,lists)