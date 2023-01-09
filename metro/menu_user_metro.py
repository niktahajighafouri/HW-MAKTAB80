import exception as ex
import user_metro as um
from bank_account import BankAccount
import metro
import datetime as dt
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

Menu = '''
1) register
2) buy ticket
3) charge ticket
4) travel order
5) charge bank account
6) Exit
'''

menu_ticket_type = '''
1) single
2) credit
3) time/credit
'''

menu_time_credit = '''
1) 3 mounths
2) 6 mounths
3) 12 mounths
'''

charge_menu1 = '''
10000
20000
30000
'''

charge_menu2 = '''
5 
10
15
'''

while True:
    option = int(input(f'select desired option: {Menu}'))
    try:
        if option not in {1, 2, 3, 4, 5, 6}:
            raise ex.Metro_Exception('Input', 'wrong number entered!')
    except ex.Metro_Exception as err:
        print(err)
        logger.warning('incorrect option selected.')
    else:
        if option == 1:
            print('enter your information:')
            firstName = input('first name: ')
            lastName = input('last name: ')
            phone = input('phone number: ')
            balance = int(input(f'enter your initial balance ( > {BankAccount.min_balance}): '))
            try:
                if balance < BankAccount.min_balance:
                    raise ex.Metro_Exception('Input', 'wrong entered amount!')
            except ex.Metro_Exception as err:
                print(err)
            else:
                user = um.User(firstName, lastName, phone, balance)
                print('your information successfully registered.')
                print('your identification code is:')
                print('ID: ', user.id)
        elif option == 2:
            userID = input('enter your ID: ')
            user = um.User.unpickle_instance(userID)
            try:
                if not isinstance(user, um.User):
                    raise ex.Metro_Exception('Id', 'ID not found!')
            except ex.Metro_Exception as err:
                print(err)
            else:
                type = int(input(f'select ticket type: {menu_ticket_type}'))
                try:
                    if type not in {1, 2, 3}:
                        raise ex.Metro_Exception('Input', 'wrong number entered!')
                except ex.Metro_Exception as err:
                    print(err)
                    logger.warning('incorrect option selected.')
                else:
                    ticket_type = 'single' if type == 1 else 'credit' if type == 2 else 'time/credit'
                    if ticket_type == 'single':
                        try:
                            if 2500 > (user.balance - BankAccount.min_balance):
                                raise ex.Metro_Exception('balance', 'balance is not sufficient!')
                        except ex.Metro_Exception as err:
                            print(err)
                        else:
                            ticket = metro.Single_ticket('single')
                            user.balance = BankAccount.Withdrawal(user.bank_account, 2500)
                            um.User.update_pickle_buy(userID, user.balance, ticket.id)
                    elif ticket_type == 'credit':
                        initial_balance = int(input('enter initial balance: '))
                        try:
                            if initial_balance > (user.balance - BankAccount.min_balance):
                                raise ex.Metro_Exception('balance', 'balance is not sufficient!')
                        except ex.Metro_Exception as err:
                            print(err)
                        else:
                            ticket = metro.Credit_ticket('credit', initial_balance)
                            user.balance = BankAccount.Withdrawal(user.bank_account, initial_balance)
                            um.User.update_pickle_buy(userID, user.balance, ticket.id)
                    elif ticket_type == 'time/credit':
                        initial_balance = int(input('enter initial balance: '))
                        try:
                            if initial_balance > (user.balance - BankAccount.min_balance):
                                raise ex.Metro_Exception('balance', 'balance is not sufficient!')
                        except ex.Metro_Exception as err:
                            print(err)
                        else:
                            type = int(input(f'select ticket type: {menu_time_credit}'))
                            try:
                                if type not in {1, 2, 3}:
                                    raise ex.Metro_Exception('Input', 'wrong number entered!')
                            except ex.Metro_Exception as err:
                                print(err)
                                logger.warning('unsuccessful buy operation due to wrong option selected!')
                            else:
                                time = 3 if type == 1 else 6 if type == 2 else 12
                                exp_date = dt.date.today() + dt.timedelta(days=time * 30)
                                ticket = metro.Time_Credit_ticket('time/credit', initial_balance, exp_date)
                                user.balance = BankAccount.Withdrawal(user.bank_account, initial_balance)
                                um.User.update_pickle_buy(userID, user.balance, ticket.id)
        elif option == 3:
            userID = input('enter your ID: ')
            user = um.User.unpickle_instance(userID)
            try:
                if not isinstance(user, um.User):
                    raise ex.Metro_Exception('Id', 'ID not found!')
            except ex.Metro_Exception as err:
                print(err)
                logger.warning('incorrect user id entered!')
            else:
                ticket_id = um.User.select_ticket(user)
                ticket = metro.Ticket.unpickle_instance(ticket_id)
                if ticket.ticket_type == 'credit':
                    print(f'Current Credit: {ticket.balance}')
                    try:
                        amount = int(input(f'how much do you want to charge: {charge_menu1}'))
                        if amount not in {10000, 20000, 30000}:
                            raise ex.Metro_Exception('Input', 'wrong number entered!')
                    except ex.Metro_Exception as err:
                        print(err)
                        logger.warning(f'unsuccessful charge operation with ticket <<{ticket.id}>>!')
                    else:
                        user.balance = BankAccount.Withdrawal(user.bank_account, amount)
                        ticket.balance = metro.Credit_ticket.charge(ticket, amount)
                        um.User.update_pickle_charge(userID, user.balance)
                        metro.Ticket.update_pickle(ticket.id, ticket.balance)
                elif ticket.ticket_type == 'time/credit':
                    try:
                        if dt.date.fromisoformat(str(ticket.expire_date)) < dt.date.today():
                            raise ex.Metro_Exception('Time', 'Card is expired!')
                    except ex.Metro_Exception as err:
                        print(err)
                        logger.error(f'expired ticket <<{ticket.id}>> inserted!')
                    else:
                        print(f'Current Credit: {ticket.balance}')
                        try:
                            number = int(input(f'how many trips do you want to charge: {charge_menu2}'))
                            if number not in {5, 10, 15}:
                                raise ex.Metro_Exception('Input', 'wrong number entered!')
                        except ex.Metro_Exception as err:
                            print(err)
                            logger.warning(f'unsuccessful charge operation with ticket <<{ticket.id}>>!')
                        else:
                            amount = number * metro.Ticket.travel_cost
                            user.balance = BankAccount.Withdrawal(user.bank_account, amount)
                            ticket.balance = metro.Time_Credit_ticket.charge(ticket, amount)
                            um.User.update_pickle_charge(userID, user.balance)
                            metro.Ticket.update_pickle(ticket.id, ticket.balance)
        elif option == 4:
            userID = input('enter your ID: ')
            user = um.User.unpickle_instance(userID)
            try:
                if not isinstance(user, um.User):
                    raise ex.Metro_Exception('Id', 'ID not found!')
            except ex.Metro_Exception as err:
                print(err)
            else:
                ticket_id = um.User.select_ticket(user)
                ticket = metro.Ticket.unpickle_instance(ticket_id)
                try:
                    if ticket.balance < 2500:
                        raise ex.Metro_Exception('balance', 'insufficien balance!')
                except ex.Metro_Exception as err:
                    print(err)
                    logger.warning(f'ticket <<{ticket.id}>> with insufficient balance inserted.')
                else:
                    if ticket.ticket_type == 'time/credit':
                        try:
                            if dt.date.fromisoformat(str(ticket.expire_date)) < dt.date.today():
                                raise ex.Metro_Exception('Time', 'Card is expired!')
                        except ex.Metro_Exception as err:
                            print(err)
                            logger.error(f'expired ticket <<{ticket.id}>> inserted!')
                        else:
                            try:
                                if ticket.balance < metro.Ticket.travel_cost:
                                    raise ex.Metro_Exception('Balance', 'Credit is not sufficient!')
                            except ex.Metro_Exception as err:
                                print(err)
                                logger.error(f'ticket <<{ticket.id}>> credit is not sufficient!')
                            else:
                                origin = input('enter origin: ')
                                travel = um.Travel(origin)
                                print(um.Travel.travel_start(travel))
                                destination = input('enter destination: ')
                                try:
                                    if not destination:
                                        raise ex.Metro_Exception('Destination', 'unknown destination!')
                                except ex.Metro_Exception as err:
                                    print(err)
                                else:
                                    print(um.Travel.travel_end(travel, destination))
                                ticket.balance = um.Travel.payment(travel, ticket)
                    else:
                        try:
                            if ticket.balance < metro.Ticket.travel_cost:
                                raise ex.Metro_Exception('Balance', 'Credit is not sufficient!')
                        except ex.Metro_Exception as err:
                            print(err)
                            logger.error(f'ticket <<{ticket.id}>> credit is not sufficient!')
                        else:
                            origin = input('enter origin: ')
                            travel = um.Travel(origin)
                            print(um.Travel.travel_start(travel))
                            destination = input('enter destination: ')
                            try:
                                if not destination:
                                    raise ex.Metro_Exception('Destination', 'unknown destination!')
                            except ex.Metro_Exception as err:
                                print(err)
                            else:
                                print(um.Travel.travel_end(travel, destination))
                            ticket.balance = um.Travel.payment(travel, ticket)
                    metro.Ticket.update_pickle(ticket.id, ticket.balance)
        elif option == 5:
            userID = input('enter your ID: ')
            user = um.User.unpickle_instance(userID)
            try:
                if not isinstance(user, um.User):
                    raise ex.Metro_Exception('Id', 'ID not found!')
            except ex.Metro_Exception as err:
                print(err)
            else:
                amount = int(input('enter amount: '))
                user.balance = BankAccount.Deposit(user.bank_account, amount)
                um.User.update_pickle_charge(userID, user.balance)
        elif option == 6:
            break
