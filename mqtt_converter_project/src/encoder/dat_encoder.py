import os
from .encoder_interface import AbstractEncoder

class DatEncoder(AbstractEncoder):
    def __init__(self, column_separator: str = ';', placeholder: str = ''):
        self.column_separator = column_separator
        self.placeholder = placeholder
        self.line_separator = '\n'

    def encode(self, data: dict) -> str:
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        # Gere apenas a linha de dados (sem salvar em arquivo)
        headers = sorted(data.keys())
        values = [str(data.get(key, self.placeholder)) for key in headers]
        # Retorne cabeçalho + linha, ou só a linha se preferir
        return self.column_separator.join(headers) + self.line_separator + self.column_separator.join(values) + self.line_separator