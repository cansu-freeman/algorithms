def shell_sort(a, div):
    n = len(a)
    h = n//div
    
    while h > 0:
        for i in range(h, n):
            j = i
            key = a[i]
            
            while j >= h and a[j-h] > key:
                a[j] = a[j-h]
                j-=h
            
            a[j] = key

        h = h//div
    print(i, a)
