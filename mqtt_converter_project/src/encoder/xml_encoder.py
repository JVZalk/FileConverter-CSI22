import xml.etree.ElementTree as ET
from .encoder_interface import AbstractEncoder

class XmlEncoder(AbstractEncoder):
    """
    Implementa o codificador para o formato XML usando a biblioteca padrão do Python.
    Padrão: Strategy.
    """

    def _dict_to_etree(self, data: dict, parent: ET.Element):
        if not isinstance(data, dict):
            # Se o dado não for um dicionário (ex: numa lista de strings), 
            # o tratamos como texto simples.
            parent.text = str(data)
            return

        for key, value in data.items():
            # Cria um sub-elemento para cada chave no dicionário
            child = ET.SubElement(parent, key)
            
            if isinstance(value, dict):
                # Se o valor for outro dicionário, chama a função recursivamente
                self._dict_to_etree(value, child)
            elif isinstance(value, list):
                # Se o valor for uma lista, cria um sub-elemento 'item' para cada
                # item na lista.
                for item_data in value:
                    item = ET.SubElement(child, 'item')
                    self._dict_to_etree(item_data, item)
            else:
                # Se for um valor simples, define como o texto do elemento
                child.text = str(value)

    def encode(self, data: dict, root_element_name: str = 'root') -> str:
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        try:
            # 1. Cria o elemento raiz do XML
            root_element = ET.Element(root_element_name)
            
            # 2. Constrói a árvore XML a partir do dicionário
            self._dict_to_etree(data, root_element)
            
            # 3. (Opcional, mas recomendado) Indenta o XML para legibilidade
            # Nota: ET.indent() está disponível no Python 3.9+
            ET.indent(root_element, space="  ", level=0)
            
            # 4. Converte a árvore de elementos para uma string
            # 'unicode' retorna uma string (str), 'utf-8' retornaria bytes.
            return ET.tostring(root_element, encoding='unicode')

        except Exception as e:
            print(f"Erro ao codificar para XML com ElementTree: {e}")
            raise