if __name__ == '__main__':
    n = int(raw_input())
    arr = list(set(map(int,raw_input().split(" "))))

    arr.sort(reverse=True) #removed dupicated elimanates & arranged in ascending order
    print arr[1]  # Reversed & printing the secong element from the list
    
    
   