import json
from .encoder_interface import AbstractEncoder

class BinaryEncoder(AbstractEncoder):
    """
    Implementa o codificador para uma string de '0's e '1's (representação binária textual).
    """

    def encode(self, data: dict) -> str:
        """
        Codifica um dicionário em uma string de representação binária.

        :param data: O dicionário a ser codificado.
        :return: Uma string contendo a representação binária dos dados.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        try:
            # 1. Serializa o dicionário para uma string JSON compacta.
            source_string = json.dumps(data, separators=(',', ':'))
            
            # 2. Converte a string para bytes usando codificação UTF-8.
            source_bytes = source_string.encode('utf-8')
            
            # 3. Converte cada byte em sua representação de 8 bits e junta tudo.
            #    format(byte, '08b') garante que cada byte seja representado com 8 dígitos.
            return "".join(format(byte, '08b') for byte in source_bytes)

        except TypeError as e:
            print(f"Erro ao codificar para Binário: {e}")
            raise