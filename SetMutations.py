length=int(raw_input())
A=set(map(int,raw_input().split()))
N=int(raw_input())

for i in range(N):
    (op,op_len)= raw_input().split()
    se=map(int,raw_input().split())
    
    if op == "intersection_update":
        A.intersection_update(se)
    elif op == "update":
        A.update(se)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(se)
    elif op == "difference_update" :
        A.difference_update(se)
        
print(sum(A))    
    
