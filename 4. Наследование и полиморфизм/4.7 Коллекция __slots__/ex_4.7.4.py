class Person(object):
    """docstring for Person."""
    __slots__ = ('_fio', '_old','_job')

    def __init__(self, fio, old, job):
        super(Person, self).__init__()
        self._fio = fio
        self._old = old
        self._job = job

persons = [
    Person('Суворов', 52, 'полководец'),
    Person('Рахманинов', 50, 'пианист, композитор'),
    Person('Балакирев', 34, 'программист и преподаватель'),
    Person('Пушкин', 32, 'поэт и писатель')
]
