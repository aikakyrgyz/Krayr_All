import names
import random
from customer import Customer
from elevator import Elevator

L = 10
C = 40
R = 10
TOTAL = 60

# building.py


class Building:
    def __init__(self, num_floors, num_customers):
        self.num_floors = num_floors
        self.num_customer = num_customers
        self.customer_list = [] # list of customers / objects
        # create an elevator in the building
        self.elevator = Elevator(self.num_floors)
        # generate the random customers, with corresponding names, cur_floors, and dst_floors
        for i in range(num_customers):
            name = names.get_first_name()
            cur_floor = random.randint(1, self.num_floors) # generate a random number 1<= N <= num_floors
            # the destination floor cannot be the same as the current floor
            dst_floor_possib = list(range(1, self.num_floors+1))
            dst_floor_possib.remove(cur_floor)
            dst_floor = random.choice(dst_floor_possib)
            customer = Customer(cur_floor, dst_floor, name)
            self.customer_list.append(customer)

    def draw(self):
        'Draws the updated version of the building'
        print('-' * TOTAL)
        print('FLOOR'.center(L) + 'CUSTOMER'.center(C) + 'ELEVATOR'.center(R))
        print('-' * TOTAL)

        for i in range(self.num_floors, 0, -1): # start = num_floors, end = 1 (since 0 is non-inclusive), step = -1 (since the loop is in decreasing order)
            floor = str(i).center(L)
            customer_and_dst = ' '.join([customer.get_name() + '(' + str(customer.get_dst_floor()) + ')' for customer in self.customer_list if not customer.is_in_elevator() and customer.get_cur_floor() == i]).center(C)
            line = floor + customer_and_dst
            line += '\U0001F7E8' if self.elevator.get_current_floor() == i else ''
            print(line)
            print('-' * TOTAL)

    def run(self):
        'Runs the elevator'
        for customer in self.customer_list:
            if customer.get_name() in self.elevator.get_list_of_customer():
                if customer.get_dst_floor() == self.elevator.get_current_floor():
                    customer.move_out()
                    self.elevator.remove_customer(customer.get_name())
            else:
                if not customer.has_been_delivered() and customer.get_cur_floor() == self.elevator.get_current_floor():
                    customer.move_in()
                    self.elevator.register_customer(customer.get_name())

        if not self.all_delivered():
            self.elevator.move()

    def get_customer_list(self):
        'Returns the list of all customers in that building'
        return self.customer_list

    def all_delivered(self):
        'Check if all the customers were delivered to their destination floors'
        for customer in self.customer_list:
            if not customer.has_been_delivered():
                return False
        return True


