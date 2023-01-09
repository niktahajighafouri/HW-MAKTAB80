import re
phone_format = r"^09\d{2}\s*?\d{3}\s*?\d{4}$"
phone_list = ["09132491735","+989132491735","3922581735"]

for phone in phone_list:
    if re.match(phone, phone_format):
        print(phone)
    else:
        print(f"{phone} is not valid")


