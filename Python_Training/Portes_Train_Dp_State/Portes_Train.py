from abc import abstractmethod

class Context_Door:
    def __init__(self) -> None:
        #Etat initial -> Fermée
        self.state =  Closed(self)
    
    def changeState(self,state,comment = ""):
        self.state = state
        print(f"Changement d'état, On passe à {self.state}. {comment}")
    
    def lock(self):
        self.state.lock()

    def close(self):
        self.state.close()
    
    def pushButton(self):
        self.state.pushButton()
    
    def unlock(self):
        self.state.unlock()

class AbstactState:
    def __init__(self,context:Context_Door) -> None:
        self.context = context

    @abstractmethod
    def lock(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def pushButton(self):
        pass

    @abstractmethod
    def unlock(self):
        pass

    def __repr__(self, state:str) -> str:
        return f"{state} ({self.__class__.__name__})"

class Opened(AbstactState):
    def __init__(self, context:Context_Door) -> None:
        super().__init__(context)

    def __repr__(self) -> str:
        return super().__repr__("Ouverte")

    def lock(self):
        print("Verouillage impossible ! Les portes ne sont pas fermées.")
    
    def close(self):
        newState = Closed(self.context)
        self.context.changeState(newState,"Fermeture des portes.")

    def pushButton(self):
        newState = Opened(self.context)
        self.context.changeState(newState,"Les portes s'ouvrent ou sont déja ouvertes.")

    def unlock(self):
        print("Les portes sont déja déverouillées.")
    
class Closed(AbstactState):
    def __init__(self, context:Context_Door) -> None:
        super().__init__(context)
    def __repr__(self) -> str:
        return super().__repr__("Fermée")

    def lock(self):
        newState = Locked(self.context)
        self.context.changeState(newState,"Verouillage des Portes.")

    def close(self):
        newState = Closed(self.context)
        self.context.changeState(newState,"Les portes ce ferment ou sont déja fermées.")
        
    def pushButton(self):
        newState = Opened(self.context)
        self.context.changeState(newState,"Ouverture des portes.")
    
    def unlock(self):
        print("Les portes sont déja déverouillées.")

class Locked(AbstactState):
    def __init__(self, context:Context_Door) -> None:
        super().__init__(context)
    def __repr__(self) -> str:
        return super().__repr__("Verouillée")
    
    def lock(self):
        newState = Locked(self.context)
        self.context.changeState(newState,"Les portes sont en cours de verouillage ou déja verouillées")

    def close(self):
        print("Les Portes sont déja fermées !")
        
    def pushButton(self):
        print("Ouverture impossible ! Les Portes sont verouillées")

    def unlock(self):
        newState = Closed(self.context)
        self.context.changeState(newState,"Déverouillage des portes.")

door = Context_Door()

door.close()
door.lock()
door.unlock()
door.pushButton()

