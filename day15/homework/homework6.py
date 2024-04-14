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


def num_list(sia):
    len(sia)

def custom_replace(string, old, new):
    string.replace(old, new)



def custom_join(list,gamyofi=''):
    if not list:
        return ''
    
    result=str(list[0])
    for i in list[1:]:
        result += gamyofi + str(i)
        
    return result