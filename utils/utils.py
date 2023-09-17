from config import platforms


def get_started():
    """ Defining start for user to enter search platform. User will have 3 attempts"""
    count: int = 0
    while count <= 2:
        print(f'You have {3 - count} more attempts')
        choose_platforms: str = input('Choose a platform\n').strip().lower()
        if choose_platforms == platforms[0].lower().strip():
            return choose_platforms
        elif choose_platforms == platforms[1].lower().strip():
            return choose_platforms

        else:
            count += 1
            print(count)
    print('You did not insert correct platform name. Search is over')
    quit()


def get_filter(filter_part: str, vacancy):
    """ Return shown filtered vacancies upon user's choice"""
    try:

        # If user choose to compare two vacancies
        if filter_part == '6':
            return 2

        # If user choose to finish search
        elif filter_part == '0':
            print('Search is finished. See you later')
            quit()
        filtered_vacancy = vacancy.get_show_filter(int(filter_part))

    except ValueError:
        print('\nPlease, chose among mentioned options')
        return 1
    except TypeError:
        print('\nPlease, chose among mentioned options')
        return 1
    return filtered_vacancy


def get_sorted(filter_part: str, sort_mode: str, vacancy):
    """ Return shown sorted vacancies upon user's choice. Sorting is done per vacancy name"""
    sorted_vacancy = vacancy.get_show_sorted(int(filter_part), int(sort_mode))
    return sorted_vacancy


def get_comparison(vacancy_list: list, vacancy_1: int, vacancy_2: int):
    """ Return comparison for the lowest salary level between two vacancies
        vacancy_list = vacancies in Favorites
        vacancy_1 and vacancy_2 = ids"""

    compared_vacancy = []
    for vacancy in vacancy_list:
        if vacancy_1 == vacancy.vacancy_id:
            compared_vacancy.append(vacancy)
        elif vacancy_2 == vacancy.vacancy_id:
            compared_vacancy.append(vacancy)

    # If Favorites does have less than 2 vacancies
    if len(compared_vacancy) < 2:
        return '\nOne of two vacancies or both are not in Favorites\n'

    try:
        if compared_vacancy[0].salary_from > compared_vacancy[1].salary_from:
            return (f'\nLowest salary level of {compared_vacancy[0].vacancy_name} '
                    f'higher than lowest salary level of {compared_vacancy[1].vacancy_name}\n')
        elif compared_vacancy[0].salary_from == compared_vacancy[1].vacancy_name:
            return (f'\nLowest salary level of {compared_vacancy[0].vacancy_name} '
                    f'equal to lowest salary level of {compared_vacancy[1].vacancy_name}\n')
        elif compared_vacancy[0].salary_from < compared_vacancy[1].vacancy_name:
            return (f'\nLowest salary level of {compared_vacancy[0].vacancy_name} '
                    f'less than lowest salary level of {compared_vacancy[1].vacancy_name}\n')

        # if lowest salary is not defined
    except TypeError:
        return '\nOne of two or both inserted vacancies do not have info about lowest salary level\n'
