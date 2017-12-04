Опис функцій
============


classification_text(data) - Первірка на те чи знаходиться шаблон чи в тексті чи окремо.
find_data_in_text(text) - Пошук шаблонів які задовільняють формат дати.
valid_days_in_february(year) - Перевірка на високосний рік.
data_filter(data) - Пошук серед знайдених шаблонів тих які представляють дату.
get_str_day(day) - Повертає строкове представлення числа.
get_str_day_nominative(day) - Повертає строкове представлення числа у називному відмінку.
get_str_month(month) - Повертає строкове представлення місяця.
get_str_year(year) - Повертає строкове представлення року.
get_genitive_case_str(nominative, day, month, year) - Об'єднує число місяць і рік в одну стрічку. 
create_list_of_all_dates(nominative, text) - Створює список з усіма знайденими датами в тексті.
print_all_dates(list_dates) - Виводить на еркан список з знайденими датами в тексті.
print_in_correct_case(text) - Визначає в якому відмінку потрібно виводити дату.
