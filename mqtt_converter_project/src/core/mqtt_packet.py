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
        self.message_expiry_interval = data.get('messageExpiryInterval', None)
        self.topic_alias = data.get('topicAlias', None)
        self.response_topic = data.get('responseTopic', None)
        self.correlation_data = data.get('correlationData', None)
        self.user_property = data.get('userProperty', None)
        self.subscription_identifier = data.get('subscriptionIdentifier', None)
        self.content_type = data.get('contentType', None)
        self.payload = data.get('payload', None)

    def __repr__(self):
        attrs = []
        for attr, value in self.__dict__.items():
            if value is not None:
                attrs.append(f"{attr}={repr(value)}")
        return f"MqttPacket({', '.join(attrs)})"