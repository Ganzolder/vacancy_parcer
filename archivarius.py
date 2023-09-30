import json


class Archivist:

    file_path = 'c:/temp/my_list.json'

    def __init__(self):
        pass

    @classmethod
    def load_archive_file(cls):
        'загружаем архив'
        with open(cls.file_path, 'r') as file:
            data = json.load(file)

        return data

    @classmethod
    def delete_item(cls, file, item):

        'удаляем элемент из архива'

        deleting_item = sorted(item, reverse=True)
        file_to_delete = file
        i = 0

        for item in deleting_item:
            item -= 1
            try:
                if i == 0:
                    del file_to_delete[item]
                    pass
                    i += 1
                else:
                    del file_to_delete[item]
            except IndexError:
                print('Что-то не то ввели...')
                break

        return file_to_delete

    @classmethod
    def get_top_n_vacs_from_archive(cls, top_n_by_salary):
        '''
        Пузырьковая обратная сортировка вакансий из архива по ЗП при помощи магических методов
        '''

        import vac_creator  #импорирован здесь дабы избежать перекрестного импортирования

        top_n = int(top_n_by_salary)

        vac_list = vac_creator.create_list_of_vacs()

        n = len(vac_list)

        for i in range(n):

            for j in range(0, n - i - 1):

                if vac_list[j] < vac_list[j + 1]:
                    vac_list[j], vac_list[j + 1] = vac_list[j + 1], vac_list[j]

        return vac_list[:top_n]  #выводим только первый топ по запросу
