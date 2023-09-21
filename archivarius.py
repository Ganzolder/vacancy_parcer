import json


class Archivist:

    file_path = 'c:/temp/my_list.json'

    def __init__(self):
        pass

    @classmethod
    def load_archive_file(cls):

        with open(cls.file_path, 'r') as file:
            data = json.load(file)

        return data

    @classmethod
    def delete_item(cls, file, item):

        deleting_item = sorted(item, reverse=True)
        file_to_delete = file
        i = 0

        for item in deleting_item:
            item -= 1
            if i == 0:
                del file_to_delete[item]
                pass
                i += 1
            else:
                del file_to_delete[item]

        return file_to_delete
