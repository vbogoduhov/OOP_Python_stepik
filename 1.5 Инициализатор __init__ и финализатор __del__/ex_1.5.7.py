class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        lst_config = [f"Материнская плата: {self.name}",
                      f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                      f"Слотов памяти: {self.total_mem_slots}",
                      f"Память: {';'.join([f'{mem.name} - {mem.volume}' for mem in self.mem_slots])}"]

        return lst_config

mb = MotherBoard('Asus', CPU('ryzen 5', 3400), [Memory('Kingston', 4000), Memory('Patriot', 4048)])
# print(mb.get_config())



