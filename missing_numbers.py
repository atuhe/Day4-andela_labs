# A function to define missing numbers between two lists
def missing_number(arr_A, arr_B):
    #return 0 if when the list is empty or they are equal
    if arr_A== arr_B or arr_A and arr_B == []:
        return  0
    miss = []
#loop to define missing numbers in the array_list
    for item in arr_A:
        if item not in arr_B:
            miss.append(str(item))

    for element in arr_B:
        if element not in arr_A:
            miss.append(str(element))

    return ''.join(miss)
print(missing_number([1,2,3],[1,2,3,6]))