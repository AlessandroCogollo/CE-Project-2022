import array


# calculate sum of every element of an array
def sum_array(to_be_summed):
    temp = 0
    for i in range(0, len(to_be_summed)):
        temp += i
    return temp


# calculate mean values of an array
def mean(to_be_calculated):
    return sum_array(to_be_calculated) / len(to_be_calculated)


# return an array in which each element equals array[i]/int
def base_distribution(array_to_process, a):
    tmp = array.array('f', [])
    for i in range(0, len(array_to_process)):
        tmp.append(array_to_process[i] / a)
    return tmp


def array_product(array_first, array_second):
    array_to_return = {}
    for i in array_first.length:
        array_to_return[i] = array_first[i] * array_second[i]
    return array_to_return
