from .decoder_interface import PayloadDecoder, StandardPayload # Supondo que as classes base existam
from src.utils.logger import logger

class HexDecoder(PayloadDecoder):
    """
    Implementa a decodificação para um payload em formato hexadecimal.
    """

    def decode(self, payload: str) -> StandardPayload:
        """
        Decodifica uma string hexadecimal para um texto legível (UTF-8).

        :param payload: A string contendo a sequência de caracteres hexadecimais.
        :return: Um dicionário {'data': 'texto decodificado'} ou um dicionário vazio em caso de erro.
        """
        if not payload or not payload.strip():
            return {}

        try:
            # Converte a string hexadecimal em bytes
            decoded_bytes = bytes.fromhex(payload)
            
            # Decodifica os bytes para uma string UTF-8
            decoded_text = decoded_bytes.decode('utf-8')
            
            # Retorna no formato padrão de dicionário
            return {"data": decoded_text}

        except (ValueError, UnicodeDecodeError) as e:
            # ValueError ocorre se a string hex for inválida (ex: tamanho ímpar)
            # UnicodeDecodeError ocorre se os bytes não formam um texto UTF-8 válido
            logger.error(f"Erro ao decodificar Hexadecimal: {e}")
            return {}