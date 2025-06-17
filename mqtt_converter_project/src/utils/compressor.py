import os
import zipfile

def compress_file(file_path: str) -> str:
    """
    Compacta o arquivo especificado em um arquivo .zip no mesmo diretório.
    Retorna o caminho do arquivo .zip criado.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    zip_path = file_path + '.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        arcname = os.path.basename(file_path)
        zipf.write(file_path, arcname=arcname)
    print(f"Arquivo compactado: {zip_path}")
    return zip_path