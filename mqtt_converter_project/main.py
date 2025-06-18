# main.py

import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Imports de alto nível
from src.utils.file_reader import FileReader
from src.core.mqtt_packet import MqttPacket
from src.core.conversion_service import ConversionService
from src.utils.logger import logger


def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. Leitura de dados pelo FileReader
    reader = FileReader(base_dir)
    config = reader.read_config()
    logger.set_enabled(config.get('logging_enabled', False))
    logger.info("--- INICIANDO APLICACAO ---")
    logger.info(f"Configuração lida: {config}")
    dados_do_pacote = reader.read_input_packet(config)

    # 2. Criação do pacote
    pacote = MqttPacket(dados_do_pacote)
    logger.info("Pacote MQTT criado:")
    logger.info(pacote)

    # 3. Execução da conversão pelo ConversionService
    logger.info("\n--- INICIANDO SERVICO DE CONVERSAO ---")
    service = ConversionService()
    service.execute_conversion(pacote, config)

    logger.info("\n--- APLICACAO FINALIZADA ---")

# --- A FUNÇÃO UNIVERSAL ---
def convert_to(content: str, output_format: str, logging_enabled: bool = False, compression_enabled: bool = False) -> str:

    config = {
        "target_format": output_format,
        "input_path": "input",
        "output_path": "output",
        "logging_enabled": logging_enabled,
        "compression_enabled": compression_enabled
    }

    logger.set_enabled(config.get('logging_enabled', False))
    logger.info("--- INICIANDO APLICACAO ---")
    logger.info(f"Configuração lida: {config}")
    dados_do_pacote = json.loads(content)

    # 2. Criação do pacote
    pacote = MqttPacket(dados_do_pacote)
    logger.info("Pacote MQTT criado:")
    logger.info(pacote)

    # 3. Execução da conversão pelo ConversionService
    logger.info("\n--- INICIANDO SERVICO DE CONVERSAO ---")
    service = ConversionService()
    output_content = service.execute_conversion(pacote, config)

    logger.info("\n--- APLICACAO FINALIZADA ---")
    return output_content
    


if __name__ == "__main__":
    main()