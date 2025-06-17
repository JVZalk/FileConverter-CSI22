# from .decoder_interface import PayloadDecoder
# from .json_decoder import JsonDecoder
# ... outros imports

class DecoderFactory:
    """Classe que cria a instância do decodificador correto."""

    @staticmethod
    def get_decoder(format_name: str): # -> PayloadDecoder
        """Método para retornar o decodificador apropriado. Padrão: Factory Method."""
        pass