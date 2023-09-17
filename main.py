import json_saver
import req_API
import printer
import vac_sorter
import vac_shorter


if __name__ == '__main__':
    print('Система поиска работы с максимальной ЗП приветствует тебя, безработный!\n')

    start_choice = int(input('Введи цифру для выбора действия:\n'
          '1. Поиск вакансий\n'
          '2. Просмотр и редактирование архива ранее сохраненных вакансий\n\n'))

    if start_choice == 1:

        area = input('Введи зону поиска вакансий (Введите "Москва", '
                 'или название любой другой области "замкадья")\n').lower()
        salary = int(input('Введи размер желаемый минимальный размер оплаты труда\n'))
        key_word = input('Введи ключевое слово для поиска по вакансиям\n').lower()
        exp = int(input('Введи свой стаж (в годах)\n'))
        top_n = int(input('Сколько вывести вакансий?\n'))

        hh_vacs = req_API.HHAPI(area, salary, key_word, exp)
        vac_list = hh_vacs.get_vac_api_resp()
        sort_top_n = vac_sorter.HHSorterSalaryTopN(vac_list, salary, top_n).sort_by_salary_top_n()
        vac_list_shorted = vac_shorter.HHShorter(sort_top_n).get_short_vac()
        vacs_to_show = printer.ShowFoundedVacs(vac_list_shorted)
        vacs_to_show.show_vacs_list()

        vacs_to_save = list(map(int, input('Выберите номера вакансий чтобы сохранить (через пробел)\n').split()))

        list_for_save = json_saver.FileSaver(vac_list_shorted, vacs_to_save)
        list_for_save.get_vac_list_to_save()
        list_for_save.save_to_file()

    else:
        pass
