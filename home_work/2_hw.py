def task_1(a:int,b:float,c:str,d:list,e:bool)->list:
        return (("a="),a, type(a),("целое число"),
                ("b="),b, type(b),("число с плавающей точкой"),
                ("c="),c, type(c), ("строка"),
                ("d="),d, type(d),("список"),
                ("e="),e, type(e)("логический тип"))
print(task_1(1,23.4,'test',[5, 10, 'двадцать пять'],True))

def task_2(a = [1, 2, 3, 5, 8, 13, 21])->list:
        return a[0:3]
print(task_2())
task_2()
# [1, 2, 3, 5, 8, 13, 21] Числа Фибоначчи


def task_3(x:float)->float:
    return x*x
print(task_3(5.45))
