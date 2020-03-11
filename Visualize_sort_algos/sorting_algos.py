def bubble_sort(a):
    l = len(a)

    arr = a
    for i in range(l):
        for j in range(0, l-i-1):
            swap = False
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
            
            yield swap, j, j+1, arr

def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        min = i
        for j in range(i+1, l):
            swap = False
            if arr[min] > arr[j]:
                arr[min], arr[j] = arr[j], arr[min]
                swap = True

            yield swap, i, j, arr

#a = [88, 55,10,9,6,2,0,-4]
#dabba = bubble_sort(a)

#print(type(dabba))
#for x in dabba:
#    print(x)