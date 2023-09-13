import requests
import json

class Vacancies_API:

    def get_params(self):
        pass

    def get_vac_api_resp(self):
        pass

    def conv_json(self):
        pass

    def get_vacs(self):
        pass


class HH_API(Vacancies_API):

    def __init__(self, area, min_salary, vac_key_word, vac_exp):
        self.area = area
        self.min_salary = min_salary
        self.vac_key_word = vac_key_word
        self.vac_exp = vac_exp
        self.per_page = 100
        self.page = 0

    def get_params(self):
        params = {'text': f'NAME:{self.vac_key_word}',
                  'area': self.area,
                  'salary': self.min_salary,
                  'experience': self.vac_exp,
                  'per_page': self.per_page,
                  'page':self.page
                  }
        return params

    def get_vac_api_resp(self):

        hh_list = []
        hh_pages = 0

        while self.page <= hh_pages:
            resp_hh = self.get_params()
            hh_request = requests.get('https://api.hh.ru/vacancies', resp_hh)
            hh_request.close()
            hh_data = hh_request.json()

            try:
                hh_pages = hh_data['pages']
            except Exception:
                hh_pages = 1
            try:
                hh_list.extend(hh_data['items'])
            except Exception:
                hh_list.extend([])
            self.page += 1

        return hh_list


class VacSorter:

    def sort_by_salary(self):
        pass

    def sort_top_n(self):
        pass


class HHSorterSalaryTopN(VacSorter):

    def __init__(self, vac_list, sort_salary, sort_top_n):
        self.vac_list = vac_list
        self.sort_result = []
        self.sort_salary = sort_salary
        self.sort_by_top_n = sort_top_n

    def sort_by_salary_top_n(self):

        for vac in self.vac_list:
            if vac['salary'] is not None:
                # print(vac)

                try:
                    if vac['salary']['from'] >= self.sort_salary:
                        self.sort_result.append(vac)
                except Exception:
                    pass

                try:
                    if vac['salary']['to'] <= self.sort_salary:
                        pass
                except Exception:
                    pass

        sorted_top_n = sorted(self.sort_result, key=lambda x: x['salary']['from'], reverse=True)[:self.sort_by_top_n]

        return sorted_top_n


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


class FileSaver():
    def __init__(self, vac_list):
        self.vac_list = vac_list

    def save_to_file(self):
        with open('c:/temp/my_list.json', 'w') as json_file:
            json.dump(self.vac_list, json_file)


class ShowFoundedVacs:
    def __init__(self, founded_vacs_dict):
        self.founded_vacs_dict = founded_vacs_dict

    def show_vacs_list(self):
        i = 0
        for vac in self.founded_vacs_dict:
            i += 1
            print(f'{i}. {vac[0]}, ЗП от {vac[1]}, требования: {vac[2]}, опыт: {vac[3]}, подробнее: {vac[4]}\n')


hh_vacs = HH_API(1, 30000, 'python', 'between1And3')
vac_list = hh_vacs.get_vac_api_resp()
sort_top_n = HHSorterSalaryTopN(vac_list, 100000, 5).sort_by_salary_top_n()

vac_list_shorted = HHShorter(sort_top_n).get_short_vac()
json_file = FileSaver(vac_list_shorted)

FileSaver.save_to_file(json_file)

vacs_to_show = ShowFoundedVacs(vac_list_shorted)

vacs_to_show.show_vacs_list()

#print(sort_top_n)


#print(vac_list[3]['salary']['from'])
'''if __name__ == '__main__':
    print_hi('PyCharm')
'''
# print(f'\n{len(hh_list)}\n')

