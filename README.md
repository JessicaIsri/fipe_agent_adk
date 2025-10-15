# Consultor FIPE: Agente de Consulta de Valor de Veículos

Este agente utiliza o Google Agent Development Kit (ADK) para interagir com a API da Tabela Fipe, permitindo consultar o valor de mercado de carros, motos e caminhões.

O fluxo de consulta é guiado e sequencial, solicitando as informações necessárias (tipo, marca, modelo e ano) passo a passo.

## Pré-requisitos

Para executar este agente, você precisa ter o Python instalado (versão 3.8+) e uma chave de API do Google Gemini.

## Instalação

1.  **Crie um Ambiente Virtual** (Recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

2.  **Instale as Dependências:**

    O agente utiliza o Google ADK para seu funcionamento.

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

O agente requer que você configure a chave de acesso à API do Google Gemini.

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variaveis:

```bash
# Define o uso da API padrão (não Vertex AI)
GOOGLE_GENAI_USE_VERTEXAI=FALSE
# Substitua pela sua chave de API
GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
```

## Como Obter uma Chave de API do Google Gemini

1. **Acesse o Google AI Studio:**
  Abra seu navegador e vá para o Google AI Studio (anteriormente conhecido como Google AI for Developers):
   
 https://aistudio.google.com/app/api-keys 

2. **Faça Login:**
  Se você ainda não estiver logado, clique em "Sign In" (Fazer Login) e use sua conta do Google.

3. **Crie a Chave de API:**
  *  Após fazer login, você será direcionado para a página de gerenciamento de chaves de API.
  *  Clique no botão **"+ Create API key"** (Criar chave de API).
  *  Uma nova chave de API será gerada instantaneamente e exibida na tela.

## Execução do Agente

Para interagir com o agente, você pode utilizar a interface web integrada do ADK.

1.  **Execute a interface web do ADK:**

    ```bash
    cd fipe_agent
    adk web 
    ```

2.  Acesse a URL exibida no console (geralmente `http://localhost:8000`) em seu navegador.

## Fluxo de Interação

O agente guiará você através das etapas necessárias para obter o valor FIPE. Certifique-se de fornecer o tipo de veículo no primeiro prompt.

**Tipos de Veículo Aceitos:**
*   `carro` (mapeia para `carros`)
*   `moto` (mapeia para `motos`)
*   `caminhao` (mapeia para `caminhoes`)

O fluxo esperado de perguntas é:

1.  **Tipo de Veículo:** (e.g., `carro`)
2.  **Marca:** O agente listará as marcas ou pedirá para você informar o código da marca.
3.  **Modelo:** O agente listará os modelos disponíveis para a marca escolhida ou pedirá o código.
4.  **Ano/Combustível:** O agente listará as combinações ano-modelo e pedirá o código.
5.  **Resultado:** O valor FIPE final.

## Exemplo de Solicitação

Aqui está um exemplo de como a conversa com o agente deve fluir:

### Passo 1: Iniciar a Consulta

**Usuário:**
> Quero consultar o valor de uma moto.

*(O Agente Orquestrador ativará o `consulta_marcas` para listar as marcas de motos.)*

### Passo 2: Seleção da Marca

**Agente:**
> Por favor, escolha a marca da moto fornecendo o código correspondente.
>
> [Lista de Marcas]
> 1: Honda
> 2: Yamaha
> ...

**Usuário:**
> 67 (Supondo que 67 seja o código da marca desejada)

### Passo 3: Seleção do Modelo

*(O Agente Orquestrador ativará o `consulta_modelos` usando o tipo 'motos' e o código da marca.)*

**Agente:**
> Agora, escolha o modelo da moto:
>
> [Lista de Modelos]
> 500: CB 500F
> 501: XRE 300
> ...

**Usuário:**
> 501

### Passo 4: Seleção do Ano

*(O Agente Orquestrador ativará o `consulta_anos` usando o tipo, marca e modelo.)*

**Agente:**
> Por fim, escolha o ano-modelo:
>
> [Lista de Anos]
> 2023-1: 2023 Gasolina
> 2024-1: 2024 Gasolina

**Usuário:**
> 2024-1

### Passo 5: Resultado Final

*(O Agente Orquestrador ativará o `consulta_fipe` e fornecerá todos os parâmetros (tipo, idMarca, idModelo, idAno).)*

**Agente:**
> O valor FIPE para a **Honda XRE 300 (2024 Gasolina)**, conforme o mês de referência de [Mês/Ano], é de **R$ 25.000,00**.
