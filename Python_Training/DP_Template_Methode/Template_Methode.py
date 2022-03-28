from abc import ABC, abstractmethod

from matplotlib.pyplot import step

class AbstactClass(ABC):
    @abstractmethod
    def step1(self):
        pass
    @abstractmethod
    def step2(self):
        pass
    @abstractmethod
    def step3(self):
        pass
    @abstractmethod
    def step4(self):
        pass

class ConcreteClass1(AbstactClass):

    def step1(self,x):
        return x + 5
    def step2(self,x):
        return x * 10
    def step3(self,x):
        return int(x / 2)
    def step4(self,x):
        return x-7

    def __init__(self,x) -> None:
        super().__init__()
        self.x = self.step1(x)
        if(self.x > 0):
            self.x = self.step2(self.x)
        for _ in range(5):
            self.x = self.step3(self.x)
            self.x = self.step4(self.x)
        
    def getX(self):
        print(self.x)
        return self.x
        
class ConcreteClass2(AbstactClass):

    def step1(self,x):
        return x + 2
    def step2(self,x):
        return x * 4
    def step3(self,x):
        return int(x / 3)
    def step4(self,x):
        return x + 8

    def __init__(self,x) -> None:
        super().__init__()
        self.x = self.step1(x)
        if(self.x > 0):
            self.x = self.step2(self.x)
        for _ in range(4):
            self.x = self.step3(self.x)
            self.x = self.step4(self.x)
        
    def getX(self):
        print(self.x)
        return self.x


A = ConcreteClass1(5).getX()
B = ConcreteClass2(5).getX()        
        
