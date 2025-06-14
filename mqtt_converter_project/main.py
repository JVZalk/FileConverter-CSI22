import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from src.core.mqtt_packet import MqttPacket

base_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(base_dir, 'config', 'settings.json')
with open(config_path, 'r') as f:
    config = json.load(f)
    target_format = config['target_format']

input_path = os.path.join(base_dir, 'input', 'example_packet.json')
with open(input_path, 'r') as f:
    dados_do_pacote = json.load(f)

pacote = MqttPacket(
    payload=dados_do_pacote['payload'],
    payload_format=dados_do_pacote.get('contentType', 'unknown'),
    packet_type=dados_do_pacote.get('packetType'),
    packet_id=dados_do_pacote.get('packetId'),
    topic_name=dados_do_pacote.get('topicName'),
    payload_format_indicator=dados_do_pacote.get('payloadFormatIndicator'),
    content_type=dados_do_pacote.get('contentType'),
    qos=dados_do_pacote.get('qos'),
    retain_flag=dados_do_pacote.get('retainFlag')
)

print(pacote)


