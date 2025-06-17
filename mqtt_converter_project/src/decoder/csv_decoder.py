import csv
import io
from .decoder_interface import PayloadDecoder, StandardPayload

class CsvDecoder(PayloadDecoder):
    """
    Implementa a decodificação para o formato CSV.
    Padrão: Strategy Concreta).
    """

    def decode(self, payload: str) -> StandardPayload:

        try:
            # Usa io.StringIO para tratar a string do payload como se fosse um arquivo
            csv_file = io.StringIO(payload)
            # DictReader lê o CSV e já usa o cabeçalho para criar dicionários
            reader = csv.DictReader(csv_file)
            # Pega o primeiro dicionário da lista (a primeira linha de dados)
            first_row = next(reader, None)
            return first_row if first_row is not None else {}
        except Exception as e:
            print(f"Erro ao decodificar CSV: {e}")
            return {}