# Guia de Uso – FileConverter-CSI22

Este documento explica como utilizar o FileConverter-CSI22 tanto como aplicação executável via linha de comando quanto como biblioteca Python.

---

## Uso como Aplicação (CLI)

### Configuração

Edite o arquivo `config/settings.json` com os parâmetros desejados. Exemplo:

```json
{
  "target_format": "json",
  "input_path": "input",
  "input_file": "packet_json",
  "output_path": "output",
  "logging_enabled": true,
  "compression_enabled": false
}
```

**target_format:** Formato desejado para saída (`json`, `xml`, `csv`, `dat`, `hex`, `bin`, `string`).

**output_path:** Caminho para a pasta onde os arquivos convertidos serão salvos.

**compression_enabled:** `true` para gerar arquivos ZIP, `false` para gerar arquivos normais.

**logging_enabled:** `true` para ativar logs das operações.

### Arquivo de Entrada

Coloque seu arquivo JSON representando um pacote MQTT na pasta `input`.

O arquivo deve conter os campos do pacote, incluindo `payload`, `payload_format_indicator` e metadados.

Exemplo de entrada (`example_packet.json`):

```json
{
  "packet_id": 10,
  "topic": "iot/device/sensor",
  "payload_format_indicator": "hex",
  "content_type": "sensor/data",
  "qos": 1,
  "retain": false,
  "payload": "7B2274656D70223A32357D"
}
```

### Execução

Execute o sistema com:

```bash
python main.py
```

### Saída

O arquivo convertido será salvo na pasta `output` no formato definido.

Se `compression_enabled` estiver ativado, um arquivo `.zip` será gerado.

Logs detalhados estarão disponíveis no arquivo `activity.log`.

## Uso como Biblioteca

O conversor pode ser usado diretamente dentro de outros scripts Python.

### Exemplo de Uso:

```python
from src.core.conversion_service import convert_payload_to
from src.core.mqtt_packet import MqttPacket

# Carregar o pacote MQTT a partir de JSON
packet = MqttPacket.from_json('input/example_packet.json')

# Realizar a conversão para CSV (sem salvar arquivo)
converted_payload = convert_payload_to(packet, target_format="csv")

print(converted_payload)
```

O resultado será uma string no formato de saída desejado.

O arquivo não é salvo quando se usa a função `convert_payload_to` diretamente.

## Observações

- O sistema não se conecta a um broker MQTT. A entrada é sempre um arquivo JSON representando o pacote.

- Para adicionar novos formatos, implemente um Decoder e um Encoder e registre nas fábricas correspondentes.

- Suporte completo a compressão e logging, configurável no arquivo settings.json.

## Dúvidas

Consulte também:

- [README](../../README.md)
- [Arquitetura](./architecture.md)
- [Diagrama de Classes](./classdiagram.png)
- [Diagrama de Sequência](./sequencediagram.png)
