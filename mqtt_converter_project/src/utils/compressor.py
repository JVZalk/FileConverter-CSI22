import os
import zipfile
from src.utils.logger import logger

def compress_file(file_path: str) -> str:
    """
    Compacta o arquivo especificado em um arquivo .zip no mesmo diretório.
    Retorna o caminho do arquivo .zip criado.
    """
    if not os.path.isfile(file_path):
        logger.error(f"Arquivo não encontrado: {file_path}")
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    base_dir = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    name_before_dot = base_name.split('.', 1)[0]
    zip_path = os.path.join(base_dir, name_before_dot + '.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        arcname = os.path.basename(file_path)
        zipf.write(file_path, arcname=arcname)
    logger.info(f"Arquivo compactado: {zip_path}")
    os.remove(file_path)  # Remove o arquivo original após compactação
    return zip_path
