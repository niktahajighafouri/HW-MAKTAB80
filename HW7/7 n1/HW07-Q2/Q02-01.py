import pickle
import dill


class User:
    def __init__(self, id, first_name, last_name, phone):
        self. id = id
        self.first_name = first_name
        self. last_name = last_name
        self. phone = phone

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


if __name__=="__main__":
    with open("users.pickled", "rb") as f:
        data = pickle.load(f)

#data:list
#data[i]:User
sorted_data = sorted(data, key= lambda obj : obj.id)
with open("output_q2_1.txt","a") as file:
    for obj in sorted_data:
        file.write(f"{obj}\n")
phone_filter=filter(lambda obj : obj.phone.startswith("0919"), data)
with open("output_q2_2.txt","a") as file:
    for obj in phone_filter:
        file.write(f"{obj}\n")
with open("output_q2_3.dill","ab") as file:
    for obj in data:
        dill.dump(obj.full_name(), file)

