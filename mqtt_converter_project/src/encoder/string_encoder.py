import json
from .encoder_interface import AbstractEncoder

class StringEncoder(AbstractEncoder):
    """
    Implementa o codificador para uma string de texto padrão (formato JSON compacto).
    """

    def encode(self, data: dict) -> str:
        """
        Codifica um dicionário em uma string JSON compacta.

        :param data: O dicionário a ser codificado.
        :return: Uma string contendo os dados em formato JSON.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")
        
        try:
            # Usa json.dumps para criar a representação em string.
            # separators=(',', ':') remove espaços em branco para uma saída mais compacta.
            return json.dumps(data, separators=(',', ':'))
        except TypeError as e:
            print(f"Erro ao codificar para String/JSON: {e}")
            raise