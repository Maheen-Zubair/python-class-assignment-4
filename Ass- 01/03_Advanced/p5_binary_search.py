import random
import time

def naive_search(array, target): #naive search is linear search in list
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def binary_search(array, target, low=None, high=None):  #agr functon call kia jae tu default value None hogi
    # for range search
    if low is None:  # agar user ne low nahi diya
        low = 0      # to 0 se start karo (array ke start se)

    if high is None:  # agar user ne high nahi diya
        high = len(array) - 1  # to end tak search karo

    if high < low:  #Agar low index bada ho gaya hai high index se, to iska matlab hai ke target number array mein nahi mila.
        return -1

    midpoint = (low + high) // 2

    if array[midpoint] == target:
        return midpoint
    elif target < array[midpoint]:
        return binary_search(array, target, low, midpoint - 1)
    else:
        return binary_search(array, target, midpoint + 1, high)

if __name__ == "__main__": #ye file jbh chalti he jbh is file ko run kia jata he
    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length , 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()  #time ko record karne ke liye, start wala
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()  #time ko record karne ke liye, end wala
    print("Naive search time: ", end - start , "seconds")  #for total time

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", end - start , "seconds")