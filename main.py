import json_saver
import req_API
import printer
import vac_sorter
import vac_shorter
import archivarius


if __name__ == '__main__':

    def start_menu():

        print('Система поиска работы с максимальной ЗП приветствует тебя, безработный!\n')

        start_choice = int(input('Введи цифру для выбора действия:\n'
              '1. Поиск вакансий\n'
              '2. Просмотр и редактирование архива ранее сохраненных вакансий\n'
              '0. Для завершения работы\n'))

        return start_choice

    start_choice = start_menu()

    while start_choice != 0:

        match start_choice:
            case 1:
                area = input('Введи зону поиска вакансий (Введите "Москва", '
                         'или название любой другой области "замкадья")\n').lower()
                salary = int(input('Введи размер желаемый минимальный размер оплаты труда\n'))
                key_word = input('Введи ключевое слово для поиска по вакансиям\n').lower()
                exp = int(input('Введи свой стаж (в годах)\n'))
                top_n = int(input('Сколько вывести вакансий с каждого сайта? (headhunter.ru и superjob.ru)\n'))

                hh_vacs = req_API.HHAPI(area, salary, key_word, exp)
                vac_list = hh_vacs.get_vac_api_resp()
                sort_top_n = vac_sorter.HHSorterSalaryTopN(vac_list, salary, top_n).sort_by_salary_top_n()
                vac_list_shorted = vac_shorter.HHShorter(sort_top_n).get_short_vac()

                sj_search = req_API.SJAPI(area, salary, key_word, exp)
                sj_vac_list = sj_search.get_SJ_vac_list()
                sj_short_vac_list = vac_shorter.SJShorter(sj_vac_list).get_short_vac()
                sj_sorted = vac_sorter.SJSorterSalaryTopN(sj_short_vac_list, salary, top_n).sort_by_salary_top_n()

                hh_sj_vac_list = []
                for i in range(top_n):
                    hh_sj_vac_list.append(vac_list_shorted[i])
                for i in range(top_n):
                    hh_sj_vac_list.append(sj_sorted[i])

                vacs_to_show = printer.ShowFoundedVacs(hh_sj_vac_list)
                vacs_to_show.show_vacs_list()

                vacs_to_save = list(map(int, input('Выбери номера вакансий чтобы сохранить (через пробел)\n').split()))

                list_for_save = json_saver.FileSaver(hh_sj_vac_list, vacs_to_save)
                list_for_save.get_vac_list_to_save()
                list_for_save.save_to_file()

                back_to_menu = int(input('Введи 0 если хочешь вернуться в меню'
                                     'или нажми Enter для продолжения поиска вакансий\n'))

                if back_to_menu == 0:
                    start_choice = 3

            case 2:
                vacs_to_delete = 1

                archived_vacs = archivarius.Archivist.load_archive_file()

                while vacs_to_delete != 0:
                    arch_vacs_to_show = printer.ShowFoundedVacs(archived_vacs)
                    arch_vacs_to_show.show_vacs_list()

                    vacs_to_delete = list(map(int, input('Выбери номера вакансий чтобы удалить из архива (через пробел)\n'
                                                         'или введи 0, чтобы вернуться в предыдущее меню\n').split()))
                    if 0 in vacs_to_delete:

                        cleared_list_for_save = json_saver.FileSaver(archived_vacs)
                        cleared_list_for_save.vac_list_to_save = archived_vacs
                        cleared_list_for_save.save_to_file()

                        vacs_to_delete = 0
                        start_choice = 3

                    else:
                        archived_vacs = archivarius.Archivist.delete_item(archived_vacs, vacs_to_delete)

            case _:
                start_choice = start_menu()
