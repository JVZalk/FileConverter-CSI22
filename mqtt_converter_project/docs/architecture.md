# Arquitetura do Projeto - CSI22 File Converter

## Visão Geral

O projeto segue princípios de Programação Orientada a Objetos (POO) e utiliza padrões como Facade, Factory, Strategy e Decorator para modularidade, flexibilidade e extensão. Também adota princípios SOLID, como o SRP (Single Responsibility Principle).

## Componentes Principais

- **main.py**: Ponto de entrada. Orquestra a leitura de arquivos, criação do pacote MQTT e chamada do serviço de conversão.
- **src/core/conversion_service.py**: [Facade] Centraliza o fluxo de conversão (decodificação, codificação, exportação e compressão).
- **src/core/mqtt_packet.py**: Representa o pacote MQTT como objeto.
- **src/decoder/**: Implementa decodificadores para diferentes formatos de entrada (JSON, CSV, XML, DAT, etc.) usando o padrão Strategy.
- **src/encoder/**: Implementa codificadores para diferentes formatos de saída usando o padrão Strategy.
- **src/utils/**: Utilitários para leitura de arquivos, logging e compressão, aplicando o padrão Decorator para adicionar funcionalidades como compressão e logging sem alterar a lógica principal.

## Padrões de Projeto

- **Facade**: `ConversionService` simplifica o uso do sistema para o usuário.
- **Factory**: `DecoderFactory` e `EncoderFactory` instanciam dinamicamente o decodificador/codificador correto.
- **Strategy**: Cada formato de entrada/saída é uma estratégia independente.
- **Decorator**: Utilizado para adicionar funcionalidades como compressão de arquivos (`compress_file`) e logging, permitindo estender comportamentos sem modificar as classes principais.

## Princípios de Projeto

- **SRP (Single Responsibility Principle)**: Cada classe tem uma responsabilidade única, facilitando manutenção e testes.
- **SOLID**: O projeto busca seguir outros princípios SOLID, como a separação de interfaces e a inversão de dependências, promovendo código limpo e desacoplado.

## Fluxo de Dados

1. O usuário coloca um arquivo na pasta `input/`.
2. O `main.py` lê as configurações e o arquivo de entrada.
3. Um objeto `MqttPacket` é criado.
4. O `ConversionService`:
   - Seleciona o decodificador adequado via `DecoderFactory`.
   - Decodifica o payload para um formato padrão.
   - Seleciona o codificador via `EncoderFactory`.
   - Codifica os dados no formato desejado.
   - Exporta o arquivo para a pasta de saída.
   - (Opcional) Aplica compressão usando o padrão Decorator.
   - (Opcional) Realiza logging das operações.

## Diagramas

- Consulte os diagramas de classe e sequência em `docs/classdiagram.png` e `docs/sequencediagram.png`.

## Extensibilidade

- Para adicionar novos formatos, basta criar uma nova classe de decoder/encoder e registrar na respectiva Factory.
- Novas funcionalidades (ex: criptografia, validação) podem ser adicionadas facilmente usando o padrão Decorator.

---