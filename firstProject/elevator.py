import random
import time
import names

UP = 1
DOWN = -1
# link if you are having problems with pip:
# https://packaging.python.org/en/latest/tutorials/installing-packages/


class Building:
    def __init__(self, num_floors, num_customers):
        'Initialize all necessary values for the Building class'
        self.num_floors = num_floors  # The number of floors
        # Create a list of customers
        self.customer_list = []
        for i in range(num_customers):
            cur_floor = random.randint(1, num_floors) # floors is inclusive here, opposite to range, where the stop is not inclusive
            choice_dst_list = list(range(1, num_floors + 1))
            choice_dst_list.remove(cur_floor) # the current floor of the customer cannot be the destination floor of that customer
            dst_floor = random.choice(choice_dst_list)
            self.customer_list.append(Customer(cur_floor, dst_floor, names.get_first_name()))
        self.elevator = Elevator(num_floors)  # Create an elevator in that building


    def run(self):
        'Operate the elevator'
        # check each customer
        for customer in self.customer_list:
            # if the customer is in the elevator
            if customer.get_name() in self.elevator.get_in_elevator_list():
                # if the customer has reached the dst_floor
                if customer.get_dst_floor() == self.elevator.get_cur_floor():
                    customer.move_out()
                    self.elevator.cancel_customer(customer.get_name())
            else:
                # if the elevator has reached one customer's floor
                if (not customer.has_finished()) and \
                        customer.get_cur_floor() == self.elevator.get_cur_floor():
                    customer.move_in()
                    self.elevator.register_customer(customer.get_name())

        # move the elevator
        if not self.has_finished():
            self.elevator.move()

    def output(self):
        """output the building"""
        LEFT = 10
        CENTER = 40
        RIGHT = 10
        print('-' * (LEFT + CENTER + RIGHT))
        print("Floor".center(LEFT) + "Customer".center(CENTER) + "Elevator".center(RIGHT))
        print('-' * (LEFT + CENTER + RIGHT))

        for i in range(self.num_floors, 0, -1):
            line = str(i).center(LEFT) + \
                   ' '.join([str(customer.get_name()) + f'({customer.get_dst_floor()})'
                             for customer in self.customer_list
                             if (not customer.is_in_elevator()) and \
                             customer.get_cur_floor() == i]).center(CENTER)
            if i == self.elevator.get_cur_floor():
                line += '\U0001F7E8'.center(RIGHT)
            print(line)
            print('-' * (LEFT + CENTER + RIGHT))

    def get_customer_list(self):
        """return the customer_list"""
        return self.customer_list

    def has_finished(self):
        """check whether all customers have reached dst_floors"""
        for customer in self.get_customer_list():
            if not customer.has_finished():
                return False
        return True


class Elevator():
    def __init__(self, floors):
        self.floors = floors  # The number of floors
        self.in_elevator_list = []  # The list of customer's names in the elevator
        self.cur_floor = 1  # The default floor is 1
        self.direction = UP # elevator starts from moving upward

    def move(self):
        """move the elevator by 1 floor"""
        # move to next floor
        self.cur_floor += self.direction
        # if next floor is outside the range, change the direction
        if self.cur_floor + self.direction < 1 or \
                self.cur_floor + self.direction > self.floors:
            self.direction *= -1

    def register_customer(self, customer):
        """put the customer into register_list"""
        self.in_elevator_list.append(customer)

    def cancel_customer(self, customer):
        """remove the customer from register_list"""
        self.in_elevator_list.remove(customer)

    def is_in_elevator_list(self, customer):
        """check whether the customer is in register_list"""
        return customer in self.in_elevator_list

    def get_in_elevator_list(self):
        """return register_list"""
        return self.in_elevator_list

    def get_cur_floor(self):
        """return current floor"""
        return self.cur_floor


class Customer:
    def __init__(self, cur_floor, dst_floor, name):
        self.cur_floor = cur_floor
        self.dst_floor = dst_floor
        self.name = name
        self.in_elevator = False  # whether the customer is in the elevator
        self.finished = False  # whether the customer has reached the dst_floor

    def __repr__(self):
        return self.name + f'({self.dst_floor})'

    def get_cur_floor(self):
        """return current floor"""
        return self.cur_floor

    def get_dst_floor(self):
        """return destination floor"""
        return self.dst_floor

    def get_name(self):
        """return customer's ID"""
        return self.name

    def move_in(self):
        """move the customer into the elevator"""
        self.in_elevator = True

    def move_out(self):
        """move the customer out of the elevator"""
        self.in_elevator = False
        self.finished = True
        self.cur_floor = self.dst_floor

    def has_finished(self):
        """check whether the customer has reached the dst_floor"""
        return self.finished

    def is_in_elevator(self):
        """check whether the customer is in the elevator"""
        return self.in_elevator


def main():
    # get user inputs to customize a building
    num_floors = input("Please input how many floors in this building: ")
    while not num_floors.isdigit():
        num_floors = input("Please input how many floors in this building: ")
    num_customers = input("Please input how many customers in this building: ")
    while not num_customers.isdigit():
        customers = input("Please input how many customers in this building: ")
    building = Building(int(num_floors), int(num_customers))
    building.output()

    # operate the elevator until all customers have reached dst_floors
    while not building.has_finished():
        time.sleep(2)
        building.run()
        building.output()
    print('\U0001F44D'.center(60))
    print('ALL CUSTOMERS HAVE BEEN DELIVERED!'.center(60))

main()
