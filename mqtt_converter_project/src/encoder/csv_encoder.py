import os
import csv
from .encoder_interface import AbstractEncoder

class CsvEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos CSV.
    Padrão: Strategy.
    """

    def encode(self, data: dict, file_name = "output_data.csv") -> None:
        """
        Codifica um dicionário (flattened JSON) em um arquivo CSV.
        Gerencia o cabeçalho dinamicamente e anexa dados, reescrevendo o arquivo
        se novos cabeçalhos forem detectados.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        if not file_name.endswith('.csv'):
            file_name += '.csv'

        # Definição do diretório de saída
        # Calculado dinamicamente para subir três níveis a partir do diretório do script atual
        # e encontrar a pasta 'output'. Ajuste conforme a estrutura do seu projeto.
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Ex: se csv_encoder.py está em 'project_root/src/main/python/encoders/',
        # os.path.join(current_script_dir, '..', '..', '..') leva a 'project_root'
        project_root_dir = os.path.abspath(os.path.join(current_script_dir, '..', '..'))
        output_dir = os.path.join(project_root_dir, 'output')
        
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        # 1. Obter os cabeçalhos existentes no arquivo e no cache (se houver)
        existing_file_headers = []
        existing_rows_data = [] # Para armazenar as linhas existentes se for necessário reescrever

        file_is_new_or_empty = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

        if not file_is_new_or_empty:
            try:
                with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile_read:
                    reader = csv.DictReader(csvfile_read)
                    existing_file_headers = reader.fieldnames if reader.fieldnames else []
                    # Ler todas as linhas existentes
                    for row in reader:
                        existing_rows_data.append(row)
            except Exception as e:
                # Trata casos onde o arquivo pode estar corrompido ou o cabeçalho é inválido
                print(f"Aviso: Não foi possível ler o arquivo existente para atualização de cabeçalho. Ele será tratado como novo/vazio. Erro: {e}")
                existing_file_headers = []
                existing_rows_data = []
                file_is_new_or_empty = True
        
        # Obter as chaves da mensagem atual (já achatada)
        current_data_keys = sorted(data.keys())

        # Combinar todos os cabeçalhos (existentes no arquivo + novos da mensagem atual)
        # Usamos um set para garantir unicidade e depois ordenamos
        all_unique_headers = sorted(list(set(existing_file_headers + current_data_keys)))

        # 2. Decidir se o cabeçalho mudou (e se o arquivo precisa ser reescrito)
        # Comparamos as listas, não apenas os sets, para detectar mudança na ordem também, se relevante
        header_changed = (all_unique_headers != existing_file_headers) 

        # 3. Executar a escrita (reescrever tudo ou apenas anexar)
        if header_changed or file_is_new_or_empty:
            # Reabrir em modo 'w' para reescrever TUDO (cabeçalho + dados antigos + dados novos)
            with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile_write:
                writer = csv.DictWriter(csvfile_write, fieldnames=all_unique_headers)
                writer.writeheader()
                
                # Reescrever todas as linhas antigas, adaptando-as ao novo conjunto de cabeçalhos
                for row_data in existing_rows_data:
                    # Garantir que todas as colunas do novo cabeçalho estejam presentes, preenchendo com vazio
                    writer.writerow({key: row_data.get(key, "") for key in all_unique_headers})
                
                # Escrever a nova linha de dados (da mensagem atual)
                writer.writerow({key: data.get(key, "") for key in all_unique_headers})
            
            # Atualizar o cache de cabeçalhos com o novo conjunto
            self._file_headers_cache[file_path] = all_unique_headers
            
        else:
            # Apenas anexar a nova linha, pois os cabeçalhos não mudaram
            with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile_append:
                # O DictWriter deve ser inicializado com os mesmos fieldnames com os quais o arquivo foi criado
                # (ou seja, os all_unique_headers que já foram gravados e são os existentes)
                writer = csv.DictWriter(csvfile_append, fieldnames=existing_file_headers) 
                # Preencher a linha com valores para todas as colunas esperadas, usando "" para ausentes
                writer.writerow({key: data.get(key, "") for key in existing_file_headers}) 

        print(f"Dados codificados e salvos em {file_name}")
