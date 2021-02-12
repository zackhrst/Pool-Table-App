
import json
tables = []

from datetime import datetime
from pool_table import PoolTable

date_now = datetime.now()
current_date = date_now.date()
formatted_date = current_date.strftime("%m-%d-%Y")


pool_tables = []


for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

def display_tables():
    for table in range(0, len(pool_tables)):
        table = pool_tables[table]
        if table.available == True:
            is_available = "is available"
            print(f"\nTable {table.table_name} {is_available}")
        elif table.available == False:
            is_not_available = "is NOT available"
            formatted_start_time = table.start_time.strftime("%I:%M%p on %m-%d-%Y")
            print(f"\nTable {table.table_name} {is_not_available} - Checkout Time: {formatted_start_time} - Play Time: {table.time_played()}")

while True: 
  
    print(f"\n  Salty Spatoon Pool Hall Manager")
    menu = input("""
    1. Display all tables
    2. Check-out a table 
    3. Check-in a table 
    q. Enter q to quit
    Enter your choice: """)
    
    if menu == "1":
        display_tables()
    
    elif menu == "2":
        display_tables()
        which_table = int(input(f"\nCheckout table number 1-12: "))
        table = pool_tables[which_table-1]

        if table.available == False:
            print(f"\n ****** WARNING ******")
            print(f"/// Pool Table {table.table_name} is currently occupied ///")

        else:
            table.check_out_table()
            display_tables()
    
    elif menu == "3":
        for table in range(0, len(pool_tables)):
            table = pool_tables[table]
            if table.available == False:
                is_not_available = "is NOT available"
                formatted_start_time = table.start_time.strftime("%I:%M%p on %m-%d-%Y")
                print(f"\nTable {table.table_name} {is_not_available} - Checkout Time: {formatted_start_time} - Play Time: {table.time_played()}")

        which_table = int(input(f"\nCheck-in table number: "))
        table = pool_tables[which_table-1]

        if table.available == True:
            print(f"\n ******** PLEASE BE ADVISED ********")

        else:
            table.check_in_table()

        try:
            formatted_start_time = table.start_time.strftime("%I:%M%p on %m-%d-%Y")
            formatted_end_time = table.end_time.strftime("%I:%M%p on %m-%d-%Y")
            play_time = table.time_played()
            formatted_play_time = str(play_time)

            with open(f"{formatted_date}.json", "w") as file_object:
                table = {"table": table.table_name, "started": formatted_start_time, "ended": formatted_end_time, "playtime": formatted_play_time}
                tables.append(table)
                json.dump(tables, file_object)

        except AttributeError:
            print(f"/// Pool Table {table.table_name} is already checked in ///")
   
        display_tables()

    elif menu == "q" or menu == "Q":
        break

    else:
        print(f"{menu} is not a valid choice. Please try again")