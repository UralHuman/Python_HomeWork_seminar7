# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1,num_rows+1):
#         for j in range(1,num_columns+1):
#             print('{:>2}'.format(i*j), end=' ')
#         print()
# def operation(a=int(input('Введите номер строки: ')),b=int(input('Ввеите номер столбца: '))):
#     print(f'Запрашеваемый элемент: {a*b}')

# print_operation_table(operation(),6,6)

def operation(a=int(input('Введите номер строки: ')),b=int(input('Ввеите номер столбца: '))):
    return a * b

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1,num_rows+1):
        for j in range(1,num_columns+1):
            print('{:>2}'.format(i*j), end=' ')
        print()
    print(f'Запрашеваемый элемент = {operation()}')

print_operation_table(operation)