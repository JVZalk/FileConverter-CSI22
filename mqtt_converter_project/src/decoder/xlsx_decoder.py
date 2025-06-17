import pandas as pd
import io
from .decoder_interface import PayloadDecoder, StandardPayload # Supondo que as classes base existam
from src.utils.logger import logger

class XlsxDecoder(PayloadDecoder):
    """
    Implementa a decodificação para o formato XLSX (Excel).
    Padrão: Strategy Concreta.
    """

    def decode(self, payload: bytes) -> StandardPayload:
        # Retorna um dicionário vazio se o payload não for fornecido
        if not payload:
            return {}

        try:
            # Usa io.BytesIO para tratar o payload binário como um arquivo em memória
            xlsx_file = io.BytesIO(payload)
            # O pandas lê o arquivo a partir do buffer em memória e o converte em um DataFrame
            df = pd.read_excel(xlsx_file)
            # Se o DataFrame estiver vazio (sem linhas de dados), retorna um dicionário vazio
            if df.empty:
                return {}
            # Seleciona a primeira linha de dados (.iloc[0]) e a converte para um dicionário
            first_row = df.iloc[0].to_dict()
            
            return first_row

        except Exception as e:
            # Captura erros de parsing, como um payload corrompido ou em formato inválido
            logger.error(f"Erro ao decodificar XLSX: {e}")
            return {}