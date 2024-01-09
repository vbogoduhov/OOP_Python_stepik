import time 

class GeyserClassic:
    # Максимальное время работы фильтра
    MAX_DATE_FILTER = 100     

    def __init__(self):
        self.slot1 = None
        self.slot2 = None
        self.slot3 = None


    def add_filter(self, slot_number, filter):
        if (slot_number == 1) and (isinstance(filter, Mechanical)):
            self.slot1 = filter
        if (slot_number == 2) and (isinstance(filter, Aragon)):
            self.slot2 = filter
        if (slot_number == 3) and (isinstance(filter, Calcium)):
            self.slot3 = filter

    def remove_filter(self, slot_number): 
        if slot_number == 1:
            self.slot1 = None
        elif slot_number == 2:
            self.slot2 = None
        else:
            self.slot3 = None


    def get_filters(self):
        return (self.slot1, self.slot2, self.slot3)

    def water_on(self):
        if (self.slot1 is not None) and (self.slot2 is not None) and (self.slot3 is not None) and \
                (0 <= time.time() - self.slot1.date <= self.MAX_DATE_FILTER) and \
                (0 <= time.time() - self.slot2.date <= self.MAX_DATE_FILTER) and \
                (0 <= time.time() - self.slot3.date <= self.MAX_DATE_FILTER):
            return True
        else:
            return False


class Mechanical:
    def __init__(self, date):
        self.date = date 

    def __setattr__(self, key, value):
        # if isinstance(self.date, float):
        #     pass
        if (type(value) is float) and (value > 0) and (not hasattr(self, "date")):
            object.__setattr__(self, key, value)
        # if hasattr(self, "date"):
        #     pass

class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        # if isinstance(self.date, float):
        #     pass
        if (type(value) is float) and (value > 0) and (not hasattr(self, "date")):
            object.__setattr__(self, key, value)
        # if hasattr(self, "date"):
        #     pass


class Calcium:
    def __init__(self, date):
        self.date = date 


    def __setattr__(self, key, value):
        # if isinstance(self.date, float):
        #     pass
        if (type(value) is float) and (value > 0) and (not hasattr(self, "date")):
            object.__setattr__(self, key, value)
        # if hasattr(self, "date"):
        #     pass

