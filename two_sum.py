list_original = [11,15,2,7]
#target = 9
"""
A soma de dois destes carinhas precisa dar 9

"""

list_original.sort() #
count= 0
for number in list_original:
    count+=1
    if list_original[0] + list_original[count] == 9:
        print(f'{list_original[0]} + {list_original[count]}')
        break
    