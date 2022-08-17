bad_behav = ["Глебов", "Васин", "Петров", "Сидоров"]
bad_marks = ['Иванов', 'Петров', 'Сидоров', 'Мишин', 'Иванов']

# for surname in bad_behav:
#     # если surname содержится в bad_marks
#     # распечатать surname
#     if surname in bad_marks:
#         print(surname)


# Пересечение - & либо метод .intersection
# Объединение - | либо метод .union

bad_behav = set(bad_behav)
bad_marks = set(bad_marks)

## Пересечение
bad_behav.intersection(bad_marks)
# или
bad_behav & bad_marks

## Объединение
bad_behav | bad_marks
# или
bad_behav.union(bad_marks)

## Разность 
print(bad_marks - bad_behav)
