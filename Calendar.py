
#                                                       !!! CHANGE THE FILE PATH FOR NORMAL WORKING OF CODE !!!

file_path = "C:\\Users\\User\\OneDrive - American University of Armenia\\Desktop\\Project\\"

months = [ "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

# Created default variables for further while loops

state_export = False
state_load = False
bye = False

# The start of Calendar object, also checking whether the year is leap or not.

class Calendar:

    def __init__(self, year):
        self.year = year
        self.tasks = {}
        self.selected_month = None
        self.is_leap_year = self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0)

    # The function for , checking whether the particular months are in their capacities or not.

    def is_valid_day(self, month, day):
        month = month.strip().lower()
        if not (1 <= day <= 31):
            return False
        elif month in ["april", "june", "september", "november"] and day > 30:
            return False    
        elif month == "february" and day > (28 + self.is_leap_year):
            return False
        return True
      
    # The function of adding tasks by using day validation function for checking compatibility of days with months and leap years, 
    # handling all error cases and all invalid input cases. And if the user will not add anyhting the default variables will change and the further loops will not work.
        
    def add_task(self):
        while True:
            try:
                month = input("Enter the month (January-December, Exit to stop): ").capitalize().strip()
                if month == "Exit":
                    break  
                if month not in months:
                    print("Invalid month, try again!")
                    continue
                while True:
                    try:
                        day = int(input("Enter the day: "))
                        if self.is_valid_day(month, day):
                            description = input("Enter task description: ")
                            date_key = f"{month}-{day}"
                            if date_key not in self.tasks:
                                self.tasks[date_key] = []
                            self.tasks[date_key].append(description)
                            print("Task added successfully!")
                            break
                        else:
                            print("Invalid day, try again!")
                    except Exception as e:
                        print(f"You have faced this error: {e}, try again!")
            except Exception as e:
                print(f"You have faced this error: {e}, try again!")
        global state_export, state_load, bye
        if self.tasks == {}:
            state_export = True
            state_load = True
            bye = True
        else:
            pass
    
    # The function is responsible for displaying the period(Month or Year) the user wanted, comparing with ones the user enters or not in the previous step

    def display_period(self, period):
        if period == 'month':
            while True:
                self.selected_month = input("Enter the month (January-December): ").capitalize().strip()
                if self.selected_month in [i.split('-')[0] for i in self.tasks.keys()]:
                    self.print_month(self.selected_month)
                    break
                else:
                    print("You have no plans that month. Try again!")
                    continue
        elif period == 'year':
            self.print_year()

    # The following 3 functions are resposnible for giving the dates and tasks corresponding to each other when the user planned tasks

    def print_month(self, month):
        date_keys = [f"{month}-{day}" for day in range(1, 32)]
        self.print_tasks(date_keys)

    def print_year(self):
        date_keys = [f"{month}-{day}" for month in months for day in range(1, 32)]
        self.print_tasks(date_keys)

    def print_tasks(self, date_keys):
        for date_key in date_keys:
            if date_key in self.tasks:
                tasks_for_day = ', '.join(self.tasks[date_key])
                print(f"{date_key}: {tasks_for_day}")

    # The function is responsible for exporting data to text editor

    def export_data(self, filename):
        with open(file_path + filename, 'w') as file:
            for date_key, tasks in self.tasks.items():
                if self.selected_month is None or date_key.startswith(self.selected_month):
                    file.write(f"{date_key} : {','.join(tasks)}\n")

    # The function is responsible for loading data from text editor which we created in the previous step

    def load_data(self, filename):
        try:
            print("Here is(are) your scheduled task(s):")
            with open(file_path+filename, 'r') as file:
                for line in file:
                    date_str, tasks_str = line.strip().split(':')
                    self.tasks[date_str] = tasks_str.split(',')
                    print(f'{date_str}:{tasks_str}')
        except Exception as e:
            print(f"You have faced this error: {e}, try again!")

# The loop is responsible for taking from user correct type of year
 
while True:
    try:
        year = int(input("Enter the year: "))
        if year>0:
            break
        else:
            print("You printed invalid year, try again!")
            continue
    except Exception as e:
        print(f"You have faced this error: {e}, try again!")

# Calling the Calendar class and naming it my_calendar, also calling the add_task() method to start the whole process

my_calendar = Calendar(year)
my_calendar.add_task()

# Creating loop using default variables for displaying and exporting the data if the user wants, handling all errors and invalid inputs

while not state_export:
    try:
        period = input("Enter the period (Month/Year): ").lower().strip()
        if period not in ["month","year"]:
            print("Invalid input, try again!")
            continue
        my_calendar.display_period(period)        
        while True:
            export = input("Do you want to export your data into txt file (Y/N) ? ").lower().strip()
            if export == "y":
                state_load = False
                name = input("Please enter name for your calendar file: ")
                if not name:
                    print("File name cannot be empty, try again!")
                    continue
                else:
                    my_calendar.export_data(name + ".txt")
                    print(f'Your file was saved here {file_path}.')
                    state_export = True
                    break
            elif export == "n":
                state_export = True
                state_load = True
                bye = True
                break
            else:
                print("Invalid input, please enter Y or N!")
                continue
    except Exception as e:
        print(f"You have faced this error: {e}, try again!")
        continue

# Creating loop for loading the file from the folder if the user wants, again handling all error cases and invalit iput cases

while not state_load:
    try:
        load = input("Do you want to load your file (Y/N) ? ").lower().strip()
        if load == "y":
            my_calendar.load_data(name+".txt")
            bye = True
            break
        elif load == "n":
            bye = True
            break
        else:
            print("Invalid input, please enter Y or N!")
            continue
    except Exception as e:
        print(f"You have faced this error: {e}, try again!")

if bye:
    print("Have a nice day!")

