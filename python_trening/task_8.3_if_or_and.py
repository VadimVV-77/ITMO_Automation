# num = 0
# permit_print = False
# if num > 0 and permit_print:
#     print('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')

def student_runk(yer_of_study):
    if yer_of_study == 1 or yer_of_study == 2 or yer_of_study == 3 or yer_of_study == 4:
        print("Вы - бакалавр")
    elif yer_of_study in range(5,7):
        print("Вы - магистр")
    elif 7<= yer_of_study<=9:
        print("Вы - аспирант")
    else:
        print("Введите корректный год обучения")
student_runk(1)


a=-51
if a>100 or a<-100:
    print("-")
else:
    print("+")