# Enter your code here. Read input from STDIN. Print output to STDOUT

t=int(raw_input()) #no of test cases

for i in  range(t):  #iterate through test case
    alen=int(raw_input())
    a=set(map(int,raw_input().split()))
    blen=int(raw_input())
    b=set(map(int,raw_input().split()))
    print(a.issubset(b))
