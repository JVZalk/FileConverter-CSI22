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

    def _flatten(self, data: dict, parent_key: str = '', sep: str = '.', list_idx_sep: str = '_') -> StandardPayload:
        items = {}
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self._flatten(v, new_key, sep=sep, list_idx_sep=list_idx_sep))
            elif isinstance(v, list):
                for i, list_item in enumerate(v):
                    list_new_key = f"{new_key}{list_idx_sep}{i}"
                    if isinstance(list_item, (dict, list)):
                        items.update(self._flatten(list_item, list_new_key, sep=sep, list_idx_sep=list_idx_sep))
                    else:
                        items[list_new_key] = list_item
            else:
                items[new_key] = v
        return items

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
            nested_data = {child.tag: child.text for child in root}

            # Chama o método auxiliar para planificar o dicionário
            flattened_data = self._flatten(nested_data)
            
            # Retorna o dicionário já planificado como o StandardPayload
            return flattened_data

        except ET.ParseError as e:
            # Captura especificamente erros de XML malformado
            logger.error(f"Erro de parsing no XML: {e}")
            return {}
        except Exception as e:
            logger.error(f"Erro inesperado ao decodificar XML: {e}")
            return {}