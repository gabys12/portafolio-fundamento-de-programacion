lst = [31,"Python","gabriela",18]
lst_tuple = [x for x in zip(*[iter(lst)])]

print(lst_tuple)
