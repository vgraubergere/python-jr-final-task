employee_list = [
    {'name': 'Roberts', 'surname': 'Bralis', 'entry_year': 2017, 'city': 'Ventspils'},
    {'name': 'Andrejs', 'surname': 'Frisfelds', 'entry_year': 2011, 'city': 'Riga'},
    {'name': 'Ervins', 'surname': 'Grinfelds', 'entry_year': 2011, 'city': 'Riga'},
    {'name': 'Jane', 'surname': 'Smith', 'entry_year': 2019, 'city': 'Tallinn'},
    {'name': 'John', 'surname': 'Doe', 'entry_year': 2020, 'city': 'Skopje'}
]


# 1.Get bosses

def get_bosses(full_list):
    new_list = []
    for index in full_list:
        if index['name'] == 'Andrejs' and index['surname'] == 'Frisfelds' \
                or index['name'] == 'Ervins' and index['surname'] == 'Grinfelds':
            new_list.append(index)

    return new_list


# 2.Sort by year


def get_employees_by_year(full_list, year):
    year_check = 0
    for index in full_list:
        if index['entry_year'] == year:
            print(index)
        else:
            year_check += 1

    if year_check == len(full_list):
        raise Exception("Entry year didn't return any employees!")

# 3.Add new employee


def add_new_employee(full_list, name, surname):
    new_employee = {'name': name, 'surname': surname}
    full_list.append(new_employee)

    return full_list


# 4. Print only employees


def print_all_employees(full_list):
    for index in full_list:
        if index['name'] == 'Andrejs' and index['surname'] == 'Frisfelds' \
                or index['name'] == 'Ervins' and index['surname'] == 'Grinfelds':
            pass
        else:
            print(
                f'[Employee] name: {index["name"]}, '
                f'surname: {index["surname"]}, '
                f'started working in: {index["entry_year"]}')


# 5. Print all


def print_all(full_list):
    for index in full_list:
        if index['name'] == 'Andrejs' and index['surname'] == 'Frisfelds' \
                or index['name'] == 'Ervins' and index['surname'] == 'Grinfelds':
            print(f'[Boss] name: {index["name"]}, '
                  f'surname: {index["surname"]}')
        else:
            print(
                f'[Employee] name: {index["name"]}, '
                f'surname: {index["surname"]}, '
                f'started working in: {index["entry_year"]}')


# 6. Print employees by city

def print_employees_by_city(full_list, city):
    for index in full_list:
        if index["city"] == city:
            print(index)
