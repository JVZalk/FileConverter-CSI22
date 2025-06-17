import json
import os

class FileReader:
    """Classe responsável por ler os arquivos de entrada e configuração."""

    def __init__(self, base_dir: str):
        """Inicializa o leitor com o diretório base do projeto."""
        self.base_dir = base_dir

    def read_config(self) -> dict:
        """Lê o arquivo de configuração e retorna um dicionário."""
        config_path = os.path.join(self.base_dir, 'config', 'settings.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config

    def read_input_packet(self, filename: str) -> dict:
        """Lê o arquivo de pacote de entrada e retorna um dicionário."""
        input_path = os.path.join(self.base_dir, 'input', filename)
        with open(input_path, 'r') as f:
            dados_do_pacote = json.load(f)
        return dados_do_pacote