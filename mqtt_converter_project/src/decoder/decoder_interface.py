from abc import ABC, abstractmethod

from src.core.standard_payload import StandardPayload 
class PayloadDecoder(ABC):
    
    """   
    Define o contrato para todos os decodificadores. 
    Padrão: Strategy.
    """

    @abstractmethod
    def decode(self, payload: str) -> StandardPayload:
        """
        Método abstrato obrigatório para decodificar um payload (string) e transformá-lo em um StandardPayload (dicionário).
        """
        pass