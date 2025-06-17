from .encoder_interface import AbstractEncoder
from .json_encoder import JsonEncoder
from .csv_encoder import CsvEncoder
from .dat_encoder import DatEncoder
from .xml_encoder import XmlEncoder

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

        else:
            raise ValueError(f"Formato de codificador não suportado: '{format_name}'")