# 🛒 Carrinho de Compras API

Bem-vindo à API do Carrinho de Compras! Esta API permite gerenciar itens em um carrinho de compras com operações CRUD (Criar, Ler, Atualizar, Deletar).

## 🚀 Como Executar

1. **Clone o repositório:**
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd carrinhoCompras
    ```

2. **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Execute a aplicação:**
    ```sh
    uvicorn main:app --reload
    ```

## 📋 Endpoints

### 📜 Listar Itens do Carrinho

- **URL:** `/carrinho`
- **Método:** `GET`
- **Descrição:** Recupera a lista de itens no carrinho.
- **Resposta de Sucesso:**
    ```json
    {
        "status": "sucesso",
        "mensagem": "Itens do carrinho recuperados com sucesso.",
        "dados": [...]
    }
    ```

### 🔍 Obter Item por ID

- **URL:** `/carrinho/{item_id}`
- **Método:** `GET`
- **Descrição:** Recupera um item do carrinho pelo ID.
- **Resposta de Sucesso:**
    ```json
    {
        "status": "sucesso",
        "mensagem": "Item do carrinho recuperado com sucesso.",
        "dados": {...}
    }
    ```
- **Resposta de Erro:**
    ```json
    {
        "detail": "Item não encontrado no carrinho."
    }
    ```

### ➕ Adicionar Item ao Carrinho

- **URL:** `/carrinho`
- **Método:** `POST`
- **Descrição:** Adiciona um novo item ao carrinho.
- **Parâmetros:**
    - `nome`: Nome do item (formulário)
    - `quantidade`: Quantidade do item (formulário)
    - `preco`: Preço do item (formulário)
- **Resposta de Sucesso:**
    ```json
    {
        "status": "sucesso",
        "mensagem": "Item adicionado ao carrinho com sucesso.",
        "dados": {...}
    }
    ```

### ✏️ Atualizar Item do Carrinho

- **URL:** `/carrinho/{item_id}`
- **Método:** `PUT`
- **Descrição:** Atualiza os detalhes de um item do carrinho pelo ID.
- **Parâmetros:**
    - `nome`: Nome do item (formulário)
    - `quantidade`: Quantidade do item (formulário)
    - `preco`: Preço do item (formulário)
- **Resposta de Sucesso:**
    ```json
    {
        "status": "sucesso",
        "mensagem": "Item do carrinho atualizado com sucesso.",
        "dados": {...}
    }
    ```
- **Resposta de Erro:**
    ```json
    {
        "detail": "Item não encontrado no carrinho."
    }
    ```

### 🗑️ Deletar Item do Carrinho

- **URL:** `/carrinho/{item_id}`
- **Método:** `DELETE`
- **Descrição:** Remove um item do carrinho pelo ID.
- **Resposta de Sucesso:**
    ```json
    {
        "status": "sucesso",
        "mensagem": "Item do carrinho removido com sucesso.",
        "dados": {...}
    }
    ```
- **Resposta de Erro:**
    ```json
    {
        "detail": "Item não encontrado no carrinho."
    }
    ```
## 📄 Documentação no Postman

Para mais detalhes sobre como utilizar a API, acesse a [documentação do Postman](https://encurtador.com.br/SDVok).
## 🛠 Tecnologias Utilizadas

- **FastAPI** - Framework para construção de APIs.
- **Uvicorn** - Servidor ASGI para execução da aplicação.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ❤️ por Gabriely Morais