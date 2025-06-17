from .encoder_interface import AbstractEncoder

class EncoderDecorator(AbstractEncoder):
    """
    Decorador base para encoders. Permite adicionar funcionalidades extras
    (ex: logging, compressão) sem alterar o encoder original.
    """
    def __init__(self, encoder: AbstractEncoder):
        self._encoder = encoder

    def encode(self, data, file_name: str) -> None:
        self._encoder.encode(data, file_name)


from src.utils.logger import log_operation
class LoggingEncoderDecorator(EncoderDecorator):
    """
    Decorador que adiciona logging ao processo de codificação.
    """
    def encode(self, data, file_name: str) -> None:
        log_operation(f"Codificando arquivo: {file_name}")
        self._encoder.encode(data, file_name)
        log_operation(f"Arquivo {file_name} codificado com sucesso.")


from src.utils.compressor import compress_file
class CompressionEncoderDecorator(EncoderDecorator):
    """
    Decorador que adiciona compressão ao arquivo gerado após a codificação.
    """
    def encode(self, data, file_name: str) -> None:
        self._encoder.encode(data, file_name)
        compress_file(file_name)