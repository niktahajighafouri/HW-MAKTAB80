from abc import ABC,abstractmethod


class Person(ABC):
    def __init__(self, f_name, l_name, b_year, national_id):
        self.f_name = f_name
        self.l_name = l_name
        self. full_name = f"f{f_name} {l_name}".title()
        self.b_year = b_year
        self.national_id = national_id

    @abstractmethod
    def weekly_income(self):
        pass


class Teacher(Person):
    counter = 0
    max_weekly_hour = 20
    negative_rate = 10  # more than 20 hour include negative rate

    def __init__(self, f_name, l_name, b_year, national_id, income_per_hour=2000):
        super().__init__(f_name, l_name, b_year, national_id)
        Teacher.counter += 1
        self.id = f"{Teacher.counter}-1"
        self.income_per_hour = income_per_hour

    def weekly_income(self, hour: float):
        if hour <= Teacher.max_weekly_hour:
            income = hour * self.income_per_hour
        else:
            income = Teacher.max_weekly_hour * self.income_per_hour + (hour-Teacher.max_weekly_hour)*(1 - Teacher.negative_rate/100)
        return f"{self.id}:{income}"


class Manager(Person):
    counter = 0
    max_weekly_hour = 35
    positive_rate = 20  # more than 35 hour include positive rate

    def __init__(self, f_name, l_name, b_year, national_id, income_per_hour=10000):
        super().__init__(f_name, l_name, b_year, national_id)
        Manager.counter += 1
        self.id = f"{Manager.counter}-1"
        self.income_per_hour = income_per_hour

    def weekly_income(self, hour: float):
        if hour <= Manager.max_weekly_hour:
            income = hour * self.income_per_hour
        else:
            income = Manager.max_weekly_hour * self.income_per_hour + (hour - Teacher.max_weekly_hour) * (1 + Manager.positive_rate / 100)
        return f"{self.id}:{income}"