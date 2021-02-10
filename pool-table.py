# Going to need classes. (pool Table)
# Import date/times
# User needs to be able to:
    # -check out table
    # -check in table
    # -total time
# Pool Table: - need empty dictionary of pool tables
    # Pool table number
    # Start Date time
    # End Date time
    # Total time played
    # cost - if hard mode

# Table class
class PoolTable:
        def __init__(self, table_number):
            self.table_number = table_number
            self.occupied = False
            self.start_time = None
            self.end_time = None
            self.time_played = None
            self.current_time = None
        
        def checkout(self):
            if self.occupied == False:
                print("")
                input("This Table is availble.")
                return False
            else: 
                self.occupied = False
                self.end_time = 
                self.time_played = self.end_time - self.start_time
                return True
        
        def checkin(self):
            if self.occupied = False:



