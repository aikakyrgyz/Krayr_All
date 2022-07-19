from building import Building

import time
# main.py


def run_program():
    # show up for the user
    # ask the user for the num_floors
    num_floors = input('Input how many floors are in the building? ')
    while not num_floors.strip().isdigit():
        num_floors = input('Input how many floors are in the building? ')
    num_customers = input('How many customers are in the building? ')
    while not num_customers.strip().isdigit():
        num_customers = input('How many customers are in the building? ')
    building = Building(int(num_floors.strip()), int(num_customers.strip()))
    building.draw()

    # when is the program going to end? When all customers are delivered to their destination floors

    while not building.all_delivered():
        time.sleep(1)
        building.run() # take care of picking up and dropping the customer
        building.draw() # draws the updated building

    print('\U0001F44D'.center(60))
    print('ALL customers have been delivered!')
run_program()

