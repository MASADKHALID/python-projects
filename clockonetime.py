class Clock:
    def __init__(self): 
        print("HOURS:MINUTES:SECOND")
        self.display_time()

    def display_time(self):
        for self.hours in range(24):  # Hours should be from 0 to 23
            for self.minutes in range(60):
                for self.seconds in range(60):
                    print(f"\r{self.hours:02}:{self.minutes:02}:{self.seconds:02}", end='')
                    # Above line prints hours, minutes, and seconds in HH:MM:SS format
                    # :02 ensures that there are at least 2 digits, padding with 0 if necessary

test1 = Clock()
    
