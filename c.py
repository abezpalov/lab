lys = [0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 15, 16, 18, 20]

def re_search(lys, low, hight, val):

    index = low + int(round((((hight - low) / (lys[hight] - lys[low])) * (val - lys[low]))))

    if lys[index] == val:
        return index
    elif hight - low <= 1:
        return None
    elif lys[index] < val:
        return re_search(lys, index, hight, val)
    else:
        return re_search(lys, low, index, val)

val = int(input('Введите искомое число: '))

idx = re_search(lys, 0, len(lys) - 1, val)
print(idx)
