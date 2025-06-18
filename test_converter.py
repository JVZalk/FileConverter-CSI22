import os
import json

# A importação crucial da sua função universal a partir do seu pacote de projeto
from mqtt_converter_project.main import convert_to

mqtt_message_str = """
{
  "packetType": "PUBLISH",
  "dup": false,
  "qos": 1,
  "retainFlag": false,
  "topicName": "dispositivos/sensores",
  "packetId": "data-dat-001",
  "payloadFormatIndicator": 1,
  "contentType": "dat",
  "payload": "sensor_id;timestamp;temperatura;umidade;pressao\\n123;2024-06-17T10:00:00Z;25.3;60.2;1013.1\\n124;2024-06-17T10:01:00Z;24.8;61.0;1012.8"
}
"""

# --- TESTE 1: Conversão simples para XML ---
print("--- TESTE 1: CSV -> XML (sem flags) ---")
xml_output = convert_to(mqtt_message_str, 'json')
print("Resultado:\n", xml_output)