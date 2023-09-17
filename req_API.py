import requests


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

    def get_exp(self):
        match int(self.vac_exp):
            case 0:
                return 'noExperience'
            case 1:
                return 'between1And3'
            case 2:
                return 'between1And3'
            case 3:
                return 'between3And6'
            case 4:
                return 'between3And6'
            case 5:
                return 'between3And6'
        if int(self.vac_exp) >= 6:
            return 'moreThan6'

    def get_area(self):

        areas = requests.get('https://api.hh.ru/areas/113').json()['areas']

        if self.area == 'Москва':
            self.area = 1
        else:
            for area in areas:
                if area['name'] == self.area:
                    self.area = area['id']
                    break

            if self.area is str:
                self.area = 113
                print(f'\nТакой регион не найден, поэтому результаты будут со всей России:\n')

        return self.area
    def get_params(self):

        params = {'text': f'NAME:{self.vac_key_word}',
                  'area': self.get_area(),
                  'salary': self.min_salary,
                  'experience': self.get_exp(),
                  'per_page': self.per_page,
                  'page':self.page
                  }
        return params

    def get_vac_api_resp(self):

        hh_list = []
        hh_pages = 0
        resp_hh = self.get_params()

        while self.page <= hh_pages:
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


