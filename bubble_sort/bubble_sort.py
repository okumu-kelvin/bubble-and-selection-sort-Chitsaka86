def bubble_sort(unsorted_list):

    for i in range(len(unsorted_list)):

        for u in range(0,len(unsorted_list)-i-1):
            if unsorted_list[u] > unsorted_list[u+1]:

                unsorted_list[u],unsorted_list[u+1]=unsorted_list[u+1],unsorted_list[u]

    # TODO: Implement bubble sort
    return unsorted_list

