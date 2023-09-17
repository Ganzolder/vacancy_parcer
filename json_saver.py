import json


class FileSaver:
    def __init__(self, vac_list, vac_num_save):
        self.vac_list = vac_list
        self.vac_num_save = vac_num_save
        self.vac_list_to_save = []

    def get_vac_list_to_save(self):
        for i in range(len(self.vac_list)):
            i += 1
            if i in self.vac_num_save:
                self.vac_list_to_save.append(self.vac_list[i - 1])
        return self.vac_list_to_save

    def save_to_file(self):
        with open('c:/temp/my_list.json', 'r') as file:
            data = json.load(file)

        print(data)

        with open('c:/temp/my_list.json', 'a') as json_file:
            json.dump(self.vac_list_to_save, json_file)
