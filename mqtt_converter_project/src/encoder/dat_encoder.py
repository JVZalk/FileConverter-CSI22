import os
from .encoder_interface import AbstractEncoder # Mantenha a mesma interface

class DatEncoder(AbstractEncoder):
    """
    Implementa o codificador para arquivos .dat (texto delimitado).
    Padrão: Strategy.
    
    Permite a customização dos separadores de coluna e linha através
    do construtor da classe.
    """

    def __init__(self, column_separator: str = ';', line_separator: str = '\n'):
        """
        Inicializa o codificador com os separadores desejados.

        :param column_separator: O caractere ou string para separar os valores (colunas)
                                 em uma mesma linha. O padrão é o ponto e vírgula ';'.
        :param line_separator: O caractere ou string para indicar o fim de uma linha.
                               O padrão é o caractere de nova linha '\n'.
        """
        self.column_separator = column_separator
        self.line_separator = line_separator


    def encode(self, data: dict, file_name = "output_data.dat") -> None:
        """
        Codifica um dicionário em uma linha de um arquivo .dat.

        Se o arquivo não existe, ele é criado com uma linha de cabeçalho
        baseada nas chaves do dicionário. Se o arquivo já existe, a nova
        linha de dados é simplesmente anexada ao final.
        """
        if not isinstance(data, dict):
            raise ValueError("Os dados recebidos pelo encoder não estão em dicionário.")

        if not file_name.endswith('.dat'):
            file_name += '.dat'

        # --- Definição do diretório de saída (lógica padrão) ---
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root_dir = os.path.abspath(os.path.join(current_script_dir, '..', '..')) 
        output_dir = os.path.join(project_root_dir, 'output')
        
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)

        try:
            # Prepara as strings de cabeçalho e dados usando os separadores definidos
            headers = data.keys()
            values = [str(v) for v in data.values()] # Garante que todos os valores são strings

            header_line = self.column_separator.join(headers) + self.line_separator
            data_line = self.column_separator.join(values) + self.line_separator

            # Verifica se o arquivo existe ou está vazio para decidir se escreve o cabeçalho
            file_exists_and_is_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0

            # Abre o arquivo em modo 'a' (append - anexar)
            # Este modo cria o arquivo se ele não existir e sempre escreve no final.
            # O parâmetro newline='' é importante para evitar conversões automáticas de fim de linha.
            with open(file_path, mode='a', encoding='utf-8', newline='') as dat_file:
                if not file_exists_and_is_not_empty:
                    # Se o arquivo é novo ou estava vazio, escreve o cabeçalho primeiro
                    dat_file.write(header_line)
                
                # Anexa a linha de dados atual
                dat_file.write(data_line)
            
            print(f"Dados codificados e salvos em {file_name}")

        except Exception as e:
            print(f"Erro ao escrever arquivo DAT: {e}")