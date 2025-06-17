import os
import pandas as pd
from .encoder_interface import AbstractEncoder # Mantenha a mesma interface

class XlsxEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos XLSX (Excel).
    Padrão: Strategy.
    """

    def encode(self, data: dict, file_name="output_data.xlsx") -> None:
        """
        Codifica um dicionário (flattened) em um arquivo CSV.
        Gerencia o cabeçalho dinamicamente e anexa dados, reescrevendo o arquivo
        se novos cabeçalhos forem detectados.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        if not file_name.endswith('.xlsx'):
            file_name += '.xlsx'

        # --- Definição do diretório de saída (idêntico ao seu código original) ---
        # Ajuste o número de '..' conforme a estrutura do seu projeto.
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root_dir = os.path.abspath(os.path.join(current_script_dir, '..', '..')) 
        output_dir = os.path.join(project_root_dir, 'output')
        
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        # Converte o novo dicionário de dados em um DataFrame do pandas de uma única linha
        df_new_row = pd.DataFrame([data])

        try:
            # Verifica se o arquivo já existe para decidir entre criar um novo ou anexar
            if os.path.exists(file_path):
                # Se o arquivo existe, lê os dados existentes para um DataFrame
                df_existing = pd.read_excel(file_path)
                
                # Concatena (anexa) a nova linha de dados ao DataFrame existente
                # ignore_index=True é importante para criar um novo índice contínuo
                df_combined = pd.concat([df_existing, df_new_row], ignore_index=True)
                
                # Salva o DataFrame combinado de volta no arquivo, sobrescrevendo o antigo
                # O parâmetro index=False evita que o índice do DataFrame seja salvo como uma coluna na planilha
                df_combined.to_excel(file_path, index=False)
            else:
                # Se o arquivo não existe, salva o DataFrame com a nova linha
                # O pandas criará automaticamente o cabeçalho a partir das chaves do dicionário
                df_new_row.to_excel(file_path, index=False)

            print(f"Dados codificados e salvos em {file_name}")

        except Exception as e:
            print(f"Erro ao escrever arquivo XLSX: {e}")