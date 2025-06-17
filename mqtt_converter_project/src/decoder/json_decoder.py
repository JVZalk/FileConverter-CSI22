import json
from .decoder_interface import PayloadDecoder, StandardPayload

class JsonDecoder(PayloadDecoder):
    """
    Implementa a decodificação para o formato JSON.
    Padrão: Strategy (Concreta).
    """

    def decode(self, payload: str) -> StandardPayload:
        try:
            return json.loads(payload)
        except json.JSONDecodeError as e:
            return {}