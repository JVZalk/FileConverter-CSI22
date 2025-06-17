# main.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Imports de alto nível
from src.utils.file_reader import FileReader
from src.core.mqtt_packet import MqttPacket
from src.core.conversion_service import ConversionService
from src.utils.logger import logger


def main():

    logger.info("--- INICIANDO APLICAÇÃO ---")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. Leitura de dados pelo FileReader
    reader = FileReader(base_dir)
    config = reader.read_config()
    dados_do_pacote = reader.read_input_packet('packet_binary.json')

    # 2. Criação do pacote
    pacote = MqttPacket(dados_do_pacote)
    logger.info("Pacote MQTT criado:")
    logger.info(pacote)

    # 3. Execução da conversão pelo ConversionService
    logger.info("\n--- INICIANDO SERVIÇO DE CONVERSÃO ---")
    service = ConversionService()
    service.execute_conversion(pacote, config)

    logger.info("\n--- APLICAÇÃO FINALIZADA ---")

if __name__ == "__main__":
    main()