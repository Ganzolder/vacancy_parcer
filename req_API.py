import requests
import os


class VacanciesAPI:
    """Мета класс для создания классов запросов по API"""
    def get_params(self):
        pass

    def get_vac_api_resp(self):
        pass

    def conv_json(self):
        pass

    def get_vacs(self):
        pass


class HHAPI(VacanciesAPI):

    def __init__(self, area, min_salary, vac_key_word, vac_exp):
        self.area = area
        self.min_salary = min_salary
        self.vac_key_word = vac_key_word
        self.vac_exp = vac_exp
        self.per_page = 100
        self.page = 0

    def get_exp(self):
        """
        Получаем корректное значние опыта
        """
        if self.vac_exp is not None:
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
        else:
            return None

    def get_area(self):
        """
        Получаем регион для поиска
        """
        areas = requests.get('https://api.hh.ru/areas/113').json()['areas']
        search_area = self.area

        if search_area == 'Москва':
            self.area = 1
        else:
            for area in areas:
                if area['name'].lower() == self.area:
                    self.area = area['id']
                    break

            if search_area == self.area:
                self.area = 113
                print(f'\nТакой регион не найден, поэтому результаты будут со всей России:\n')

        return self.area

    def get_params(self):

        params = {'text': f'NAME:{self.vac_key_word}',
                  'area': self.get_area(),
                  'salary': self.min_salary,
                  'experience': self.get_exp(),
                  'per_page': self.per_page,
                  'page': self.page
                  }
        return params

    def get_vac_api_resp(self):

        hh_list = []
        hh_pages = 1
        resp_hh = self.get_params()

        while self.page < hh_pages:

            resp_hh['page'] = self.page
            hh_request = requests.get('https://api.hh.ru/vacancies', resp_hh)
            hh_request.close()
            hh_data = hh_request.json()

            try:
                hh_pages = hh_data['pages']
            except Exception:
                hh_pages = 0
            try:
                hh_list.extend(hh_data['items'])
            except Exception:
                hh_list.extend([])
                print(hh_list)
            self.page += 1

        return hh_list


class SJAPI(VacanciesAPI):

    def __init__(self, area, min_salary, vac_key_word, vac_exp):
        self.api_key = "".join((os.getenv('SJ_SECRET_KEY')).splitlines())
        self.area = area
        self.area_founded = self.get_area()
        self.min_salary = min_salary
        self.vac_key_word = vac_key_word
        self.vac_exp = vac_exp
        self.exp_founded = self.get_exp()
        self.page = 0
        self.first_page = self.get_sj_vacancies()

    def get_sj_vacancies(self):

        sj_api_url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'X-Api-App-Id': self.api_key,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

        if self.area.lower() == 'москва':
            payload = {
                'town': self.area,
                'payment_from': self.min_salary,
                'keyword': self.vac_key_word,
                'experience': self.exp_founded,
                'page': self.page,
                'agreement': 0
            }
        else:
            payload = {
                'o': self.area_founded,
                'payment_from': self.min_salary,
                'keyword': self.vac_key_word,
                'experience': self.exp_founded,
                'page': self.page,
                'agreement': 0
            }

        response = requests.get(sj_api_url, headers=headers, params=payload)
        response.raise_for_status()
        page_data = response.json()

        return page_data

    def get_sj_vac_list(self):
        """
        Получаем все вакансии в список
        """
        sj_vac_list = []

        try:
            get_pages_count = int(self.first_page['total']) // len(self.first_page['objects'])
            get_last_page = int(self.first_page['total']) % len(self.first_page['objects'])
        except ZeroDivisionError:
            return sj_vac_list

        if get_last_page == 0:
            pages = get_pages_count
        else:
            pages = get_pages_count + 1

        for i in range(pages):
            objects = self.get_sj_vacancies()['objects']

            for vac in range(len(objects)):
                sj_vac_list.append(objects[vac])

            self.page += 1

        return sj_vac_list

    def get_area(self):
        """
        Получаем регион для поиска
        """
        request = requests.get('https://api.superjob.ru/2.0/regions/combined/')
        search_region = self.area

        i = -1
        for region in request.json()[0]['regions']:

            i += 1
            if search_region.lower() in region['title'].lower():
                area = request.json()[0]['regions'][i]['id']
                return area

    def get_exp(self):
        """
        Получаем корректное значние опыта
        """
        match self.vac_exp:
            case 0:
                return 1
            case 1:
                return 2
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return 3
            case 5:
                return 3
            case 6:
                return 4
            case _:
                return None
