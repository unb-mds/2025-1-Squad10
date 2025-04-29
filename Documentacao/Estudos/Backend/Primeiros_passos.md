# Instalando Python3 e pip

Primeiro, atualize a lista de pacotes com o comando: `sudo apt update`
Após a atualização, instale o Python com o comando: `sudo apt install python3`
Em seguida, instale o pip com o comando: `sudo apt install python3-pip`
# Preparando ambiente virtual

Primeiro, instale o módulo venv: `sudo apt install python3-venv`

Em seguida, crie um novo ambiente virtual com o seguinte comando: `python3 -m venv </local-do-novo-ambiente-virtual>`
Exemplo: `python3 -m venv ./python_mds`

**Para ativar ambiente virtual**, utilize o comando: `source ./local-do-novo-ambiente-virtual/bin/activate`
Exemplo: `source ./python_mds/bin/activate`

Quando ativo, o terminal mostrará o nome da pasta do ambiente virtual
<img src="./assets/printscreens/Pasted image 20250423122043.png">

**Para desativar o ambiente virtual**, utilize o comando: `deactivate`

Lembre-se de que toda vez que for trabalhar com o código do projeto, você deverá ativar o ambiente virtual específico.
# Instalando Streamlit e o Ipeadatapy

Com o ambiente virtual ativado, instale o Streamlit com o seguinte comando:
`pip install streamlit`

Para verificar se o Streamlit está funcionando, utilize o comando: `streamlit hello`

<img src="./assets/printscreens/Pasted image 20250423122500.png">
Utilize <kbd>Ctrl</kbd> + <kbd>C</kbd> para finalizar a execução do servidor local.

Instale o ipeadatapy com o comando:
`pip install ipeadatapy`