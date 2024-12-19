from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()

# Armazenamento em memória para itens do carrinho
itens_carrinho = []

@app.get("/carrinho")
async def listar_itens_carrinho():
   
    #Recuperar a lista de itens no carrinho.
   
    return {
        "status": "sucesso",
        "mensagem": "Itens do carrinho recuperados com sucesso.",
        "dados": itens_carrinho
    }

@app.get("/carrinho/{item_id}")
async def obter_item_carrinho_por_id(item_id: int):
   
    #Recuperar um item do carrinho pelo ID.
   
    for item in itens_carrinho:
        if item["id"] == item_id:
            return {
                "status": "sucesso",
                "mensagem": "Item do carrinho recuperado com sucesso.",
                "dados": item
            }
    raise HTTPException(status_code=404, detail="Item não encontrado no carrinho.")


@app.post("/carrinho")
async def adicionar_item_carrinho(
    nome: str = Form(...),
    quantidade: int = Form(...),
    preco: float = Form(...)
):
    
    #Adicionar um novo item ao carrinho.
    
    item = {
        "id": len(itens_carrinho) + 1,  # Gerar um ID simples
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    itens_carrinho.append(item)
    return {
        "status": "sucesso",
        "mensagem": "Item adicionado ao carrinho com sucesso.",
        "dados": item
    }

@app.put("/carrinho/{item_id}")
async def atualizar_item_carrinho(
    item_id: int,
    nome: str = Form(...),
    quantidade: int = Form(...),
    preco: float = Form(...)
):
    
    #Atualizar os detalhes de um item do carrinho pelo ID.
    
    for item in itens_carrinho:
        if item["id"] == item_id:
            item.update({"nome": nome, "quantidade": quantidade, "preco": preco})
            return {
                "status": "sucesso",
                "mensagem": "Item do carrinho atualizado com sucesso.",
                "dados": item
            }
    raise HTTPException(status_code=404, detail="Item não encontrado no carrinho.")

@app.delete("/carrinho/{item_id}")
async def deletar_item_carrinho(item_id: int):
    
    #Remover um item do carrinho pelo ID.
    
    for indice, item in enumerate(itens_carrinho):
        if item["id"] == item_id:
            item_deletado = itens_carrinho.pop(indice)
            return {
                "status": "sucesso",
                "mensagem": "Item do carrinho removido com sucesso.",
                "dados": item_deletado
            }
    raise HTTPException(status_code=404, detail="Item não encontrado no carrinho.")
