# Extrator de dados do CNPJ

## 📖 Descrição
Este projeto foi desenvolvido para automatizar o processo de extração de informações de CNPJs de um site específico e armazenar os dados em uma planilha. O objetivo é facilitar o acesso e a análise de informações cadastrais de empresas de maneira eficiente.

---

## 💻 Tecnologias
- **Python**: Versao 3.12.3 

## Bibliotecas
- **Pandas**: Versão 2.2.3
- **Beautifulsoup4**: Versão 4.12.3 
- **Requests**: Versão 2.32.3

---

## ✨ Funcionalidades
- **Leitura** de dados: Lê os CNPJs de uma planilha de entrada (`inputs.xlsx`).
- **Extração** de dados: Efetua uma requisição ao um site de consulta de cnpj e obtém informações como Razão Social, Porte, Capital, Situação Cadastral, Telefone, Email e Endereço.
- **Exportação** dados: Salva os dados coletados em uma planilha de saída (`outputs.xlsx`).

---

## 📂 Configuração dos Arquivos
- Planilha de Entrada (inputs.xlsx)
- Certifique-se de criar ou editar uma planilha chamada inputs.xlsx.
- A planilha deve conter os CNPJs na primeira coluna, com o cabeçalho CNPJ.

### Configuração Opcional
Ao iniciar o sistema, você poderá selecionar arquivos de entrada e saída fora da pasta padrão. Caso contrário, serão utilizados os caminhos padrão na raiz do projeto.

---

## 🚀 Como Executar
Executável (Windows e Linux)
Para executar o programa de maneira simples:

Navegue até a pasta dist.
Execute o arquivo principal:
- **Windows**: Dê dois cliques no executável.

- **Linux**: Use o comando:
```bash
dist/main
```

---

## 🛠 Instalação Dev (Essa sessão é necessária apenas para os devs)

### ✅ Requisitos
1. **Python**: Certifique-se de que o Python está instalado no seu sistema. https://www.python.org/downloads/
2. **Git**: Instale o Git para clonar o repositório. https://git-scm.com/downloads

### 🔄 Clonar o Repositório
Abra seu terminal (Bash, PowerShell ou CMD) e execute o seguinte comando:
```bash
git clone https://github.com/juniorferreira23/CNPJ_Data_Extractor.git
```

### 🌐 Criando ambiente vitual
```bash
python3 -m venv venv
```

### Ativar ambiente virtual
Windows
```cmd
.\venv\Scripts\activate.ps1
```

Linux
```bash
Source venv/bin/activate
```

### 📦 Instalação de dependências
No ambiente virtual, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### ▶️  Executando o Código
Para rodar o programa diretamente, utilize:
```bash
python3 main.py
```
Ou para o uso com interface
```bash
python3 interface.py
```
