def selection_sort_pattern_1(data_list):
    count = 0
    for x in range(len(data_list)):
        min_value = min(data_list[count:])
        index_value= data_list.index(min_value)
        data_list[count] , data_list[index_value]=min_value ,data_list[count]
        count+=1
    print(data_list)


#Below is another pattern

def selection_sort_pattern_2(data_list):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data_list[j]<data_list[min_index]:
                min_index=j
        data_list[i] , data_list[min_index] = data_list[min_index],data_list[i]
    print(data_list)
        

selection_sort_pattern_1([10,44,26,23,89,54,67,39])
selection_sort_pattern_2([10,44,26,23,89,54,67,39])

#[10, 23, 26, 39, 44, 54, 67, 89]
# [10, 23, 26, 39, 44, 54, 67, 89]