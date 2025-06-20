def selection_sort(arr):
    s = len(arr)

    for i in range(s):

        minimum_number =i
        for n in range(i+1,s):
            if arr[n]<arr[minimum_number]:
                minimum_number= n
        if minimum_number:
         arr[i], arr[minimum_number]= arr[minimum_number], arr[i]


    return arr

