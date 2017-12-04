import re


num_days_in_mun = {
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def classification_text(data):
    if len(re.findall(r'[^\d -.]', data)) == 0:
        if len(re.findall(r'[\d]', data)) <= 8:
            return True
    return False


def find_data_in_text(text):
    data = re.findall(r'\b(\d{1,2})[-](\d{1,2})[-](\d{2}|\d{4})\b', text) +\
           re.findall(r'\b(\d{1,2})[.](\d{1,2})[.](\d{2}|\d{4})\b', text) +\
           re.findall(r'\b(\d{1,2})[ ](\d{1,2})[ ](\d{2}|\d{4})\b', text)
    return data


def valid_days_in_february(year):
    if year % 4 == 0:
        if year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
            return 29
    return 28


def data_filter(data):
    for i in data:
        if int(i[1]) in num_days_in_mun:
            if int(i[0]) > num_days_in_mun[int(i[1])]:
                data.remove(i)
        elif int(i[1]) == 2:
            if int(i[0]) > valid_days_in_february(int(i[2])):
                data.remove(i)
        else:
            data.remove(i)
    return data


def get_str_day(day):
    return nd.NUMBERS_DICT_GENITIVE_CASE[day] + ' '


def get_str_day_nominative(day):
    return nd.NUMBERS_DICT_NOMINATIVE[day] + ' '


def get_str_month(month):
    return nd.MONTH_DICT[month] + ' '


def get_str_year(year):
    if year <= 99:
        year += 2000
    thousands = year // 1000
    hundreds = (year % 1000) // 100
    tens = (year % 100) // 10
    ones = year % 10
    str_year = ''

    if hundreds == 0 and tens == 0 and ones == 0:
        str_year += nd.NUMBES_DICT_THOUSANDS[thousands] + ' тисячного '
    elif thousands == 0:
        pass
    elif thousands == 1:
        str_year += nd.NUMBERS_DICT[thousands] + ' тисяча '
    elif thousands in [2, 3, 4]:
        str_year += nd.NUMBERS_DICT[thousands] + ' тисячі '
    else:
        str_year += nd.NUMBERS_DICT[thousands] + ' тисяч '

    if tens == 0 and ones == 0:
        str_year += nd.NUMBERS_DICT_ONLY_HUNDREDS[hundreds] + ' '
    else:
        str_year += nd.NUMBERS_DICT_HUNDREDS[hundreds] + ' '

    if ones == 0:
        str_year += nd.NUMBERS_DICT_TENS[tens] + ' року'
    elif tens < 2:
        str_year += nd.NUMBERS_DICT_GENITIVE_CASE[tens*10+ones] + ' року'
    else:
        str_year += nd.NUMBERS_DICT_ONLY_TENS[tens] + ' '
        str_year += nd.NUMBERS_DICT_GENITIVE_CASE[ones] + ' року'
    return str_year + "\n"


def get_genitive_case_str(nominative, day, month, year):
    if nominative:
        genitive_case_str = get_str_day_nominative(int(day))
    else:
        genitive_case_str = get_str_day(int(day))
    genitive_case_str += get_str_month(int(month))
    genitive_case_str += get_str_year(int(year))
    return genitive_case_str


def create_list_of_all_dates(nominative, text):
    list_of_all_dates = []
    for i in data_filter(find_data_in_text(text)):
        list_of_all_dates.append(get_genitive_case_str(nominative, *i).split())
    return list_of_all_dates


def print_all_dates(list_dates):
    print('\n')
    if len(list_dates) == 0:
        print("Дати не знайдено")
    for i in list_dates:
        for j in i:
            print(j, end=" ")
        print('\n')


def print_in_correct_case(text):
    if classification_text(text):
        print_all_dates(create_list_of_all_dates(True, text))
    else:
        print_all_dates(create_list_of_all_dates(False, text))


if __name__ == '__main__':
    from numbers_dict import numbers_dict as nd
    data = input("Введіть стрічку у котрій потрібно знайти дату: ")
    print_in_correct_case(data)
else:
    from .numbers_dict import numbers_dict as nd
