# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
c=set(map(int,raw_input().split(" ")))
e=int(raw_input())
d=set(map(int,raw_input().split(" ")))

h=c.union(d)

print(len(h))
