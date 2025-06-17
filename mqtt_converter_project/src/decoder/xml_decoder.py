import xml.etree.ElementTree as ET
from .decoder_interface import PayloadDecoder, StandardPayload # Supondo que as classes base existam
from src.utils.logger import logger

class XmlDecoder(PayloadDecoder):
    """
    Decodifica o formato XML usando a biblioteca padrão do Python (ElementTree).
    Ideal para XML que representa um único registro com vários campos.
    Não requer configuração no __init__.
    Padrão: Strategy (Concreta).
    """

    def decode(self, payload: str) -> StandardPayload:
        """
        Decodifica um payload de texto XML e retorna um dicionário plano.
        """
        if not payload or not payload.strip():
            return {}

        try:
            # ET.fromstring analisa a string XML e retorna o elemento raiz
            root = ET.fromstring(payload)

            # Usa uma dictionary comprehension para criar o dicionário:
            # Para cada 'child' no elemento 'root', a chave será a tag do child
            # e o valor será o texto do child.
            data_dict = {child.tag: child.text for child in root}
            
            return data_dict

        except ET.ParseError as e:
            # Captura especificamente erros de XML malformado
            logger.error(f"Erro de parsing no XML: {e}")
            return {}
        except Exception as e:
            logger.error(f"Erro inesperado ao decodificar XML: {e}")
            return {}