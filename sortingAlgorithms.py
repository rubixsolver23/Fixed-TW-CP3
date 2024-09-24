import random
import time

data_set = [round(random.random()*100, 5) for i in range(100)]

def partition(data): # This is part of quicksort
    idx_pointer = -1
    pvt_pointer = -1
    pvt = data[-1]
    for item in range(0, len(data)):
        idx_pointer += 1
        if data[idx_pointer] <= pvt:
            pvt_pointer += 1
            if idx_pointer > pvt_pointer:
                data[pvt_pointer], data[idx_pointer] = data[idx_pointer], data[pvt_pointer]
        else:
            pass
    return [data[0:pvt_pointer], data[pvt_pointer], data[pvt_pointer+1:]]

def quicksort(data):
    
    total = partition(data)
    
    if len(total[0]) > 1:
        left = quicksort(total[0])
    else:
        left = total[0]
    
    if len(total[2]) > 1:
        right = quicksort(total[2])
    else:
        right = total[2]
    
        
    return left+[total[1]]+right

def bubblesort(data):
    for h in range(len(data)-1):
        for i in range((len(data)-1)-h):
            if data[i] > data[i + 1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data

def selectionsort(data):
    pass

def othernewsort(data):
    pass






t = time.time()
sorted_set = quicksort(data_set)
timer = time.time() - t
print(timer * 1000, "ms")