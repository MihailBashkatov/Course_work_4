from classes.functionality_classes.vacancy import Vacancy
from config import platforms
from utils.utils import get_started, get_filter, get_comparison, get_sorted


def user_interaction():
    """Intersection with user.
    Covering set of question and depending on what user is answering, programme define next steps"""

    while True:

        # Defining which platform will be used: Headhunter or Superjob
        chosen_platform = get_started()

        # User inserting word, which will be used for initializing object of class Vacancy
        choose_word = input('Insert word: ').strip().lower()

        vacancy = Vacancy(choose_word)

        # Initializing search in Headhunter
        if chosen_platform == platforms[0].lower().strip():
            vacancy.initialize_vacancies_headhunter()

        # Initializing search in Superjob
        elif chosen_platform == platforms[1].lower().strip():
            vacancy.initialize_vacancies_superjob()

        # Defining where to search inserted word
        while True:
            print('\nInsert number which area you want to search')
            filter_part = input('Everywhere: [1]\nEmployee name: [2]\n'
                                'Vacancy name: [3]\n'
                                'Vacancy description: [4]\n'
                                'Check Favorites: [5]\n'
                                'Compare vacancies: [6]\nQuit: [0]\n')

            # Showing vacancies under chosen mode
            response = get_filter(filter_part, vacancy)

            # If user chose something out of proposed options, programme comes back to options
            if response == 1:
                continue

            # If user wants to compare the lowest salary level for two vacancies in Favorite
            elif response == 2:
                try:

                    # Vacancies in Favorite
                    vacancy_list = vacancy.vacancies_favorite
                    if len(vacancy_list) < 2:
                        print('\nFavorites does have less, than 2 vacancies')
                        continue
                    while True:

                        # User enters id vacancy 1
                        vacancy_1 = int(input('Make sure, that Favorites does have more than 1 vacancy'
                                              'Insert vacancy_1 ID\n If want to stop comparison, insert [3]\n'))

                        # User enters id vacancy 2
                        if vacancy_1 == 3:
                            break
                        vacancy_2 = int(input('Make sure, that Favorites does have more than 1 vacancy'
                                              'Insert vacancy_2 ID\n If want to stop comparison, insert [3]\n'))
                        if vacancy_2 == 3:
                            break

                        # Actual comparison
                        comparison = get_comparison(vacancy_list, vacancy_1, vacancy_2)
                        if type(comparison) == str:
                            print(comparison)
                            continue

                # if user inserted not digits
                except ValueError:
                    print('\nID shall be digits, not letters')
            else:
                break

        # Defining if sorting is needed. Sorting is done per vacancy name
        is_sort_data = input('Do you want to sort data? If yes, insert [1]. If no, insert [any button]')
        if is_sort_data == '1':

            # Defining sorting mode: ascending orf descending
            sort_mode = input('\nWhich order you want to sort? If Ascending, insert [1]. If Descending, insert [2]')
            get_sorted(filter_part, sort_mode, vacancy)

        # Defining if saving to Favorites is needed
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
