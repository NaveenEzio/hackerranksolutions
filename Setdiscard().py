n = input()
s = set(map(int, raw_input().split()))
tc= int(raw_input())

for i in range(tc):
            p=raw_input().split()
            if p[0]=="remove":
                s.remove(int(p[1]))
                #print p[0]
                #print p[1]
            elif p[0]=="discard":
                s.discard(int(p[1]))
               # print p[0]
               # print p[1]
            else:
                s.pop()
        
print(sum(s))          
    
