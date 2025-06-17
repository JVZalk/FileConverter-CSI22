
from .decoder_interface import PayloadDecoder
from .json_decoder import JsonDecoder
from .csv_decoder import CsvDecoder
from .xml_decoder import XmlDecoder
from .dat_decoder import DatDecoder
from .binary_decoder import BinaryDecoder
from .string_decoder import StringDecoder
from .hex_decoder import HexDecoder
from src.utils.logger import logger

class DecoderFactory:
    """
    Cria e retorna a instância do decodificador correto.
    Padrão: Factory Method.
    """
    
    @staticmethod
    def get_decoder(format_name: str) -> PayloadDecoder:

        """
        Recebe o nome de um formato e retorna o objeto decodificador correspondente.
        """
        if format_name.lower() == 'json':
            return JsonDecoder()
        elif format_name.lower() == 'csv':
            return CsvDecoder()
        elif format_name.lower() == 'xml':
            return XmlDecoder()
        elif format_name.lower() == 'dat':
            return DatDecoder()
        elif format_name.lower() == 'binary':
            return BinaryDecoder()
        elif format_name.lower() == 'string':
            return StringDecoder()
        elif format_name.lower() == 'hex':
            return HexDecoder()

        else:
            raise ValueError(f"Formato de decodificador não suportado: '{format_name}'")