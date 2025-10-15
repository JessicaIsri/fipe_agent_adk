from google.adk.tools.openapi_tool import OpenAPIToolset

openapi_spec_string = """
openapi: 3.0.0
info:
  title: API da Tabela Fipe
  description: Uma API REST para consultar dados da Tabela Fipe.
  version: 1.0.0
servers:
  - url: https://parallelum.com.br/fipe/api/v1/
    description: Servidor da API v1
tags:
  - name: Marcas
    description: Endpoints para consultar marcas de veículos.
  - name: Modelos
    description: Endpoints para consultar modelos de veículos.
  - name: Anos
    description: Endpoints para consultar anos-modelo de veículos.
  - name: Valor
    description: Endpoint para consultar o valor de um veículo.
paths:
  /{tipo}/marcas:
    get:
      tags:
        - Marcas
      summary: Lista todas as marcas de veículos.
      parameters:
        - name: tipo
          in: path
          required: true
          description: O tipo de veículo (carros, motos ou caminhoes).
          schema:
            type: string
            enum: [carros, motos, caminhoes]
      responses:
        '200':
          description: Uma lista de marcas de veículos.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Marca'
  /{tipo}/marcas/{idMarca}/modelos:
    get:
      tags:
        - Modelos
      summary: Lista todos os modelos de uma marca.
      parameters:
        - name: tipo
          in: path
          required: true
          description: O tipo de veículo (carros, motos ou caminhoes).
          schema:
            type: string
            enum: [carros, motos, caminhoes]
        - name: idMarca
          in: path
          required: true
          description: O código da marca.
          schema:
            type: string
      responses:
        '200':
          description: Uma lista de modelos e anos.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelosAnos'
  /{tipo}/marcas/{idMarca}/modelos/{idModelo}/anos:
    get:
      tags:
        - Anos
      summary: Lista todos os anos de um modelo.
      parameters:
        - name: tipo
          in: path
          required: true
          description: O tipo de veículo (carros, motos ou caminhoes).
          schema:
            type: string
            enum: [carros, motos, caminhoes]
        - name: idMarca
          in: path
          required: true
          description: O código da marca.
          schema:
            type: string
        - name: idModelo
          in: path
          required: true
          description: O código do modelo.
          schema:
            type: string
      responses:
        '200':
          description: Uma lista de anos-modelo disponíveis para um veículo específico.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Ano'
  /{tipo}/marcas/{idMarca}/modelos/{idModelo}/anos/{idAno}:
    get:
      tags:
        - Valor
      summary: Consulta o valor de um veículo específico.
      parameters:
        - name: tipo
          in: path
          required: true
          description: O tipo de veículo (carros, motos ou caminhoes).
          schema:
            type: string
            enum: [carros, motos, caminhoes]
        - name: idMarca
          in: path
          required: true
          description: O código da marca.
          schema:
            type: string
        - name: idModelo
          in: path
          required: true
          description: O código do modelo.
          schema:
            type: string
        - name: idAno
          in: path
          required: true
          description: O código do ano.
          schema:
            type: string
      responses:
        '200':
          description: Os detalhes do valor do veículo.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Valor'

components:
  schemas:
    Marca:
      type: object
      properties:
        nome:
          type: string
          example: 'GM - Chevrolet'
        codigo:
          type: string
          example: '23'
    Modelo:
      type: object
      properties:
        nome:
          type: string
          example: 'AGILE LTZ 1.4 MPFI 8V FlexPower 5p'
        codigo:
          type: number
          example: 5980
    Ano:
      type: object
      properties:
        nome:
          type: string
          example: '1995 Gasolina'
        codigo:
          type: string
          example: '1995-1'
    ModelosAnos:
      type: object
      properties:
        modelos:
          type: array
          items:
            $ref: '#/components/schemas/Modelo'
        anos:
          type: array
          items:
            $ref: '#/components/schemas/Ano'
    Valor:
      type: object
      properties:
        Valor:
          type: string
          example: 'R$ 13.911,00'
        Marca:
          type: string
          example: 'GM - Chevrolet'
        Modelo:
          type: string
          example: 'AGILE LTZ 1.4 MPFI 8V FlexPower 5p'
        AnoModelo:
          type: number
          example: 2011
        Combustivel:
          type: string
          example: 'Gasolina'
        CodigoFipe:
          type: string
          example: '004399-5'
        MesReferencia:
          type: string
          example: 'dezembro de 2023'
        TipoVeiculo:
          type: number
          example: 1
        SiglaCombustivel:
          type: string
          example: 'G'
"""

fipe_toolset = OpenAPIToolset(
    spec_str=openapi_spec_string,
    spec_str_type='yaml',
)