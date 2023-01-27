def s2(a,t):
    res=set()
    for i in a:
        if t-i in res:
            return (i,t-i)
        res.add(i)
    return None
