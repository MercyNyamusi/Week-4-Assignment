def repeat(function, list1):
    """
   function to ask the user whether they would like to repeat the operation or not
   :param function: the operation being carried out
   :param list1: list of cars

   """
    response = input("Do you wish to try again?(Y/N)").lower()
    if response == 'y' or response == 'yes' or response == 'yeah':
        x = function(list1)
    elif response == 'n' or response == 'no':
        x = list1
    else:
        print("Invalid Input. Please try again")
        repeat(function, list1)
    return x


def add_new_entry(existing_list):
    """
        function to add new car entries to records
        :param existing_list: list of cars already in inventory

    """
    car_plate = input("Please input the car's number plate:")
    for i in range(len(existing_list)):
        # checks whether record already exists
        if existing_list[i]["Car_plate"] == car_plate:
            print(f"Car with {car_plate} already exists")
            x = repeat(add_new_entry, existing_list)
            return x
    # takes details of the new entry as input
    car_model = input("Please input the model of the car:")
    year_of_release = input("Please input the year the car is released:")
    year_of_acquisition = input("Please input the year the car was acquired:")
    car_revenue = input("Please input the money made from the car:")
    number_of_rents = input("Please input the number of times the car has been rented since acquisition:")
    existing_list.append(
        {"Car_plate": car_plate, "Model": car_model, "Year_of_release": year_of_release,
         "Year_of_acquisition": year_of_acquisition,
         "revenue_generated": car_revenue, "number_of_times_rented": number_of_rents})

    x = existing_list
    return x


def remove_entry(existing_list):
    """
        function to remove entry from list
        :param existing_list: list of cars already in inventory

    """
    count = 0
    index = 0
    car_remove = input("Please enter the number plate of the car you wish to remove:")
    for i in range(len(existing_list)):
        # checks whether entry exists
        if existing_list[i]["Car_plate"] == car_remove:
            index = i
            count += 1
            break
    if count == 0:
        print("Sorry, our records do not have a car matching that plate.")
        x = repeat(remove_entry, existing_list)
        return x
    else:
        existing_list.pop(index)
        return existing_list


def count_car_rented(existing_list):
    """
        function to count the number of times a car has been rented
        :param existing_list: list of cars already in inventory

    """
    elem_count = 0
    x = 0
    car_rents = input("Please enter the number plate of the car you wish to inquire:")
    for i in range(len(existing_list)):
        # checks whether entry exists
        if existing_list[i]["Car_plate"] == car_rents:
            x = existing_list[i]["number_of_times_rented"]
            elem_count += 1
    if elem_count == 0:
        print("Sorry, our records do not have a car matching that plate.")
        x = repeat(count_car_rented, existing_list)
    return x


def revenue_generated(existing_list):
    """
        function to calculate amount of revenue generated from renting a car
        :param existing_list: list of cars already in inventory

    """
    elem_count = 0
    x = 0
    car_revenue = input("Please enter the number plate of the car you wish to inquire:")
    for i in range(len(existing_list)):
        # checks whether entry exists
        if existing_list[i]["Car_plate"] == car_revenue:
            x = existing_list[i]["revenue_generated"]
            elem_count += 1
    if elem_count == 0:
        print("Sorry, our records do not have a car matching that plate.")
        x = repeat(revenue_generated, existing_list)

    return x


def rent_car(existing_list):
    """
        function to allow user to rent a car
        updates the revenue amount and the number of times a car has been rented
        :param existing_list: list of already existing cars

    """
    elem_count = 0
    car_rents = input("Please enter the number plate of the car you wish to rent:")
    car_revenue = int(input("Please enter the revenue to be generated from the renting:"))
    for i in range(len(existing_list)):
        # checks whether entry exists
        if existing_list[i]["Car_plate"] == car_rents:
            existing_list[i]["number_of_times_rented"] += 1
            existing_list[i]["revenue_generated"] += car_revenue
            elem_count += 1
    if elem_count == 0:
        print("Sorry, our records do not have a car matching that plate.")
        x = repeat(rent_car, existing_list)
        return x
    else:
        print(f"You have successfully rented car with the number plate: {car_rents}")
        return existing_list


def display(existing_list):
    return existing_list


# list of dictionaries where each dictionary contains info about the first 5 cars
existing_cars = [{"Car_plate": "KBC 456T", "Model": "Benz", "Year_of_release": 2008, "Year_of_acquisition": 2011,
                  "revenue_generated": 45000, "number_of_times_rented": 20},
                 {"Car_plate": "KAZ 135M", "Model": "Audi", "Year_of_release": 2019, "Year_of_acquisition": 2019,
                  "revenue_generated": 3000, "number_of_times_rented": 6},
                 {"Car_plate": "KEB 897Y", "Model": "Wish", "Year_of_release": 2016, "Year_of_acquisition": 2017,
                  "revenue_generated": 30000, "number_of_times_rented": 16},
                 {"Car_plate": "KCA 223K", "Model": "Land Cruiser", "Year_of_release": 2016,
                  "Year_of_acquisition": 2020,
                  "revenue_generated": 8000, "number_of_times_rented": 10},
                 {"Car_plate": "KPM 478P", "Model": "BMW", "Year_of_release": 2019, "Year_of_acquisition": 2021,
                  "revenue_generated": 500, "number_of_times_rented": 4}]


# allows users to choose the operation they wish to perform
def task_choice():
    user_input = int(
        input("Welcome to Omondi Car Shop Record System\nPlease select the operation you wish to perform.\n"
              "1.Add a new car to the collection\n"
              "2.Rent a car\n"
              "3.Remove a car from the collection\n"
              "4.Count the number of times a car has been rented out\n"
              "5.Count the amount of revenue generated from a car\n"
              "6.Display existing list of cars\n"))

    if user_input == 1:
        print("New list:", add_new_entry(existing_cars))
    elif user_input == 2:
        print("New list:", rent_car(existing_cars))
    elif user_input == 3:
        print("New list:", remove_entry(existing_cars))
    elif user_input == 4:
        print("Number of times rented:", count_car_rented(existing_cars))
    elif user_input == 5:
        print("revenue generated", revenue_generated(existing_cars))
    elif user_input == 6:
        print("Existing cars:", display(existing_cars))
    else:
        print("Please enter a valid option")
    response = input("Do you wish to perform another operation?(Y/N)").lower()
    if response == 'y':
        task_choice()
    elif response == 'n':
        return


task_choice()
