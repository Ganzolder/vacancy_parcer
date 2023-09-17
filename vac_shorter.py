class ShortedVacs:
    def shorter(self):
        pass


class HHShorter(ShortedVacs):
    def __init__(self, vac_list):
        self.vac_list = vac_list
        self.vac_list_shorted = []

    def get_short_vac(self):
        for vac in self.vac_list:

            vac_name = vac['name']
            vac_salary = vac['salary']['from']
            vac_url = vac['alternate_url']
            vac_roles = vac['snippet']['requirement']
            vac_exp = vac['experience']['name']

            self.vac_list_shorted.append([vac_name, vac_salary, vac_roles, vac_exp, vac_url])

        return self.vac_list_shorted
