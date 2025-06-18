import os
import json
from mqtt_converter_project.main import convert_payload_to

mqtt_message_str = """
{
  "packetType": "PUBLISH",
  "dup": false,
  "qos": 1,
  "retainFlag": false,
  "topicName": "dispositivos/sensores",
  "packetId": "data-csv-001",
  "payloadFormatIndicator": 1,
  "contentType": "csv",
  "payload": "sensor_id,timestamp,temperatura,umidade,pressao\\n123,2024-06-17T10:00:00Z,25.3,60.2,1013.1\\n124,2024-06-17T10:01:00Z,24.8,61.0,1012.8"
}
"""

# --- TESTE 1: Conversão simples para XML ---
print("--- TESTE: ---")
mensagem_convertida = convert_payload_to(mqtt_message_str, 'json')
print("Resultado:\n", mensagem_convertida)