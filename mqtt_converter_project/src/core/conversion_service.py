from ..decoder.decoder_factory import DecoderFactory
from ..encoder.encoder_factory import EncoderFactory
from .mqtt_packet import MqttPacket

class ConversionService:
    """
    [FACADE] Orquestra todo o processo de conversão de pacotes.
    """
    
    def execute_conversion(self, packet: MqttPacket, config: dict):
        """
        Executa a lógica de decodificação e codificação que antes estava na main.py.
        """
        target_format = config.get('target_format', 'txt') # Pega o formato alvo do config

        # --- Bloco DECODER (movido da main.py) ---
        formato_do_payload = packet.content_type
        payload_bruto = packet.payload

        try:
            decoder = DecoderFactory.get_decoder(formato_do_payload)
            print(f"Fábrica selecionou o decodificador: {type(decoder).__name__}")

            dados_padronizados = decoder.decode(payload_bruto)
            
            print("\nPayload decodificado:")
            print(dados_padronizados)

        except ValueError as e:
            print(f"\nErro durante a decodificação: {e}")
            return # Interrompe a execução em caso de erro
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            return # Interrompe a execução em caso de erro

        # --- Bloco ENCODER (movido da main.py) ---
        try:
            encoder = EncoderFactory.get_encoder(target_format)
            print(f"\nFábrica selecionou o codificador: {type(encoder).__name__}")

            # Codifica os dados padronizados em um arquivo
            encoder.encode(dados_padronizados, file_name="output_data")

            print(f"\nDados codificados com sucesso no formato '{target_format}'.")

        except ValueError as e:
            print(f"\nErro durante a codificação: {e}")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")