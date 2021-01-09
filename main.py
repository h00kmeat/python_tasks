file = open('ludi.txt', encoding='utf-8')
max_year, min_year = map(int, input('Введите максимальное значение и минимальное соответственно => ').split())
surname_count = 0
for line in file:

    years = int(line.rpartition('.')[-1])
    if years < 1978:
        surname_count += 1
        print(line.partition(' ')[0])

    if min_year <= years <= max_year:
        print(line.rpartition(' ')[0] , line.rpartition('.')[-1] )

print(surname_count, 'Жителей родившихся раньше 1978 г.')
file.close()
