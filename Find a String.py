def count_substring(string, sub_string):
    cnt=0
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
                    cnt += 1
    
    return cnt
