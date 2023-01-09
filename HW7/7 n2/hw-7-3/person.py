import logging


# create logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create handeler and set level
file_handler = logging.FileHandler('person.log')
file_handler.setLevel(logging.DEBUG)

# handeler set format
file_format = logging.Formatter('%(asctime)s - %(name)-10s - %(levelname)-16s - %(message)s')
file_handler.setFormatter(file_format)

# add handeler to logger
logger.addHandler(file_handler)


class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger.info("Person created! {} {}".format(self.name, self.family))


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logger.warning("Invalid age!")
            self._age = 0

