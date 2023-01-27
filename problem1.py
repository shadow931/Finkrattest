def lcss(s1,s2):
    m=len(s1)
    n=len(s2)
    res=0
    end=0
    len1=[[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i]==s2[j]:
                len1[i+1][j+1]=len1[i][j]+1
                if len1[i+1][j+1]>res:
                    res=len1[i+1][j+1]
                    end=i
            else:
                len1[i+1][j+1]=0
    if res==0:
        return ""
    return s1[end-res+1:end+1]
