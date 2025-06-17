from abc import ABC, abstractmethod

class AbstractEncoder(ABC):
    """   
    Define o contrato para todos os codificadores. 
    Padrão: Strategy.
    """
    @abstractmethod
    def encode(self, data: dict) -> str:
        """
        Método abstrato para codificar um dicionário em uma STRING no formato específico.
        """
        pass