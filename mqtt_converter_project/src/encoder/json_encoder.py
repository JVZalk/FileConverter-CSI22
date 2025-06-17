import os
import json
from .encoder_interface import AbstractEncoder

class JsonEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos Json.
    Padrão: Strategy.
    """

    def encode(self, data: dict, file_name = "output_data.json") -> None:
        """
        Codifica um dicionário (flattened JSON) em um arquivo json.
        Gerencia o cabeçalho dinamicamente e anexa dados, reescrevendo o arquivo
        se novos cabeçalhos forem detectados.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        if not file_name.endswith('.json'):
            file_name += '.json'

        # Definição do diretório de saída
        # Ajuste o número de '..' conforme a estrutura do seu projeto.
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root_dir = os.path.abspath(os.path.join(current_script_dir, '..', '..')) 
        output_dir = os.path.join(project_root_dir, 'output')
        
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        # Lista para armazenar todos os registros (existentes + o novo)
        all_records = []

        # Tentar ler o conteúdo existente do arquivo JSON
        # Verifica se o arquivo existe e não está vazio para tentar ler
        file_exists_and_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0 
        
        if file_exists_and_not_empty:
            try:
                with open(file_path, mode='r', encoding='utf-8') as jsonfile_read:
                    existing_content = json.load(jsonfile_read) # Carrega o JSON inteiro
                    
                    if isinstance(existing_content, list):
                        # Se o arquivo já é uma lista de objetos, estendemos ela
                        all_records.extend(existing_content) 
                    elif isinstance(existing_content, dict):
                        # Se o arquivo era um único objeto, tratamos como a primeira entrada da nova lista
                        all_records.append(existing_content) 
                    else:
                        # Se o JSON existente não é uma lista nem um objeto, é um formato inesperado
                        print(f"Aviso: O conteúdo de '{file_name}' não é uma lista ou objeto JSON válido. O arquivo será sobrescrito.")
                        # all_records permanece vazia, efetivamente iniciando um novo arquivo
            except json.JSONDecodeError as e:
                # Ocorre se o arquivo não é um JSON válido
                print(f"Aviso: Arquivo JSON existente '{file_name}' está corrompido ou malformado. Iniciando um novo arquivo. Erro: {e}")
                # all_records permanece vazia
            except Exception as e:
                # Outros erros de leitura
                print(f"Aviso: Erro ao ler arquivo JSON existente '{file_name}'. Iniciando um novo arquivo. Erro: {e}")
                # all_records permanece vazia

        # Adicionar o novo dado (o dicionário achatado) à lista de registros
        all_records.append(data)

        # Reescrever o arquivo com a lista completa e atualizada de registros
        # Sempre abrimos em modo 'w' (write) porque estamos escrevendo a estrutura completa (o array JSON)
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as jsonfile_write:
                # json.dump escreve o objeto Python (neste caso, a lista) como uma string JSON
                json.dump(all_records, jsonfile_write, indent=4) # indent=4 para legibilidade
            print(f"Dados codificados e salvos em {file_name}")
        except Exception as e:
            print(f"Erro ao escrever arquivo JSON: {e}")