# main.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Imports de alto nível
from src.utils.file_reader import FileReader
from src.core.mqtt_packet import MqttPacket
from src.core.conversion_service import ConversionService

def main():

    print("--- INICIANDO APLICAÇÃO ---")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. Leitura de dados pelo FileReader
    reader = FileReader(base_dir)
    config = reader.read_config()
    dados_do_pacote = reader.read_input_packet('example_packet.json')

    # 2. Criação do pacote
    pacote = MqttPacket(dados_do_pacote)
    print("Pacote MQTT criado:")
    print(pacote)

    # 3. Execução da conversão pelo ConversionService
    print("\n--- INICIANDO SERVIÇO DE CONVERSÃO ---")
    service = ConversionService()
    service.execute_conversion(pacote, config)

    print("\n--- APLICAÇÃO FINALIZADA ---")

if __name__ == "__main__":
    main()
