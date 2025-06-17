from .encoder_interface import AbstractEncoder
from .json_encoder import JsonEncoder
from .csv_encoder import CsvEncoder
from .dat_encoder import DatEncoder
from .xml_encoder import XmlEncoder
from .binary_encoder import BinaryEncoder
from .string_encoder import StringEncoder
from .hex_encoder import HexEncoder

class EncoderFactory:
    """
    Cria e retorna a instância do decodificador correto.
    Padrão: Factory Method.
    """
    
    @staticmethod
    def get_encoder(format_name: str) -> AbstractEncoder:

        """
        Recebe o nome de um formato e retorna o objeto codificador correspondente.
        """
        if format_name.lower() == 'json':
            return JsonEncoder()
        elif format_name.lower() == 'csv':
            return CsvEncoder()
        elif format_name.lower() == 'dat':
            return DatEncoder()
        elif format_name.lower() == 'xml':
            return XmlEncoder()
        elif format_name.lower() == 'binary':
            return BinaryEncoder()
        elif format_name.lower() == 'string':
            return StringEncoder()
        elif format_name.lower() == 'hex':
            return HexEncoder()

        else:
            raise ValueError(f"Formato de codificador não suportado: '{format_name}'")