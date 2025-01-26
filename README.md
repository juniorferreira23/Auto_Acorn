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
- **Salva** dados: Após a extração os dados são formatados e salvos em uma planilha de saída (`outputs.xlsx`).

---

## Inputs
Para informar quais CNPJ's serão consultados, basta adicionar na planilha inputs.xlsx os CNPJ's na primeira coluna com o cabeçalho CNPJ. 

Ao abrir a janela do sistema, é opcional o preenchimento do caminho da planilha input e output, caso não preencha será considerado a raiz da pasta, ou podera selecionar a planilha de input fora da pasta e onde deve ser salvo.

---

## Rode de maneira simples
Dentro da pasta dist terá um executavel para executar no windows basta das dois clicks e no linux use o comando abaixo na raiz do projeto:
```bash
dist/main
```

## 🛠 Instalação Dev (Essa sessão é necessária apenas para os devs)

### ✅ Requisitos
1. **Python**: Certifique-se de que o Python está instalado no seu sistema. https://www.python.org/downloads/
2. **Git**: Instale o Git para clonar o repositório. https://git-scm.com/downloads

### 🔄 Clonar o Repositório
Abra seu terminal (Bash, PowerShell ou CMD) e execute o seguinte comando:
```bash
git clone https://github.com/juniorferreira23/CNPJ_Data_Extractor.git
```

### Inicialização de ambiente vitual
```bash
python3 -m venv venv
```

### Acessar ambiente virtual
Windows
```cmd
.\venv\Scripts\activate.ps1
```

Linux
```bash
Source venv/bin/activate
```

### Instalação de dependências
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python3 main.py
```
