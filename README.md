# CSI22 File Converter - IoT Data Converter

Este projeto é um conversor de arquivos orientado a objetos, desenvolvido para aplicações de IoT. Ele permite transformar pacotes de dados MQTT em diferentes formatos (JSON, CSV, DAT, XLSX), facilitando a integração e análise de dados de dispositivos conectados.

## Como funciona

- O sistema lê pacotes MQTT do diretório `input/` (exemplo: `example_packet.json`).
- O formato de entrada e saída, além de preferências como compressão, são definidos no arquivo `config/settings.json`.
- O pacote é decodificado, convertido para o formato desejado e salvo em `output/`.
- Opcionalmente, o arquivo de saída pode ser compactado automaticamente.

## Como usar

1. **Coloque o arquivo de entrada**  
   Salve o arquivo MQTT (ex: `example_packet.json`) no diretório `input/`.

2. **Configure as preferências**  
   Edite o arquivo [`config/settings.json`](config/settings.json) para definir:
   - `target_format`: formato de saída desejado (`json`, `csv`, `dat`, `xlsx`)
   - `output_path`: pasta de saída (normalmente `output`)
   - `compression_enabled`: `true` para compactar o arquivo final em `.zip`

3. **Execute o conversor**  
   No terminal, rode:
   - `CSI22-FileConverter\mqtt_converter_project\main.py`


4. **Resultado**  
O arquivo convertido aparecerá em `output/` no formato escolhido. Se a compressão estiver ativada, será gerado um `.zip`.

## Exemplo de configuração (`config/settings.json`)
```json
{
  "target_format": "dat",
  "output_path": "output",
  "compression_enabled": true
}