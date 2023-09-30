
class VacCreator:
    '''
    Класс для создания вакансий и сравнения или сортировки их по зп
    '''
    def __init__(self, vac_name, salary, reqs, exp, url):
        self.vac_name = vac_name
        self.salary = salary
        self.reqs = reqs
        self.exp = exp
        self.url = url

    def __gt__(self, other):
        if isinstance(other, VacCreator):
            return self.salary > other.salary
        return False

    def __ge__(self, other):
        if isinstance(other, VacCreator):
            return self.salary >= other.salary
        return False

    def __lt__(self, other):
        if isinstance(other, VacCreator):
            return self.salary < other.salary
        return False

    def __le__(self, other):
        if isinstance(other, VacCreator):
            return self.salary <= other.salary
        return False

    def __str__(self):
        return f'{self.vac_name}, {self.salary}, {self.reqs}, {self.exp}, {self.url}'

def create_list_of_vacs():
    '''
    Метод создающий циклом все экземпляры вакансии в архиве
    '''

    import archivarius #импорирован здесь дабы избежать перекрестного импортирования

    vacs = []

    vac_list = archivarius.Archivist.load_archive_file()

    for i in range(len(vac_list)):
        vac = VacCreator(vac_list[i][0], vac_list[i][1], vac_list[i][2], vac_list[i][3], vac_list[i][4])
        vacs.append(vac)

    return vacs






