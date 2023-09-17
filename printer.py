class ShowFoundedVacs:
    def __init__(self, founded_vacs_dict):
        self.founded_vacs_dict = founded_vacs_dict

    def show_vacs_list(self):

        i = 0
        for vac in self.founded_vacs_dict:
            i += 1
            print(f'{i}. {vac[0]}, ЗП от {vac[1]}, требования: {vac[2]}, опыт: {vac[3]}, подробнее: {vac[4]}\n')
