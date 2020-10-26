### This is A euler phi function ###


from trial_div import fun
from functools import reduce

def IsPrime(N):

    for a in range(2,int(N**0.5)):
        if N%a!=0 :
            return True
    
    return False

#print(IsPrime(19))




def f(dt):
    #print(dt)
    
    return ([ a**dt[a]-a**(dt[a]-1) for a in dt])


#f({'a':1,'b':3,'c':1})
#f({7:2,2:2})

def phi(N):

    if len(fun(N))==1 :
        if N==1:
            return 0
        elif IsPrime(N):
            return N-1
    else:
        A={}
        for a in fun(N):
            A[a]=fun(N).count(a)
        #print(A)
        #print(reduce(lambda x,y: x*y,f(A)))
        return reduce(lambda x,y: x*y,f(A))
        
        

inp=int(input())
print(phi(inp))
  


