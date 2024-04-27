def manual_pop(lst, index=None):
    if index is None:
        return lst[:-1]  # ბოლო ელემენტის ამოშლა
    else:
        return lst[:index] + lst[index+1:]  # მინუს ინდექსის წაშლა