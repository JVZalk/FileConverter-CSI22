from abc import ABC, abstractmethod

class AbstractEncoder(ABC):
    
    """   
    Define o contrato para todos os codificadores. 
    Padrão: Strategy.
    """

    @abstractmethod
    def encode(self, data, file_name: str) -> None:
        """
        Método abstrato obrigatório para codificar um StandardPayload (dicionário) em arquivo do tipo especifico.
        """
        pass