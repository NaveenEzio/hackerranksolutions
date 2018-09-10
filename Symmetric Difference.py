m=int(raw_input())
a=set(map(int,raw_input().strip().split(" ")))
n=int(raw_input())
b=set(map(int,raw_input().strip().split(" ")))

     
e=(a.difference(b))
f=(b.difference(a))      
g=sorted(e.union(f))     

for i in g:
    print i
      
