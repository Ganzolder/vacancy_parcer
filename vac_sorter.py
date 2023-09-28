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
