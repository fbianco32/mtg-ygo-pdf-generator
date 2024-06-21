from abc import ABCMeta, ABC, abstractmethod
import os
import Utils

class DeckService(ABC):
    @abstractmethod
    def prepareDecks() -> int:
        pass
