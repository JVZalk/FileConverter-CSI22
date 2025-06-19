
# FileConverter-CSI22

Conversor de arquivos para integração em sistemas IoT com MQTT. Este middleware permite a conversão de payloads de pacotes MQTT entre diversos formatos de dados, como JSON, XML, CSV, DAT, Binário, Hexadecimal e String, garantindo interoperabilidade entre dispositivos heterogêneos.

---

## Funcionalidades

- Conversão de payloads entre múltiplos formatos.
- Detecção automática do formato de entrada.
- Suporte a uso como aplicação (linha de comando) ou como biblioteca.
- Exportação dos dados convertidos como arquivos `.txt` UTF-8.
- Compressão opcional (ZIP).
- Logging detalhado das operações (opcional).
- Arquitetura modular e extensível.

---

## Arquitetura

A arquitetura do projeto segue princípios de Programação Orientada a Objetos e padrões de projeto como:

- Factory Method
- Strategy
- Facade
- Singleton
- (Parcial) Decorator

O detalhamento completo da arquitetura está no arquivo [`architecture.md`](./architecture.md).

---

## Estrutura de Pastas

```
mqtt_converter_project/
├── main.py                
├── config/                
├── input/                 
├── output/                
├── src/                   
│   ├── core/              
│   ├── decoder/           
│   ├── encoder/           
│   └── utils/             
├── tests/                 
└── docs/                  
```

---

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/SeuUsuario/FileConverter-CSI22.git
cd FileConverter-CSI22
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## Uso como Aplicação

1. Configure o arquivo `config/settings.json`:
```json
{
  "target_format": "json",
  "output_path": "output/",
  "compression_enabled": true,
  "logging_enabled": true
}
```

2. Coloque o arquivo de pacote MQTT no diretório `input/` (ex.: `example_packet.json`).

3. Execute o programa:
```bash
python main.py
```

4. O arquivo convertido estará na pasta `output/` (compactado se configurado).

---

## Uso como Biblioteca

Você pode importar o conversor diretamente em outro projeto:

```python
from src.core.conversion_service import convert_payload_to
from src.core.mqtt_packet import MqttPacket

packet = MqttPacket.from_json('input/example_packet.json')
result = convert_payload_to(packet, 'csv')
print(result)
```

---


## Tecnologias

- Python 3
- Padrões de Projeto (Factory, Strategy, Facade, Singleton)
- Compressão (ZIP)
- Logging

---

## Licença

Este projeto é acadêmico, desenvolvido como parte da disciplina CSI-22 – Programação Orientada a Objetos do Instituto Tecnológico de Aeronáutica (ITA).

---

## Autores

- Brunno Rezende dos Santos
- Cícero Nunes da Silva Neto
- João Victor Zalkauskas Della Mônica Silva
- Matheus Bianchesi
- Thiago Frota Maranhão

---

## Documentação

- [Arquitetura]()
- [Usage](./mqtt_converter_project/docs/usage.md)
- [Diagrama de Classes](./docs/classdiagram.png)
- [Diagrama de Sequência](./docs/sequencediagram.png)

---

## Apresentação

- [Vídeo no YouTube](https://www.youtube.com/watch?v=aV79eHoicVI)
- [Slides de apresentação](https://csi22projeto.my.canva.site/dagqtzmdu8u)
- [Repositório no GitHub](https://github.com/JVZalk/FileConverter-CSI22)