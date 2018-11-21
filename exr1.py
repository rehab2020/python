def new_list(old_list):
    b=[]
    b.append(old_list[0])
    b.append(old_list[-1])
    return b

    a=[3,5,6,2,58,9]
    b=[23,4,58,19,2874,366,27]
    c=[100,1]


    print(new_list(a))
    print(new_list(b))
    print(new_list(c))
