import os
from ..decoder.decoder_factory import DecoderFactory
from ..encoder.encoder_factory import EncoderFactory
from src.core.mqtt_packet import MqttPacket
from .file_exporter import FileExporter
from src.utils.compressor import compress_file
from src.utils.logger import logger

class ConversionService:
    """
    [FACADE] Orquestra todo o processo de conversão de pacotes.
    """
    
    def execute_conversion(self, packet: MqttPacket, config: dict):
        """
        Executa a lógica de decodificação e codificação que antes estava na main.py.
        """
        target_format = config.get('target_format', 'txt')
        output_path = config.get('output_path', '.')  # <-- pega o output_path do settings

        formato_do_payload = packet.content_type
        payload_bruto = packet.payload

        try:
            decoder = DecoderFactory.get_decoder(formato_do_payload)
            logger.info(f"Fabrica selecionou o decodificador: {type(decoder).__name__}")

            dados_padronizados = decoder.decode(payload_bruto)

            logger.info("\nPayload decodificado:")
            logger.info(dados_padronizados)

        except ValueError as e:
            logger.error(f"\nErro durante a decodificação: {e}")
            return
        except Exception as e:
            logger.error(f"\nOcorreu um erro inesperado: {e}")
            return

        try:
            encoder = EncoderFactory.get_encoder(target_format)
            logger.info(f"\nFabrica selecionou o codificador: {type(encoder).__name__}")

            conteudo = encoder.encode(dados_padronizados)
            logger.info(conteudo)

            logger.info(f"\nDados codificados com sucesso no formato '{target_format}'.")

             # Torna o caminho absoluto em relação ao diretório do main.py
            base_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(base_dir, '..', '..'))
            output_dir = os.path.join(project_root, output_path)

            file_name = f"output_data.{target_format}"
            full_output_path = os.path.join(output_dir, file_name)
            if full_output_path.endswith(('.binary', '.hex', '.string')):
                full_output_path = full_output_path.rsplit('.', 1)[0] + '.txt'

            os.makedirs(output_dir, exist_ok=True)
            FileExporter.export(conteudo, full_output_path)

            if config.get('compression_enabled', False):
                logger.info("\nCompressao ativada. Compactando o arquivo de saida...")
                try:
                    compress_file(full_output_path)
                except Exception as e:
                    logger.error(f"Erro durante a compactação do arquivo: {e}")

        except ValueError as e:
            logger.error(f"\nErro durante a codificação: {e}")
        except Exception as e:
            logger.error(f"\nOcorreu um erro inesperado: {e}")