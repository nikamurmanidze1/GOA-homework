def manual_count(lst, element=None):
    if element is None:
        return int(sum(lst) / len(lst))  # საშუალო არითმეტიკული
    else:
        count = 0
        for el in lst:
            if el == element:
                count += 1
        return count