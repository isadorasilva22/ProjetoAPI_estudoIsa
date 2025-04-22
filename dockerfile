# Define instruções para criar uma imagem Docker da aplicação, permitindo:
# Empacotar a aplicação com todas as suas dependências
# Facilitar o deploy em diferentes ambientes

FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8001

CMD ["python", "app.py"]
