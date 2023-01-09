import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
file_handler = logging.FileHandler("person.log")
file_handler.setLevel(level=logging.DEBUG)
file_format = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(message)s")
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger.debug("Person created! {} {}".format(self.name, self.family)) # it seems to me that log level does not make sense?

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, input_age):
        try:
            if input_age <= 0:
                raise Exception("invalid age!")
        except:
            self._age=0
            logger.error("Invalid age!")  # logging only help us understand flow of code not handle errors in the code
        else:
            self._age = input_age






