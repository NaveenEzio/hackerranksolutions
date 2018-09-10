m=int(raw_input())
a=set(map(int,raw_input().strip().split(" ")))  #getting input by including space & removing duplicate elements
n=int(raw_input())
b=set(map(int,raw_input().strip().split(" ")))

     
e=(a.difference(b))  # Find Difference A & b elements present in a but not in b
f=(b.difference(a))      
g=sorted(e.union(f))     #sort using Ascending Order

for i in g:
    print i               #print the sorted elements
      
