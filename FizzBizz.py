t=int(raw_input())

d=map(int,raw_input().split())

len=len(d)
j=0

while j<len:
    for i in range(1,d[j]+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)
    j+=1


               
                
            
        
    
