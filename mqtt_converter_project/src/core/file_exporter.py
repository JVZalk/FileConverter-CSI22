class FileExporter:
    """Classe com a responsabilidade única de salvar conteúdo em arquivos."""

    @staticmethod
    def export(content: str, output_path: str):
        """Método para salvar um conteúdo de texto em um arquivo."""
        if output_path.endswith(('.binary', '.hex', '.string')):
            output_path = output_path.rsplit('.', 1)[0] + '.txt'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)