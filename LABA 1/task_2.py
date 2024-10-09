
inf_v_disk=1.44 # mbite
kolvo_str=100
str=50
kolvo_symbol=25


disk_bite=1.44*1024**2#перевод дискеты в байты

ves_bite= kolvo_str*str*kolvo_symbol*4#общее кол-во сиволов в байтах

result=int(disk_bite//ves_bite)

print("Количество книг, помещающихся на дискету:",result)



