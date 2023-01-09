import datetime as dt
import time
import exception as ex
import pickle
import logging

# create logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create handeler and set level
file_handler = logging.FileHandler('metro.log')
file_handler.setLevel(logging.INFO)

# handeler set format
file_format = logging.Formatter('%(asctime)s - %(name) -10s - %(levelname) -10s - %(message)s')
file_handler.setFormatter(file_format)

# add handeler to logger
logger.addHandler(file_handler)


class Ticket:
    ''' class of metro ticket'''
    travel_cost = 2500

    def __init__(self, ticket_type: str, balance: int = 2500, expire_date: int = None) -> None:
        '''
        constractor for class Ticket.
        :param ticket_type: type of thicket.
        :param balance: initial balance of ticket.
        :param expire_date: expire date of ticket.
        '''
        self.ticket_type = ticket_type
        self.issue_date = dt.date.today()
        self.balance = balance
        self.expire_date = expire_date
        self.id = f'{self.ticket_type}-{self.issue_date}-{time.localtime()[3]}-{time.localtime()[4]}-{time.localtime()[5]}'
        # recording of ticket creation in file
        logger.info(f'ticket <<{self.id}>> issued.')
        # pickling of ticket information in file
        with open('cards.pickle', 'ab') as file:
            pickle.dump(self, file)
        # recording of data pickling in file
        logger.info(f'ticket <<{self.id}>> info pickled.')

    def __repr__(self) -> dict:
        '''
        function to show instance's attributes.
        :return: ticket attributes.
        '''
        return str(vars(self))

    @staticmethod
    def update_pickle(input_id: str, new_balance: int, file='cards.pickle') -> None:
        '''
        function to update of attribute of instances of class Ticket.
        :param input_id: ticket's id.
        :param new_balance: ticket's new balance.
        :param file: file of pickled instances.
        :return: None.
        '''
        lst = []
        with open(file, 'rb') as f:
            while True:
                try:
                    instance = pickle.load(f)
                    if instance.id == input_id:
                        instance.balance = new_balance
                        lst.append(instance)
                    else:
                        lst.append(instance)
                except EOFError:
                    break
        with open(file, 'wb') as f:
            for i in range(len(lst)):
                pickle.dump(lst[i], f)

    @staticmethod
    def unpickle_instance(input_id: str, file='cards.pickle'):
        '''
        function to unpickle instances of class Ticket.
        :param input_id: ticket id.
        :param file: file of pickled instances.
        :return: instance of class Ticket.
        '''
        with open(file, 'rb') as f:
            while True:
                try:
                    instance = pickle.load(f)
                    if instance.id == input_id:
                        return instance
                except EOFError:
                    print('invalid id!')
                    break
        new_id = input('enter your ID: ')
        User.unpickle_instance(new_id)


class Single_ticket(Ticket):
    ''' class of one travel ticket'''

    def pay_trip(self, travel_cost: int) -> int:
        '''
        function for travel payment.
        :param travel_cost: travel cost.
        :return: ticket balance after payment.
        '''
        self.balance -= travel_cost
        Ticket.update_pickle(self.id, self.balance)
        print(f'current credit is: {self.balance}')
        logger.info(f'ticket <<{self.id}>> used.')
        return self.balance


class Credit_ticket(Ticket):
    ''' class of credit ticket'''

    def pay_trip(self, travel_cost: int) -> int:
        '''
        function for travel payment.
        :param travel_cost: travel cost.
        :return: ticket balance after payment.
        '''
        self.balance -= travel_cost
        Ticket.update_pickle(self.id, self.balance)
        print(f'current credit is: {self.balance}')
        logger.info(f'ticket <<{self.id}>> used.')
        return self.balance

    def charge(self, amount: int) -> int:
        '''
        function to charge ticket.
        :param amount: charge amount.
        :return: ticket's new balance.
        '''
        self.balance += amount
        Ticket.update_pickle(self.id, self.balance)
        print(f'card {self.id} charged.')
        print(f'Current Credit: {self.balance}')
        logger.info(f'ticket <<{self.id}>> charged.')
        return self.balance


class Time_Credit_ticket(Credit_ticket):
    ''' class of time-credit ticket'''

    def pay_trip(self, travel_cost: int) -> int:
        '''
        function for travel payment.
        :param travel_cost: travel cost.
        :return: ticket balance after payment.
        '''
        self.balance -= travel_cost
        Ticket.update_pickle(self.id, self.balance)
        print(f'current credit: {self.balance}')
        logger.info(f'ticket <<{self.id}>> used.')
        return self.balance

    def charge(self, amount: int) -> int:
        '''
        function to charge ticket.
        :param amount: charge amount.
        :return: ticket's new balance.
        '''
        self.balance += amount
        Ticket.update_pickle(self.id, self.balance)
        print(f'card {self.id} charged')
        print(f'Current Credit: {self.balance}')
        logger.info(f'ticket <<{self.id}>> charged.')
        return self.balance
