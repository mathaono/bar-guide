#Imagem oficiao do Python
FROM python:3.11-slim

#Define diretório de trabalho dentro do container
WORKDIR /app

#Copia requirements.txt e instala as dependências
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

#Copia o restante do código backend
COPY . .

ENV PYTHONPATH=/app

#Expõe a porta padrão do unicorv
EXPOSE 8000

#Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]