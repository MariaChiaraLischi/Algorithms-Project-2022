# Use this file to implement your own utils

##### HERE YOU CAN ADD YOUR UTILITY FUNCTIONS / OBJECT / CLASSES #####

def Merge(Aleft, Aright, Nleft, Nright):

    left_index, right_index = 0, 0
    Aresult = []
    Nresult = []
    
    while left_index < len(Aleft) and right_index < len(Aright):
        if Aleft[left_index] < Aright[right_index]:
            Aresult.append(Aleft[left_index])
            Nresult.append(Nleft[left_index])
            left_index += 1
        else:
            Aresult.append(Aright[right_index])
            Nresult.append(Nright[right_index])
            right_index += 1

    Aresult += Aleft[left_index:]
    Aresult += Aright[right_index:]
    
    Nresult += Nleft[left_index:]
    Nresult += Nright[right_index:]
    
    return [Aresult, Nresult]


def MergeSort(array, names):

    if len(array) <= 1:
        return [array, names]

    half = len(array) // 2
    left = MergeSort(array[:half], names[:half])
    right = MergeSort(array[half:], names[half:])
    
    Aleft = left[0]
    Aright = right[0]
    
    Nleft = left[1]
    Nright = right[1]

    return Merge(Aleft, Aright, Nleft, Nright)


def AlphaMerge(left, right):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def AlphaMergeSort(array):

    if len(array) <= 1:
        return array

    half = len(array) // 2
    left = AlphaMergeSort(array[:half])
    right = AlphaMergeSort(array[half:])

    return AlphaMerge(left, right)
