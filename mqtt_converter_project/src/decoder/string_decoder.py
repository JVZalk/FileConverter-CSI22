from .decoder_interface import PayloadDecoder, StandardPayload

class StringDecoder(PayloadDecoder):
    """
    Implementa um 'decoder' para um payload que já é uma string de texto simples.
    Atua como um pass-through para se encaixar no padrão de design.
    """

    def decode(self, payload: str) -> StandardPayload:
        """
        'Decodifica' uma string de texto simples, envolvendo-a em um dicionário.

        :param payload: A string de texto original.
        :return: Um dicionário {'data': 'payload original'}.
        """
        # A única "decodificação" é colocar a string no formato de dicionário padrão
        return {"data": payload}