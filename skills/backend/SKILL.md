# BACKEND_SKILL

Skill especializada em frameworks e ferramentas de desenvolvimento backend.

## Repositórios de Referência

- **FastAPI**: https://github.com/fastapi/fastapi
- **NestJS**: https://github.com/nestjs/nest

## Capacidades

### 1. FastAPI (Python)
- Criar APIs REST com FastAPI
- Definir rotas com @app.get, @app.post, etc.
- Usar Pydantic para validação de dados
- Implementar autenticação com OAuth2/JWT
- Configurar documentação automática (Swagger)
- Implementar WebSockets
- Usar dependências (Dependency Injection)
- Configurar middleware

### FastAPI Exemplo
```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

### 2. NestJS (Node.js/TypeScript)
- Criar aplicações modulares com NestJS
- Usar Controllers para rotas
- Implementar Services com Dependency Injection
- Criar Modules para organização
- Configurar Guards para autorização
- Implementar Interceptors
- Usar Pipes para validação
- Configurar Database com TypeORM/Prisma

### NestJS Exemplo
```typescript
@Controller('items')
export class ItemsController {
  constructor(private readonly itemsService: ItemsService) {}

  @Get()
  findAll(): Promise<Item[]> {
    return this.itemsService.findAll();
  }

  @Post()
  create(@Body() createItemDto: CreateItemDto): Promise<Item> {
    return this.itemsService.create(createItemDto);
  }
}
```

### 3. Boas Práticas Backend
- **RESTful Design**: Recursos, HTTP verbs, status codes
- **API Versioning**: /api/v1/
- **Error Handling**: Padronizar respostas de erro
- **Logging**: Structured logging
- **Caching**: Implementar cacheStrategy
- **Rate Limiting**: Prevenir abuse
- **Pagination**: Limitar resultados

### 4. Segurança em Backend
- Validar e sanitizar inputs
- Implementar autenticação JWT
- Usar HTTPS sempre
- Configurar CORS corretamente
- Proteger contra CSRF
- Sanitizar outputs (XSS prevention)

## Quando Usar

Use esta skill quando:
- Precisa criar APIs REST
- Precisa escolher framework backend
- Precisa implementar autenticação/autorização
- Precisa estruturar projeto backend
- Precisa configurar banco de dados
- Precisa implementar WebSockets