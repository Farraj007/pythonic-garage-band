from abc import  abstractmethod

class Band :
    instances = [] 

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        
    def __str__(self):
        return f'The band {self.name}'

    def __repr__(self):
        return  f"Band instance. name={self.name}, members={self.members}"

    @classmethod
    def to_list(cls):
        return cls.instances

    
    def play_solos(cls):
        return [member.play_solo() for member in cls.members]

class Musician: 

    def __init__(self):
        self.name = ''
        self.instrument = ''


    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):

    def __init__(self, name):
        self.name = name
        self.instrument ="guitar"

    def __repr__(self):
        return (f"Guitarist instance. Name = {self.name}")

    
    def __str__(self):
        return (f"My name is {self.name} and I play {self.instrument}")

    
    def get_instrument(self):
        return self.instrument

    
    def play_solo(self):
        return f'face melting {self.instrument} solo'


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"
    
    def __repr__(self):
       return f"Bassist instance. Name = {self.name}"


    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    
    def get_instrument(self):
        return self.instrument

    
    def play_solo(self):
        return "bom bom buh bom"

    

class Drummer(Musician):

    def __init__(self, name):
        self.name = name
        self.instrument = "drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    
    def get_instrument(self):
        return self.instrument

    
    def play_solo(self):
        return 'rattle boom crash'
#    [print(i) for i in .play_solos()]
