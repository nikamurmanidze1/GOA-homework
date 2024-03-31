def luwebi(sia):
    result = 0
    for i in range(0,len(sia), 2):
        result += sia[i]
    return result


def luwebi(sia):
    luwi = 0
    kenti = 0
    for i in sia:
        if i % 2 == 0:
            luwi += i
        else:
            kenti += i
    return luwi,kenti
sia = [1,2,3,4,5]
print(luwebi(sia))
