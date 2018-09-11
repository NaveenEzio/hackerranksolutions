# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(raw_input())
c=[]
i=0

for i in range(0,n):
    c.append(raw_input())
    i+=1
    

e=len(set(c))
print(e)
