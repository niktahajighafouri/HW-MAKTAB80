from person import Person
import logging


# create logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create handelers and set level
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.INFO)

# handelers set format
stream_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_format = logging.Formatter('%(asctime)s - %(name) -10s - %(levelname) -16s - %(msecs)03d - %(message)s')
file_handler.setFormatter(file_format)

# add handelers to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def sub(a, b):
    if b != 0:
        logger.info("a/b=" + str(a / b))
        return a / b
    logger.error("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)


def log(file_name, level):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            if level.upper() in line:
                count += 1
    return count

print(log('sample.log', 'info'))
print(log('sample.log', 'DEBUG'))
print(log('sample.log', 'ERROR'))
print(log('sample.log', 'warning'))
print(log('person.log', 'info'))
print(log('person.log', 'DEBUG'))
print(log('person.log', 'ERROR'))
print(log('person.log', 'warning'))
