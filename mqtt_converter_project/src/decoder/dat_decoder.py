import csv
import io
from .decoder_interface import PayloadDecoder, StandardPayload # Supondo que as classes base existam

class DatDecoder(PayloadDecoder):
    """
    Implementa a decodificação para o formato .dat (texto delimitado).
    Padrão: Strategy Concreta.
    """

    def __init__(self, column_separator: str = ';'):
        self.separator = column_separator

    def decode(self, payload: str) -> StandardPayload:
        # Retorna um dicionário vazio se o payload não for fornecido
        if not payload:
            return {}

        try:
            # Usa io.StringIO para tratar a string do payload como se fosse um arquivo
            dat_file = io.StringIO(payload)

            # Usa csv.DictReader, que é perfeito para esta tarefa. Ele lê a primeira
            # linha como cabeçalho e as seguintes como dados.
            # A chave aqui é passar o delimitador customizado.
            reader = csv.DictReader(dat_file, delimiter=self.separator)
            
            # Pega o primeiro dicionário da lista (a primeira linha de dados)
            # next(reader, None) é uma forma segura de pegar o próximo item,
            # retornando None se não houver linhas de dados.
            first_row = next(reader, None)
            
            return first_row if first_row is not None else {}

        except Exception as e:
            # Captura erros de parsing, como um payload malformado
            print(f"Erro ao decodificar DAT: {e}")
            return {}