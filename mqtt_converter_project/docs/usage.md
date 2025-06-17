# Guia de Uso - CSI22 File Converter

Este projeto converte pacotes MQTT de IoT em diferentes formatos de arquivo, facilitando a integração de dados.

## 1. Pré-requisitos

- Python 3.8+
- Instale as dependências:
  ```
  pip install -r requirements.txt
  ```

## 2. Preparando os arquivos

- Coloque o arquivo de entrada (ex: `example_packet.json`) na pasta `input/`.
- Edite as preferências no arquivo `config/settings.json`:
  - `target_format`: formato de saída (`json`, `csv`, `dat`, `xml`)
  - `output_path`: pasta de saída (ex: `output`)
  - `compression_enabled`: `true` para compactar o arquivo final

## 3. Executando o conversor

No terminal, execute:
```
python main.py
```

## 4. Resultados

- O arquivo convertido será salvo na pasta definida em `output_path`.
- Se a compressão estiver ativada, será gerado um `.zip`.

## 5. Exemplo de configuração

```json
{
  "target_format": "csv",
  "output_path": "output",
  "compression_enabled": true
}
```

## 6. Observações

- O log da aplicação é salvo em `activity.log` (se ativado).
- Para converter outros arquivos, basta trocar o arquivo na pasta `input/` e repetir o processo.