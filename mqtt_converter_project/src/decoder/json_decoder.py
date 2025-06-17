# from .decoder_interface import PayloadDecoder
# from src.core.standard_payload import StandardPayload

class JsonDecoder: # (PayloadDecoder)
    """Classe que implementa a decodificação de JSON. Padrão: Strategy (Implementação Concreta)."""

    def decode(self, payload: str): # -> StandardPayload
        """Método para decodificar um payload no formato JSON."""
        pass