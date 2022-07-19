# customer.py

class Customer:
    def __init__(self, cur_floor, dst_floor, name):
        self.cur_floor = cur_floor
        self.dst_floor = dst_floor
        self.name = name
        self.in_elevator = False
        self.delivered = False

    def __str__(self):
        return f'{self.name}({self.dst_floor})'

    def get_cur_floor(self):
        'Returns current floor of the customer'
        return self.cur_floor

    def get_dst_floor(self):
        'Returns destination floor of the customer'
        return self.dst_floor

    def get_name(self):
        'Returns the name of the customer'
        return self.name

    def move_in(self):
        'Pick up: Customer enters the elevator'
        self.in_elevator = True

    def move_out(self):
        'Drop off: Customer gets out the elevator'
        self.in_elevator = False
        self.delivered = True
        self.cur_floor = self.dst_floor

    def has_been_delivered(self):
        'Check if the customer was delivered to his/her destination floor'
        return self.delivered

    def is_in_elevator(self):
        'Check if the customer is still in the elevator'
        return self.in_elevator
