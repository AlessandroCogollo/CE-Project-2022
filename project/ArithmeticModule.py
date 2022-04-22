import array


class ArithmeticModule:

    # calculate sum of every element of an array
    @staticmethod
    def sum(to_be_summed):
        temp = 0
        for i in range(0, len(to_be_summed)):
            temp += i
        return temp

    # calculate mean values of an array
    @staticmethod
    def mean(to_be_calculated):
        return sum(to_be_calculated) / len(to_be_calculated)

    # return an array in which each element equals array[i]/int
    @staticmethod
    def base_distribution(array_to_process, a):
        tmp = array.array('f', [])
        for i in range(0, len(array_to_process)):
            tmp.append(array_to_process[i] / a)
        return tmp
