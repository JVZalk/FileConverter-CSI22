import csv
import io
from .encoder_interface import AbstractEncoder

class CsvEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos CSV.
    Padrão: Strategy.
    """

    def encode(self, data: dict) -> str:
        """
        Codifica um dicionário em uma string CSV (com cabeçalho).
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        headers = sorted(data.keys())
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerow(data)
        return output.getvalue()