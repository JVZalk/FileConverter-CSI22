class MqttPacket:
    def __init__(self, payload: any, payload_format: str, packet_type: str = None, 
                 packet_id: str = None, topic_name: str = None, 
                 payload_format_indicator: int = None, content_type: str = None, 
                 qos: int = None, retain_flag: bool = None):
        self.payload = payload
        self.payload_format = payload_format
        self.packet_type = packet_type
        self.packet_id = packet_id
        self.topic_name = topic_name
        self.payload_format_indicator = payload_format_indicator
        self.content_type = content_type
        self.qos = qos
        self.retain_flag = retain_flag
        print(f"Caixa 'MqttPacket' criada")

    def __repr__(self):
        return (f"MqttPacket(payload={self.payload}, formato='{self.payload_format}', "
                f"tipo='{self.packet_type}', id='{self.packet_id}', "
                f"tópico='{self.topic_name}', qos={self.qos}, retain={self.retain_flag})")