# src/core/mqtt_packet.py

class MqttPacket:
    def __init__(self, payload: any, packet_type: str = None, 
                 packet_id: str = None, topic_name: str = None, 
                 payload_format_indicator: int = None, content_type: str = None, 
                 qos: int = None, retain_flag: bool = None):
        self.payload = payload
        self.packet_type = packet_type
        self.packet_id = packet_id
        self.topic_name = topic_name
        self.payload_format_indicator = payload_format_indicator
        self.content_type = content_type
        self.qos = qos
        self.retain_flag = retain_flag

    @classmethod
    def from_dict(cls, data: dict):
        """
        [FACTORY METHOD]
        Este método de fábrica é responsável por criar uma instância de MqttPacket
        a partir de um dicionário (vindo de um JSON).
        Toda a lógica de extrair os campos fica encapsulada aqui.
        """
        print("⚙️  Usando o Factory Method 'from_dict' para criar o pacote...")
        return cls(
            payload=data.get('payload'),
            packet_type=data.get('packetType'),
            packet_id=data.get('packetId'),
            topic_name=data.get('topicName'),
            payload_format_indicator=data.get('payloadFormatIndicator'),
            content_type=data.get('contentType'),
            qos=data.get('qos'),
            retain_flag=data.get('retainFlag')
        )

    def __repr__(self):
        return (f"MqttPacket(payload={self.payload}, formato='{self.content_type}', "
                f"tipo='{self.packet_type}', id='{self.packet_id}', "
                f"tópico='{self.topic_name}', qos={self.qos}, retain={self.retain_flag})")