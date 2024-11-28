# Data Lake Application

## Descrição

Este projeto foi desenvolvido como parte de um desafio para uma rede de restaurantes. Nele, criei uma aplicação em Flask que permite a manipulação, verificação, busca e pesquisa de dados armazenados em um data lake. Os dados são armazenados em arquivos JSON organizados por tipo de dado, ano, mês e loja.

Por que armazenar as respostas das APIs? 
Armazenar as respostas das APIs tem várias vantagens, especialmente em um contexto onde o desempenho, a integridade dos dados e a eficiência operacional são cruciais.

Considere que a resposta do endpoint getGuestChecks foi alterada, por exemplo, guestChecks.taxes foi renomeado para guestChecks.taxation. O que isso implicaria?
Implicações da Alteração  - Compatibilidade de Dados
 - Manutenção de Código
 - Integração de Sistemas
 - Documentação e Comunicação
 - Versionamento de API


## Estrutura de Pastas

A estrutura de pastas do projeto é organizada da seguinte forma:

## Instalação Siga os passos abaixo para configurar e executar a aplicação:
1. **Clone o repositório**:

2. **Crie um ambiente virtual**: ```sh python3 -m venv .venv source .venv/bin/activate ```

3. **Instale as dependências**: ```sh pip install -r requirements.txt ```

4. **Estrutura de Pastas e Arquivos JSON**:
   - Certifique-se de que a estrutura de pastas e os arquivos JSON estão corretos conforme descrito anteriormente.

## Uso

1. **Execute a aplicação Flask**:
    ```sh
    python app.py
    ```

2. **Acesse a aplicação no navegador**:
    - Abra o navegador e vá para `http://127.0.0.1:5000/`

3. **Use o formulário para buscar dados**:
    - Selecione o tipo de dados, insira a data de operação: = 2024/01/01 e o ID da loja = 1, e clique em "Buscar".

## Funções Principais

### Carregar Dados JSON
Carrega dados de um arquivo JSON dado um caminho específico.

### Processar `Guest Checks`
Processa dados do tipo `guest_checks`, focando no campo `taxation`.

]

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para obter mais informações.

Explicação das Seções
1. Descrição: Uma breve descrição do projeto e sua finalidade. 
2. Estrutura de Pastas: A estrutura de pastas do projeto para facilitar a navegação. 
3. Instalação: Instruções para clonar o repositório, criar um ambiente virtual e instalar as dependências. 
4. Uso: Como executar a aplicação e utilizá-la. 
5. Funções Principais: Descrição das principais funções do código. 
6. Contribuição: Informações sobre como contribuir com o projeto. 
7. Licença: Tipo de licença do projeto. 
Sinta-se à vontade para ajustar e adicionar mais informações conforme necessário. 
