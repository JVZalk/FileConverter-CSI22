import json
from .encoder_interface import AbstractEncoder

class JsonEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos Json.
    Padrão: Strategy.
    """

    def encode(self, data: dict) -> str:
        """
        Codifica um dicionário em uma string JSON formatada.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")
        return json.dumps(data, indent=4)