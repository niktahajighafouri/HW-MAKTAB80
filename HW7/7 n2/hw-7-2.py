import pickle
import dill


class User:

    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    @property
    def full_name(self):
        return '{}{}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return f'{self.id}: {self.first_name}{self.last_name}<{self.phone}>'


with open('users.pickled', 'rb') as f:
    data = pickle.load(f)

sorted_data = sorted(data, key=lambda obj: obj.id, reverse=False)
with open('output-q-3-1.txt', 'a') as f:
    for obj in sorted_data:
        f.write(f'{repr(obj)}\n')

filtered_data = [obj for obj in sorted_data if obj.phone.startswith('0919')]
with open('output-q-3-2.txt', 'a') as f:
    for obj in filtered_data:
        f.write(f'{repr(obj)}\n')


with open('output-q-3-q.dill', 'ab') as f:
    for obj in data:
        dill.dump(obj.full_name, f)




