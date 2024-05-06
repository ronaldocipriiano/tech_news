# Tech News

Este projeto consiste em um sistema de busca de notícias sobre tecnologia, utilizando raspagem de dados do blog da Trybe (https://blog.betrybe.com/) e armazenamento das notícias em um banco de dados MongoDB. O sistema é acompanhado por uma interface de linha de comando (CLI) que permite ao usuário realizar consultas e atualizar o banco de notícias.

## Instalação e Uso

1. Clone o repositório:

    ```
    git clone git@github.com:ronaldocipriiano/tech_news.git
    cd tech_news
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

4. Inicie o servidor MongoDB:

    ```
    docker-compose up -d mongodb
    ```

5. Execute a CLI para buscar notícias:

    ```
    tech-news-analyzer
    ```

## Funcionalidades Implementadas

### 1. Função fetch

A função `fetch` em `tech_news/scraper.py` realiza a requisição HTTP ao site da Trybe para obter o conteúdo HTML das páginas.

### 2. Função scrape_updates

A função `scrape_updates` em `tech_news/scraper.py` extrai as URLs das páginas de notícias do conteúdo HTML da página inicial do blog da Trybe.

### 3. Função scrape_next_page_link

A função `scrape_next_page_link` em `tech_news/scraper.py` obtém o link da próxima página de notícias para permitir a paginação.

### 4. Função scrape_news

A função `scrape_news` em `tech_news/scraper.py` faz o scrape dos dados de uma única notícia, preenchendo um dicionário com informações como URL, título, data, autor, tempo de leitura, resumo e categoria.

### 5. Função get_tech_news

A função `get_tech_news` em `tech_news/scraper.py` busca as últimas n notícias do site, armazena-as no MongoDB e retorna essas notícias.

### 6. Teste da classe ReadingPlanService

O teste `test_reading_plan_group_news` em `tests/reading_plan/test_reading_plan.py` verifica o método `group_news_for_available_time` da classe `ReadingPlanService`, garantindo que as notícias sejam agrupadas corretamente para o tempo disponível de leitura.

### 7. Função search_by_title

A função `search_by_title` em `tech_news/analyzer/search_engine.py` busca notícias por título no banco de dados e retorna uma lista de tuplas com os títulos e URLs das notícias encontradas.

### 8. Função search_by_date

A função `search_by_date` em `tech_news/analyzer/search_engine.py` busca notícias por data no banco de dados e retorna uma lista de tuplas com os títulos e URLs das notícias encontradas.

### 9. Função search_by_category

A função `search_by_category` em `tech_news/analyzer/search_engine.py` busca notícias por categoria no banco de dados e retorna uma lista de tuplas com os títulos e URLs das notícias encontradas.

### 10. Função top_5_categories (Requisito Bônus)

A função `top_5_categories` em `tech_news/analyzer/ratings.py` lista as cinco categorias mais populares com base no número de ocorrências no banco de dados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues com sugestões de melhorias.
