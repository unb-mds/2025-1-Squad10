# 🤝 Como contribuir

## Instalando Python 3
### No Windows

- Baixe e instale o [Python 3]([Download Python | Python.org](https://www.python.org/getit/)).
### No Linux

- No Linux, é necessário instalar os pacotes de desenvolvimento do Python. Utilize o seguinte comando:
```
sudo apt install python3-dev python3-pip python3-venv
```
## Clonando repositório

- Clone o repositório utilizando o comando:

```
git clone https://github.com/unb-mds/2025-1-Squad10.git
```

## Criando e ativando um ambiente virtual do Python

- Vá a pasta do repositório

```
cd 2025-1-Squad10
```

-  Crie um ambiente virtual do Python

```
python -m venv venv
```

-  Ative o ambiente virtual

#### No Windows

```
venv\Scripts\activate.bat
```

#### No Linux

```
source ./venv/bin/activate
```
## Instalando pré-requisitos

- Atualize a versão do pip
```
# No Windows
python -m pip install -U pip
# No Linux
python3 -m pip install --upgrade pip
```

- Instale as dependências do projeto com o comando:
```
 pip install -r requirements.txt 
```
