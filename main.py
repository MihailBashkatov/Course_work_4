from classes.functionality_classes.vacancy import Vacancy
from config import platforms
from utils.utils import get_started, get_filter, get_comparison, get_sorted


def user_interaction():
    while True:
        chosen_platform = get_started()
        choose_word = input('Insert word: ').strip().lower()

        vacancy = Vacancy(choose_word)
        if chosen_platform == platforms[0].lower().strip():

            vacancy.initialize_vacancies_headhunter()
        elif chosen_platform == platforms[1].lower().strip():
            vacancy.initialize_vacancies_superjob()
        while True:
            print('\nInsert number which area you want to search')
            filter_part = input('Everywhere: [1]\nEmployee name: [2]\n'
                                'Vacancy name: [3]\n'
                                'Vacancy description: [4]\n'
                                'Check Favorites: [5]\n'
                                'Compare vacancies: [6]\nQuit: [0]\n')
            response = get_filter(filter_part, vacancy)
            if response == 1:
                continue
            elif response == 2:
                try:
                    vacancy_list = vacancy.vacancies_favorite
                    if len(vacancy_list) < 2:
                        print('\nFavorites does have less, than 2 vacancies')
                        continue
                    while True:
                        vacancy_1 = int(input('Make sure, that Favorites does have more than 1 vacancy'
                                              'Insert vacancy_1 ID\n If want to stop comparison, insert [3]\n'))
                        if vacancy_1 == 3:
                            break
                        vacancy_2 = int(input('Make sure, that Favorites does have more than 1 vacancy'
                                              'Insert vacancy_2 ID\n If want to stop comparison, insert [3]\n'))
                        if vacancy_2 == 3:
                            break

                        comparison = get_comparison(vacancy_list, vacancy_1, vacancy_2)
                        if type(comparison) == str:
                            print(comparison)
                            continue
                except ValueError:
                    print('\nID shall be digits, not letters')
            else:
                break

        is_sort_data = input('Do you want to sort data? If yes, insert [1]. If no, insert [any button]')
        if is_sort_data == '1':
            sort_mode = input('\nWhich order you want to sort? If Ascending, insert [1]. If Descending, insert [2]')
            get_sorted(filter_part, sort_mode, vacancy)

        save_mode = input('\nWould you like to save data? If yes, insert [1]. '
                          'If no, start again [any button] or quite [0]\n')

        if save_mode == '1':
            vacancy.save_favorite(int(filter_part), int(save_mode))
            print(f'Saved vacancies: {len(vacancy.vacancies_favorite)}')
        elif save_mode == '0':
            print('Search is over')
            quit()


if __name__ == '__main__':
    user_interaction()
