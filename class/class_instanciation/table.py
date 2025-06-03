def gen(table, values):
    x = values.split('\n')
    for i in x:
        y = []
        for j in i.split(' '):
            if j.startswith('19'):
                y.append('TO_DATE(' + "'" + j + "')")
            elif j.isalpha():
                y.append("'" + j + "'")
            else:
                y.append(j)
        print(f'Insert into {table} values({", ".join(y)});')
gen('Collage','''Column
Name Data type Size
cName varchar 10
state varchar 10
enrollment int''')