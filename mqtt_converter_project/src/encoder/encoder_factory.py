from .encoder_interface import AbstractEncoder
from .json_encoder import JsonEncoder
from .csv_encoder import CsvEncoder

class DecoderFactory:
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

        else:
            raise ValueError(f"Formato de codificador não suportado: '{format_name}'")