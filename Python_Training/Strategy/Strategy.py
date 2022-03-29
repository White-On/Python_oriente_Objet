class ParserMeta(type):
    def __instancecheck__(cls, __instance) -> bool:
        return cls.__subclasscheck__(type(__instance))
    
    def __subclasscheck__(cls, __subclass) -> bool:
        return (hasattr(__subclass,'execute') and callable(__subclass.execute))


class InterfaceStrategy(metaclass=ParserMeta):
    pass

class Strategy1(InterfaceStrategy):
    def __init__(self):
        pass

    def execute(self)->str:
        return "Strategy1"
    
class Strategy2(InterfaceStrategy):
    def __init__(self):
        pass

    def execute(self)->str:
        """Execute strategy 2"""
        return "Strategy2"

class Strategy3(InterfaceStrategy):
    def __init__(self):
        pass
    
    def execute(self)->str:
        return "Strategy3"

class ContextX:
    def __init__(self, strategy:InterfaceStrategy):
        self.strategy = strategy

    def setStrategy(self, strategy:InterfaceStrategy):
        self.strategy = strategy

    def execute(self)->str:
        return self.strategy.execute()


print(ContextX(Strategy1()).execute())
c = ContextX(Strategy2())
print(c.execute())
c.setStrategy(Strategy3())
print(c.execute())