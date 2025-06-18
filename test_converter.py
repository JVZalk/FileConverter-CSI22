import os
import json
from mqtt_converter_project.main import convert_to

mqtt_message_str = """
{
  "packetType": "PUBLISH",
  "dup": false,
  "qos": 1,
  "retainFlag": false,
  "topicName": "dispositivos/sensores",
  "packetId": "data-json-001",
  "payloadFormatIndicator": 1,
  "contentType": "json",
  "payload": {
    "timestamp": "2024-06-17T10:00:00Z",
    "leituras": [
      {
        "sensor_id": 123,
        "temperatura": 25.3,
        "umidade": 60.2,
        "pressao": 1013.1
      },
      {
        "sensor_id": 124,
        "temperatura": 24.8,
        "umidade": 61.0,
        "pressao": 1012.8
      }
    ]
  }
}
"""

# --- TESTE 1: Conversão simples para XML ---
print("--- TESTE: ---")
xml_output = convert_to(mqtt_message_str, 'json')
print("Resultado:\n", xml_output)