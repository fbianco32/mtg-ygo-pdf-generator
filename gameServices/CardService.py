from abc import ABC, abstractmethod

class CardService(ABC):
    @abstractmethod
    def getCardsFromFile(totalCards: int) -> int:
        pass
