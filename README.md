# 📦 Sistema de Gerenciamento de Aluguel de Jogos de Tabuleiro

Este projeto implementa uma aplicação simples para gerenciar **aluguel de jogos de tabuleiro** e **envio de e-mails**, utilizando Python. Ele foi estruturado de forma modular para facilitar manutenção, testes e expansão.

---

## 📁 Estrutura de Pastas

```
project/
├── main.py                # Arquivo principal da aplicação
├── database/
│   └── db.py              # Conexão e operações com o banco de dados
├── models/
│   ├── RentData.py        # Classe de dados para aluguel
│   └── BoardGameData.py   # Classe de dados para jogos
├── services/
│   └── email_service.py   # Serviço para envio de e-mails
├── .env                   # Variáveis de ambiente
└── README.md              # Documentação
```

---

## 🧩 Funcionalidades

### ✔️ **Cadastro de Jogos de Tabuleiro**
- Nome do jogo
- Custo
- Número de jogadores

### ✔️ **Cadastro de Aluguéis**
- Data do aluguel
- Valor total
- Cliente

### ✔️ **Envio de E-mails**
O sistema envia e-mails usando Gmail via SMTP.

---

## ⚙️ Configuração

### 1️⃣ Instalar dependências
```bash
pip install python-dotenv
```

### 2️⃣ Criar arquivo `.env`
```env
DATABASE_NAME=exampledatabase.db
EMAIL=exampleemail@gmail.com
EMAIL_PASSWORD=examplepassword123
```
> **Importante:** para Gmail, pode ser necessário gerar uma senha de app.

---

## ✉️ Serviço de E-mail

```python
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL")
    msg['To'] = to

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)

    return True
```

---

## 🗄️ Modelos de Dados

### **RentData**
```python
class RentData:
    def __init__(self, date, totalCost, client):
        self.date = date
        self.totalCost = totalCost
        self.client = client
```

### **BoardGameData**
```python
class BoardGameData:
    def __init__(self, boardGameName, cost, playerCount):
        self.boardGameName = boardGameName
        self.cost = cost
        self.playerCount = playerCount
```

---

## 🚀 Como Executar

```bash
python main.py
```

---

## 📝 Licença
Este projeto é livre para uso e modificação.

---

Se quiser, posso **personalizar o README**, adicionar imagens, badges, instruções mais detalhadas ou exemplos de uso!

