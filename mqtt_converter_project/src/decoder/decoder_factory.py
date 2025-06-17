
from .decoder_interface import PayloadDecoder
from .json_decoder import JsonDecoder
from .csv_decoder import CsvDecoder

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

        else:
            raise ValueError(f"Formato de decodificador não suportado: '{format_name}'")