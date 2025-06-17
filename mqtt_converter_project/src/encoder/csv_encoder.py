import os
import csv
from .encoder_interface import AbstractEncoder

class CsvEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos CSV.
    Padrão: Strategy.
    """

    def encode(self, data, file_name: str) -> None:
        """
        Codifica um StandardPayload (dicionário) em um arquivo CSV.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder nao estao em dicionario.")

        if not file_name.endswith('.csv'):
            file_name += '.csv'

        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'output')
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print(f"Dados codificados e salvos em {file_name}")