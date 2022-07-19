# elevator.py

UP = 1
DOWN = -1


class Elevator:

    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.cur_floor = 1 # shows the current floor of the elevator
        self.direction = UP
        self.in_elevator_list = [] # the list of customers that are in the elevator

    def get_current_floor(self):
        'Returns the current floor of the elevator'
        return self.cur_floor

    def move(self):
        'Moves the elevator by one floor, depending on the direction'
        # 8 -> 9 UP
        # 8 -> 7 DOWN
        self.cur_floor += self.direction
        # Change the direction if the last floor or the first floor is reached
        next_floor = self.cur_floor + self.direction
        if next_floor < 1 or next_floor > self.num_floors:
            self.direction = UP if self.direction == DOWN else DOWN

    def get_list_of_customer(self):
        'Returns the list of the customers that are inside the elevator'
        return self.in_elevator_list

    def register_customer(self, customer):
        'Add the customer to the in_elevator_list: if the cusomter just entered the elevator'
        self.in_elevator_list.append(customer)

    def remove_customer(self, customer):
        'Remove the customer from the in_elevator_list: if the customer just exited the elevator'
        self.in_elevator_list.remove(customer)

    def is_in_elevator(self, customer):
        'Check is the customer is inside the elevator'
        return customer in self.in_elevator_list







