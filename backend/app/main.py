from fastapi import FastAPI
from app.database import engine, Base
from app.routers import resume

# Inicializar o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir as rotas
app.include_router(resume.router)

@app.get("/")
def read_root():
    return {"message": "Vitae.ai está funcionando!"}
