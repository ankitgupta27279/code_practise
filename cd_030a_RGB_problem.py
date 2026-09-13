### RGB problem

def get_RGB_1(test_str: str) -> str:
    list_R=[]
    list_G=[]
    list_B=[]
    for ch in test_str:
        if ch.upper()=="R":
            list_R.append(ch)
        elif ch.upper()=="G":
            list_G.append(ch)
        elif ch.upper()=="B":
            list_B.append(ch)
    list_R.extend(list_G)
    list_R.extend(list_B)
    return "".join(list_R)


# def get_RGB_2(test_str: str) -> str:
#     test_list=list(test_str)
    


if __name__=="__main__":
    sample_str="grgrrrgrrbbgrbrbgbr"
    print(get_RGB_1(sample_str))
