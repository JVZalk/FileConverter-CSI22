import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from src.core.mqtt_packet import MqttPacket

#Leitura dos arquivos
base_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(base_dir, 'config', 'settings.json')
with open(config_path, 'r') as f:
    config = json.load(f)
    target_format = config['target_format']

input_path = os.path.join(base_dir, 'input', 'example_packet.json')
with open(input_path, 'r') as f:
    dados_do_pacote = json.load(f)

# Criação do pacote
pacote = MqttPacket.from_dict(dados_do_pacote)
print(pacote)