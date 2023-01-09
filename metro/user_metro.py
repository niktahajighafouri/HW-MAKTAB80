import bank_account as bk
import pickle
import metro
import time
import exception as ex
import logging

# create logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create handler and set level and format
handler = logging.FileHandler('metro.log')
handler.setLevel(logging.INFO)
format = logging.Formatter('%(asctime)s - %(name) -10s - %(levelname) -10s - %(message)s')
handler.setFormatter(format)

# add handler to logger
logger.addHandler(handler)


class User:
    ''' class of metro user'''
    counter = 1000000

    def __init__(self, first_name, last_name, phone, balance) -> None:
        '''
        constructor of class User.
        :param first_name: first name of user
        :param last_name: last name of user
        :param phone: phone number of user
        :param balance: initial balance of user's bank account
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.balance = balance
        self.bank_account = bk.BankAccount(first_name, last_name, balance)
        User.counter += 1
        self.tickets = []
        self.id = f'{self.first_name}-{self.last_name}-{User.counter}'
        # recording of ticket creation in file
        logger.info(f'user <<{self.id}>> created.')
        with open('users.pickle', 'ab') as file:
            pickle.dump(self, file)
        # recording of data pickling in file
        logger.info('user <<{self.id}>> info pickled.')

    @staticmethod
    def update_pickle_buy(input_id: str, new_balance: int, ticket_id: str, file='users.pickle') -> None:
        '''
         function to update attributes of instances of class User.
        :param input_id: user id
        :param new_balance: ticket's new balance
        :param ticket_id_: ticket id
        :param file: file of pickled instances
        :return: None
        '''
        lst = []
        with open(file, 'rb') as f:
            while True:
                try:
                    instance = pickle.load(f)
                    if instance.id == input_id:
                        instance.balance = new_balance
                        instance.tickets.append(ticket_id)
                        lst.append(instance)
                    else:
                        lst.append(instance)
                except EOFError:
                    break
        with open(file, 'wb') as f:
            for i in range(len(lst)):
                pickle.dump(lst[i], f)

    @staticmethod
    def update_pickle_charge(input_id: str, user_balance: int, file='users.pickle') -> None:
        '''
        function to update instance's attributes
        :param input_id: user id
        :param user_balance: user's new balance
        :param file: file of pickled instances
        :return: None
        '''
        lst = []
        with open(file, 'rb') as f:
            while True:
                try:
                    instance = pickle.load(f)
                    if instance.id == input_id:
                        instance.balance = user_balance
                        lst.append(instance)
                    else:
                        lst.append(instance)
                except EOFError:
                    break
        with open(file, 'wb') as f:
            for i in range(len(lst)):
                pickle.dump(lst[i], f)

    @staticmethod
    def unpickle_instance(input_id: str, file='users.pickle') -> None:
        '''
        function to unpickle instances of class User
        :param input_id: user id
        :param file: file of pickled instances
        :return: None
        '''
        with open(file, 'rb') as f:
            while True:
                try:
                    instance = pickle.load(f)
                    if instance.id == input_id:
                        return instance
                except EOFError:
                    break

    def select_ticket(self) -> str:
        '''
        function to select ticket to use
        :return: ticket id
        '''
        tickets = self.tickets
        menu_user_ticket = ''
        for i in range(len(tickets)):
            menu_user_ticket = f'{menu_user_ticket} {i}) {tickets[i]}\n'
        index = int(input(f'select ticket:\n {menu_user_ticket}'))
        return tickets[index]


class Travel:
    ''' class of travel'''
    counter = 100000

    def __init__(self, origin: str) -> None:
        '''
        constructor of class Travel
        :param origin: origin of travel
        '''
        self.origin = origin
        Travel.counter += 1
        self.id = Travel.counter
        # recording of travel ordered in file
        logger.info(f'travel <<{self.id}>> ordered.')

    def travel_start(self) -> str:
        '''
        function to order travel
        :return: message of travel start
        '''
        self.travel_cost = 2500
        # recording of start of travel in file
        logger.info(f'travel <<{self.id}>> started.')
        return f'travel started at {time.localtime()[:6]} from {self.origin}'

    def travel_end(self, destination: str) -> str:
        '''
        function to close ordered travel
        :param destination: travel destination
        :return: message of end of travel
        '''
        self.travel_cost = 2000
        return f'travel ended at {time.localtime()[:6]} in {destination}'

    def payment(self, ticket) -> int:
        '''
        function of travel payment
        :param ticket: ticket to be used to travel
        :return: ticket's new balance
        '''
        # recording of end of travel in file
        logger.info(f'travel <<{self.id}>> ended.')
        if ticket.ticket_type == 'single':
            ticket.balance = metro.Single_ticket.pay_trip(ticket, self.travel_cost)
        elif ticket.ticket_type == 'credit':
            ticket.balance = metro.Credit_ticket.pay_trip(ticket, self.travel_cost)
        else:
            ticket.balance = metro.Time_Credit_ticket.pay_trip(ticket, self.travel_cost)
        return ticket.balance
