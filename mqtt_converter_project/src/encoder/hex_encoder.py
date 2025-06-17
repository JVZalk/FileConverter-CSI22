import json
from .encoder_interface import AbstractEncoder

class HexEncoder(AbstractEncoder):
    """
    Implementa o codificador para uma string hexadecimal.
    """

    def encode(self, data: dict) -> str:
        """
        Codifica um dicionário em uma string hexadecimal.

        :param data: O dicionário a ser codificado.
        :return: Uma string contendo a representação hexadecimal dos dados.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        try:
            # 1. Serializa o dicionário para uma string JSON compacta.
            source_string = json.dumps(data, separators=(',', ':'))
            
            # 2. Converte a string para bytes usando codificação UTF-8.
            source_bytes = source_string.encode('utf-8')
            
            # 3. Converte os bytes para sua representação em string hexadecimal.
            return source_bytes.hex()
            
        except TypeError as e:
            print(f"Erro ao codificar para Hexadecimal: {e}")
            raise