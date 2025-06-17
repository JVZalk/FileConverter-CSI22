from abc import ABC, abstractmethod

class PayloadDecoder(ABC):
    """Define o contrato para todos os decodificadores. Padrão: Strategy (Interface)."""

    @abstractmethod
    def decode(self, payload: str):
        """Método abstrato para decodificar um payload de string para um formato padrão."""
        pass