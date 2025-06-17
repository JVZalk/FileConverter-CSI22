# src/core/mqtt_packet.py

class MqttPacket:
    def __init__(self, data: dict):
        self.packet_type = data.get('packetType', None)
        self.dup = data.get('dup', None)
        self.qos = data.get('qos', None)
        self.retain_flag = data.get('retainFlag', None)
        self.topic_name = data.get('topicName', None)
        self.packet_id = data.get('packetId', None)
        self.payload_format_indicator = data.get('payloadFormatIndicator', None)
        self.content_type = data.get('contentType', None)
        self.payload = data.get('payload', None)

    def __repr__(self):
        return (f"MqttPacket(payload={self.payload}, formato='{self.content_type}', "
                f"tipo='{self.packet_type}', id='{self.packet_id}', "
                f"tópico='{self.topic_name}', qos={self.qos}, retain={self.retain_flag})")