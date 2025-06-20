def selection_sort(arr):
    s = len(arr)

    for i in range(s):

        minimum_number =i
        for n in range(i+1,s):
            if arr[n]<arr[minimum_number]:
                minimum_number= n

                arr[i], arr[minimum_number]= arr[minimum_number], arr[i]

    # TODO: Implement selection sort
    return arr

