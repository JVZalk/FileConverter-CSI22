# from .decoder_interface import PayloadDecoder
# from src.core.standard_payload import StandardPayload

class CsvDecoder: # (PayloadDecoder)
    """Classe que implementa a decodificação de CSV. Padrão: Strategy (Implementação Concreta)."""

    def decode(self, payload: str): # -> StandardPayload
        """Método para decodificar um payload no formato CSV."""
        pass