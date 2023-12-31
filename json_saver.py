import json


class FileSaver:
    '''
    Класс для сохранения в Архив с контролем уникальности вакансии по URL
    '''
    file_path = 'c:/temp/my_list.json'

    def __init__(self, vac_list, *vac_num_save):
        self.vac_list = vac_list
        self.vac_num_save = vac_num_save
        self.vac_list_to_save = []

    def get_vac_list_to_save(self):

        vacs_urls = []
        vac_arch = FileSaver.read_from_file()

        for vac in vac_arch:
            vacs_urls.append(vac[4])

        for i in range(len(self.vac_list)):
            i += 1
            if i in self.vac_num_save[0]:
                if self.vac_list[i - 1][4] not in vacs_urls:
                    vac_arch.append(self.vac_list[i - 1])
                else:
                    pass

        self.vac_list_to_save = vac_arch

        return self.vac_list_to_save

    def save_to_file(self):

        with open(self.file_path, 'w') as json_file:
            json.dump(self.vac_list_to_save, json_file)

    @classmethod
    def read_from_file(cls):

        with open(cls.file_path, 'r') as json_file:
            data = json.load(json_file)

        return data
