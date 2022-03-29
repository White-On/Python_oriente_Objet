from abc import ABC, abstractmethod
import ContextX

class AbstactState(ABC):
    def __init__(self,context:ContextX) -> None:
        self.context = context
    @abstractmethod
    def doThis(self):
        pass
    @abstractmethod
    def doThat(self):
        pass
    def __repr__(self) -> str:
        return self.__class__.__name__

class State1(AbstactState):
    def __init__(self, context:ContextX) -> None:
        super().__init__(context)
    def __repr__(self) -> str:
        return super().__repr__()
    def doThis(self):
        newState = State2(self.context)
        self.context.changeState(newState)
    
class State2(AbstactState):
    def __init__(self, context:ContextX) -> None:
        super().__init__(context)
    def __repr__(self) -> str:
        return super().__repr__()
    def doThis(self):
        newState = State1(self.context)
        self.context.changeState(newState)