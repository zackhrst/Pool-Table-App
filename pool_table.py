from datetime import datetime

class PoolTable:
    def __init__(self, name):
        self.table_name = name 
        self.available = True
        self.start_time = None
        self.end_time = None

    def check_out_table(self):
        self.available = False
        self.start_time = datetime.now()
   
    def check_in_table(self):
        self.available = True 
        self.end_time = datetime.now()

    def time_played(self):
        if self.start_time == None:
            return datetime.now() - datetime.now()
        elif self.end_time == None:
            return datetime.now() - self.start_time
        else:
            return self.end_time - self.start_time