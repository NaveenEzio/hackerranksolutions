def swap_case(s):
    c=[]
    e=''
    for i in s:
        c.append(i)
    
    for j in c:
        if(j.isupper()==True):
            e+=j.lower()
        else:
            e+=j.upper()    
            
        
        
        
    return e
