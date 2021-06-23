# %% Function obtain_digit
def obtain_digit(num, base,col):
    """
    Obtains specific digit of a given number. 

    :param num: An integer
    :param base: Base representation of the integer
    :param col: Position of digit to be obtained
    :return: Single digit in form of integer

    Best/Worst Time Complexity: O(1) - Arithmetic operation is constant
    Total Space Complexity: O(1) - Does not require additional memory and input is constant
    Auxiliary Space: O(1) - Does not require additional memory

    """
    return (num//base**col) % base

# %% Function radix_sort_task1_task1
def radix_sort_task1(my_list,base):
    """
    Performs radix sort on a list by comparing elements. Counting sort is utilized to compare elements 
    with its respective digits. 
    
    :param my_list: A list containing elements which are integers
    :param base: Base representation of each integers in the list
    :return: A list with elements sorted in ascending order

    Best/Worst Time Complexity: O(kN) -
    k - Number of digits of the greater number in the list
    N - Number of integers in the list (size of the list)

    Total Space Complexity: O(kN)
    Auxiliary Space: O(N)
    The input list gives a space complexity of O(kN) and each counting sort will need O(M+N) where
    M is the number of unique characters for an integer in the list. The algorithm uses a constant 
    M which represents the base. Therefore, the total space complexity is O(kN). Likewise for auxiliary, 
    since M is constant, the auxiliary space complexity is O(N). 
    """

    if len(my_list) == 0: 
        return my_list

    # Find maximum num 
    max_item = my_list[0]
    for item in my_list:
        if item > max_item:
            max_item = item 

    col = 0
    while max_item != 0:
        # Initialize count array
        count_array = [None]*(base)
        for i in range(len(count_array)):
            count_array[i] = []

        for item in my_list:
            count_array[obtain_digit(item,base,col)].append(item)
        
        # Update input array
        index = 0
        for i in range(len(count_array)): # O(1)
            item = i
            frequency = count_array[i]
            for j in range(len(frequency)):
                my_list[index] = count_array[item][j]
                index = index + 1 

        max_item = max_item//10
        col += 1

    return my_list

# %% Function group_elements
def group_elements(lst):
    """
    This function groups the same integer, process the frequency of the integer and store it in
    a list. 

    :param lst: A sorted list with elements sorted in ascending order
    :return: A 2-dimensional list consisting grouping of elements which corresponds to their frequency

    Best/Worst Time Complexity: O(N) - N is the number of elements in the list (size of the list).
    Total Space Complexity: O(N)
    Auxiliary Space: O(N)
    Input list has a space complexity of O(N). An empty list is initialized to store the groupings of elements.
    For element in the list, the function will include its corresponding frequency, which leads to O(N + N + N) total 
    space complexity. Therefore, the final total space complexity of this function is O(N).  
    """
    res = []
    pointer = lst[0]
    count = 0
    for i in range(len(lst)):
        if lst[i] != pointer: 
            temp = [pointer,count]
            pointer = lst[i]
            count = 1
            res.append(temp)
        else:
            count += 1
    
    # Add last element 
    res.append([lst[len(lst)-1],count])
    return res

# %% 
def best_interval(records,t):
    """
    This function finds the best interval with the most number of elements and the minimal start
    time. 

    :param records: Unsorted List of non-negative integers
    :param t: Non negative integer, representing length of time
    :return best_t: The time such that the interval starting at best_t and ending at best_t + t 
    contains more elements from records than any other interval of length t
    :return count: Number of elements in the interval of length t starting at best_t

    Best/Worst Time Complexity: O(nk) - 
    n - The number of elements in records
    k - The greatest number of digits in any element in records
    This function call functions radix_sort_task1 and group_elements, which has a time complexity of
    O(kn) and O(n) respectively. In a worst case scenario, each element in the list is unique. 
    Therefore, the list will go through each element at least once and during each loop, each interval 
    is unique. Thus, the complexity of the looping function is O(n). The final time complexity of this
    function is O(nk).

    Total Space Complexity: O(nk)
    Auxiliary Space: O(n) 
    This function call function radix_sort_task1 and group_elements, which have a total complexity of
    O(nk) and O(n) respectively. Both of these functions also have an auxiliary space complexity
    of O(n). Since no additional space is used in this function, the final total space complexity
    is O(nk) and the auxiliary space complexity is O(n).

    """
    # Sort it using radix sort - O(kN)
    records = radix_sort_task1(records,10)

    # Group elements together - O(N)
    count_array = group_elements(records)

    if t == 0: 
        return (count_array[0][0],count_array[0][1])

    last_item = 0
    result = 0

    i = 0
    j = 0

    check_count = 0
    while i < len(count_array):
        current = count_array[i]

        start_time = current[0]   
        end_time = start_time + t

        # Initialize k
        if i+1 < len(count_array):
            k = i + 1 

        count = 0 
        j = i
        while j < len(count_array) and count_array[j][0] <= end_time: 
            count += count_array[j][1]
            j += 1
        
        # Break when pointer j reaches last element
        if j == len(count_array): 
            break
        
        if count > result: 
            last_item = count_array[j-1][0]
            result = count
        
        # Optimize to ensure function skip intervals which are a subset of current interval
        if count_array[j][0] - count_array[k][0] > t:
            while count_array[j][0] - count_array[k][0] > t:
                k = k+1
                i = k
        else:
            i += 1

        check_count += 1

    if count > result: 
        last_item = count_array[len(count_array)-1][0]
        result = count 

    best_t = last_item - t
    if best_t < 0:
        best_t = 0
    
    return (best_t, result)