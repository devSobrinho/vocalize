# Vocalize

Esta é uma REST API desenvolvida em Python que converte texto em áudio usando a biblioteca gTTS (Google Text-to-Speech). A API recebe texto via requisição e retorna o áudio correspondente em um stream. Este projeto foi criado com Flask e utiliza Marshmallow para validação de dados.

## Estrutura de Pastas

```
vocalize/
├── app/
│   ├── common/
│   │   ├── helpers/
│   │   │   ├── convert/
│   │   │   │   ├── audio_convert.py          # Funções para conversão de texto em áudio
│   │   │   │   └── __init__.py
│   │   │   ├── modules/
│   │   │   │   └── speech/
│   │   │   │       ├── schemas/
│   │   │   │       │   └── stream_audio_schema.py   # Schema para validação de dados usando Marshmallow
│   │   │   │       ├── speech_controller.py         # Controlador para gerenciar as requisições de áudio
│   │   │   │       ├── speech_service.py            # Serviço para a lógica de negócio de conversão de texto em áudio
│   │   │   │       ├── __init__.py
│   │   │   │       ├── server_setting.py            # Configurações do servidor Flask
│   │   │   │       └── util.py                      # Funções utilitárias
├── myenv/                                          # Ambiente virtual Python
├── main.py                                         # Ponto de entrada da aplicação
├── README.md                                       # Documentação do projeto
└── requirements.txt                                # Dependências do projeto
```

## Tecnologias Utilizadas

- **Python** - Linguagem principal do projeto.
- **Flask** - Framework para construção de APIs.
- **Marshmallow** - Biblioteca para serialização e validação de dados.
- **gTTS** - Google Text-to-Speech para conversão de texto em áudio.

## Endpoints

### `POST /api/speech/stream`

Recebe um texto via JSON e retorna o áudio correspondente em um stream.

#### Exemplo de Requisição

```http
POST /api/speech/stream
Content-Type: application/json

{
  "text": "Olá, bem-vindo ao conversor de texto para áudio!"
}
```

#### Exemplo de Resposta

- **Status Code**: 200 OK
- **Corpo**: Stream de áudio gerado a partir do texto fornecido.

### Estrutura de Dados

O endpoint `/api/speech/stream` utiliza o seguinte schema para validação dos dados de entrada:

```json
{
  "text": "string",
  "language": "string"
}
```

### Validações

- `text` (obrigatório): O texto a ser convertido para áudio.
- `language` (opcional): A linguagem do texto, sendo por padrão pt-br

## Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd vocalize
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # No Windows: myenv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Executando a Aplicação

1. No terminal, execute o arquivo principal:

   ```bash
   python main.py
   ```

2. A aplicação estará disponível em `http://localhost:5000`.

## Estrutura de Arquivos

- **`main.py`**: Ponto de entrada para iniciar a aplicação Flask.
- **`app/common/helpers/convert/audio_convert.py`**: Funções para converter o texto em áudio usando a biblioteca gTTS.
- **`app/common/modules/speech/schemas/stream_audio_schema.py`**: Define o schema para validação do texto de entrada.
- **`app/common/modules/speech/speech_controller.py`**: Controlador para gerenciar as requisições e chamadas do serviço de áudio.
- **`app/common/modules/speech/speech_service.py`**: Contém a lógica de negócio para a conversão de texto para áudio.
- **`app/common/modules/speech/server_setting.py`**: Configurações do servidor Flask.

## Dependências

- **Flask**
- **Marshmallow**
- **gTTS**

Essas dependências estão listadas no arquivo `requirements.txt` e podem ser instaladas com o comando:

```bash
pip install -r requirements.txt
```
