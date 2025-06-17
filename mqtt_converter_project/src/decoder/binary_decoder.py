from .decoder_interface import PayloadDecoder, StandardPayload
from src.utils.logger import logger

class BinaryDecoder(PayloadDecoder):
    """
    Implementa a decodificação para um payload em formato de string binária (0s e 1s).
    """

    def decode(self, payload: str) -> StandardPayload:
        """
        Decodifica uma string de '0's e '1's para um texto legível (UTF-8).
        """
        if not payload or not payload.strip():
            return {}

        try:
            # Converte a string binária em um único número inteiro
            binary_int = int(payload, 2)
            
            # Calcula o número de bytes necessários para representar esse inteiro
            byte_number = (binary_int.bit_length() + 7) // 8
            
            # Converte o inteiro para uma sequência de bytes
            decoded_bytes = binary_int.to_bytes(byte_number, "big")
            
            # Decodifica os bytes para uma string UTF-8
            decoded_text = decoded_bytes.decode('utf-8')
            
            return {"data": decoded_text}
            
        except (ValueError, UnicodeDecodeError) as e:
            logger.error(f"Erro ao decodificar Binário: {e}")
            return {}