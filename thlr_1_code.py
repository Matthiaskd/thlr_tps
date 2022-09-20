#[Q9]
def union(E,F):
    res=set()
    for i in (F):
        res.add(i)
    for j in (E):
        res.add(j)
    return res
#[/Q9]
E={1,2,3,4,7}
F={3,4,5,6}

#[Q10]
def inter(E,F):
    res=set()
    for x in E:
        for y in F:
            if x==y:
                res.add(x)
    return res
#[/Q10]

#[Q11]
def substraction(E,F):
    res=set()
    f=list(F)
    len_f=len(F)
    for e in E:
        i=0
        while (i<len_f and f[i]!=e):
            i+=1
        if(i==len_f):
            res.add(e)
    return res

#[/Q11]

#[Q12]
def diff(E,F):
    return union(substraction(E,F),substraction(F,E))
#[/Q12]


#[Q13]
def sublists(l):
    if (len(l)==0):
        return [[]]
    else:
        aux=sublists(l[1:])
        res=[]
        for i in aux:
            res.append(i)
            res.append([l[0]]+i)
        return res


#[/Q13]

#[Q14]
def power_set(E):
    aux=[]
    for i in E:
        aux.append(i)
    aux2=sublists(aux)
    for i in range(len(aux2)):
        aux2[i]=set(aux2[i])
    return aux2
#[/Q14]
