# a:int=5
# b:str='строчка'
# с:list=[1,2]
#
# def indent(s:str, width:int)->str:
#     return" "*(max(0,width-len(s)))+s
# print(indent('5',69))


# def append_list(my_list:list):
#     my_list.append('text')
#     return my_list
# print(append_list(['один',2,3]))


def sum_list(my_list:list)->int:
    result=0
    for elem in my_list:
        result=result+elem
    return result
print(sum_list([1,2,3]))

