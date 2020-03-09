def bubble_sort(a):
    l = len(a)

    arr = a
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
            yield arr

#a = [88, 55,10,9,6,2,0,-4]
#dabba = bubble_sort(a)

#print(type(dabba))
#for x in dabba:
#    print(x)