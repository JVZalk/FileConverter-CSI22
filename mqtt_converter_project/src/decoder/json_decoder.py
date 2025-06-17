import json
from .decoder_interface import PayloadDecoder, StandardPayload
from src.utils.logger import logger

class JsonDecoder(PayloadDecoder):
    """
    Decodifica o formato JSON,
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
        try:
            #Converte a string JSON em um dicionário Python aninhado
            nested_data = json.loads(payload)
            
            #Chama o método auxiliar para planificar o dicionário
            flattened_data = self._flatten(nested_data)

            # Retorna o dicionário já planificado como o StandardPayload
            return flattened_data
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar JSON: {e}")
            return {}
        except Exception as e:
            logger.error(f"Erro durante o processo de planificação: {e}")
            return {}