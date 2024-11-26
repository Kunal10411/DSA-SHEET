def count(arr):
    frequency_map={}
    
    for element in arr:
        if element in frequency_map:
            frequency_map[element]+=1

        else:
            frequency_map[element]=1
    return frequency_map

def high_low(frequency_map):
    max_freq=max(frequency_map.values())
    min_freq=min(frequency_map.values())

    high_freq_ele=[key for key, value in frequency_map.items() if value==max_freq]
    low_freq_ele=[key for key, value in frequency_map.items() if value==min_freq]

    return high_freq_ele,low_freq_ele


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

frequency_map=count(arr)    
print(f"frequency_map={frequency_map}")
hih=high_low(frequency_map)
lol=high_low(frequency_map)
print(f"highest_frequency={hih}")
print(f"lowest_frequency={lol}")