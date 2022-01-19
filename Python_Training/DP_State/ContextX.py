import State

class ContextX:
    def __init__(self) -> None:
        self.state =  State.State1(self)
    
    
    def changeState(self,state):
        self.state = state
        print(f"Changement d'état, On passe à {self.state}")
    
    def doThis(self):
        self.state.doThis()