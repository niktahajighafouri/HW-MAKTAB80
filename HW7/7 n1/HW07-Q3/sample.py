from person import Person
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
file_handler = logging.FileHandler("sub.log")
file_handler.setLevel(level=logging.DEBUG)
file_format = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(msecs)-03d-%(message)s")
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(level=logging.INFO)
stream_format=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
stream_handler.setFormatter(stream_format)
logger.addHandler(stream_handler)


def sub(a, b):
    if b != 0:
        logger.debug("a/b=" + str(a / b))
        return a / b
    logger.error("Divide by zero!")


def log_level_find(file_name,level):
    count = 0
    try:
        with open(file_name) as file:
            for line in file.readlines():
                if level in line:
                    count+=1
    except:
        print("no such a file")
    else:
        return f"{level}: {count}"


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
# evaluating log_level_find function
print(f"sub.log[INFO]: {log_level_find('sub.log', 'INFO')}")
print(f"sub.log[ERROR]: {log_level_find('sub.log', 'ERROR')}")
print(f"sub.log[DeBUG]: {log_level_find('sub.log', 'DEBUG')}")
print(f"person.log[DEBUG]: {log_level_find('person.log', 'DEBUG')}")
print(f"person.log[ERROR]: {log_level_find('person.log', 'ERROR')}")
print("inavalid file name:")
log_level_find('person.lo', 'ERROR')

