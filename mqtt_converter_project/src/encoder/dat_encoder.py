import os
from .encoder_interface import AbstractEncoder

class DatEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos .dat (texto delimitado) de forma robusta,
    com nomes de variáveis padronizados com base no CsvEncoder.
    """

    def __init__(self, column_separator: str = ';', placeholder: str = ''):
        """
        Inicializa o codificador com os separadores e placeholders desejados.

        :param column_separator: O caractere para separar as colunas. Padrão: ';'.
        :param placeholder: O valor a ser usado para dados ausentes. Padrão: string vazia.
        """
        self.column_separator = column_separator
        self.placeholder = placeholder
        self.line_separator = '\n'

    def encode(self, data: dict, file_name="output_data.dat") -> None:
        """
        Codifica um dicionário em uma linha de um arquivo .dat.
        Gerencia o cabeçalho dinamicamente e reescreve o arquivo se novos
        cabeçalhos forem detectados.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        if not file_name.endswith('.dat'):
            file_name += '.dat'

        # --- Definição do diretório de saída ---
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root_dir = os.path.abspath(os.path.join(current_script_dir, '..', '..'))
        output_dir = os.path.join(project_root_dir, 'output')
        
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        # 1. Obter cabeçalhos e dados existentes
        existing_file_headers = []
        existing_rows_data = []

        file_is_new_or_empty = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

        if not file_is_new_or_empty:
            try:
                with open(file_path, mode='r', encoding='utf-8') as datfile_read:
                    header_line = datfile_read.readline().strip()
                    if header_line:
                        existing_file_headers = header_line.split(self.column_separator)
                        
                        for line in datfile_read:
                            line = line.strip()
                            if line:
                                values = line.split(self.column_separator)
                                row_data = dict(zip(existing_file_headers, values))
                                existing_rows_data.append(row_data)
            except Exception as e:
                print(f"Aviso: Não foi possível ler o arquivo .dat existente. Será tratado como novo. Erro: {e}")
                file_is_new_or_empty = True

        # 2. Combinar cabeçalhos e verificar se houve mudança
        current_data_keys = sorted(data.keys())
        all_unique_headers = sorted(list(set(existing_file_headers + current_data_keys)))
        header_changed = (all_unique_headers != existing_file_headers)

        # 3. Executar a escrita (reescrever ou anexar)
        try:
            if header_changed or file_is_new_or_empty:
                # --- Reescreve o arquivo inteiro ---
                with open(file_path, mode='w', encoding='utf-8') as datfile_write:
                    datfile_write.write(self.column_separator.join(all_unique_headers) + self.line_separator)
                    
                    for row_data in existing_rows_data:
                        ordered_values = [row_data.get(key, self.placeholder) for key in all_unique_headers]
                        datfile_write.write(self.column_separator.join(ordered_values) + self.line_separator)
                    
                    new_ordered_values = [str(data.get(key, self.placeholder)) for key in all_unique_headers]
                    datfile_write.write(self.column_separator.join(new_ordered_values) + self.line_separator)
            else:
                # --- Apenas anexa a nova linha ---
                with open(file_path, mode='a', encoding='utf-8') as datfile_append:
                    ordered_values = [str(data.get(key, self.placeholder)) for key in existing_file_headers]
                    datfile_append.write(self.column_separator.join(ordered_values) + self.line_separator)

            print(f"Dados codificados e salvos em {file_name}")

        except Exception as e:
            print(f"Erro ao escrever no arquivo .dat: {e}")