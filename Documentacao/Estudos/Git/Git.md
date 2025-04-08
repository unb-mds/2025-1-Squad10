#**Git**


Git é um software de versionamento (***VCS - Version Control System***) utilizado para relizar o controle das versões de um software com o decorrer de implementações no mesmo. É o software responsável por gerenciar todas as alterações e estados realizados no código fonte no repositório local (dispositivo do desenvolvedor).


No mundo de desenvolvimento de software, existem dois tipos de versionamento:


***Versionamento Centralizado/Linear***


   - Os commits são enviados diretamente para um repositório central. É mantida uma conexão direta com o servidor.


***Versionamento Distribuido***


   - Os commits são enviados para um repositório local, e posteriormente para um repositório remoto.


Onde o Git faz parte do conjunto de VCS's do formato distribuído.


##**Vantagens de utilizar Git:**


- Controle de histórico;
- Trabalho em equipe;
- Ramificações do projeto;
- Segurança;
- Organização.


#***GitHub***


GitHub é uma plataforma social para programadores onde é possível armazenar diretórios contendo códigos-fonte. Exerce o papel de repositório remoto, ou seja, todas as atualizações a respeito da aplicação serão implementadas através deste repositório.


##***Vantagens de utilizar o GitHub:***


- Repositórios ilimitados;
- Hospedagem de código fonte;
- Colaboração com/de terceiros;
- GitHub Desktop, que traz uma interface amigável para manipular Git.


#**Dicionário Git/GitHub**


***Repositório Local***


   - Armazena a cópia do projeto existente no repositório remoto no dispositivo do usuário.


***Repositório Remoto***


   - Armazena a cópia de um repositório que está hospedado na internet ou em uma rede de conexão (software em funcionamento) e pode receber implementações provenientes dos repositórios locais a este associado.


***Commit***


   - Envia as mudanças realizadas no código-fonte para o repositório local.


***Push***


   - Envia mudanças para o repositório remoto.


***Pull***


   - Recebe mudanças do repositório remoto para o repositório local.


***Branch***


   - Ramificação do projeto em um certo ponto.


***Clone***


   - Clona um repositório remoto ja existente.


***Merge***


   - Junção de implementações, normalmente associadas a branches.


#**Instalação**


Vale ressaltar que o projeto que será desenvolvido em dispositivos que contém o sistema operacional Linux Mint e que utilizaremos como padrão a IDE Visual Studio Code.


##**Instalalçao do Git**


No terminal utilizamos o seguinte comando para realizar a instalação do Git: "sudo apt-get install git"


##**Instalação do GitHub Desktop**


Para instalar o GitHub Desktop em uma distribuição Linux entre no seguinte repositório: [Repositório Shitfkey](https://github.com/shiftkey/desktop/releases)


Cheque no terminal com o comando ***lscpu*** o modelo de arquitetura de seu dispositivo, na linha ***arquitetura***, onde caso ***x86_64 = amd64***, ou caso ***aarch64 = arm64***.


Procure pela última versão ***tipo_de_arquitetura***.deb e baixe o arquivo, após isso, abra o terminal e navegue até o diretório onde está contido o download e execute o comando: "sudo dpkg -i ***nome_arquivo***.deb"


Após a instalação do GitHub Desktop, logue no aplicativo com sua conta GitHub e realize a clonagem do repositório remoto referente ao projeto da seguinte maneira: ***File -> Clone Repository -> URL***, cole a URL do repositório do projeto e escolha um diretório para o mesmo.


Com a conclusão de todas as etapas, a clonagem do repositório do projeto estará pronta e será possível contribuir diretamente com a construção do software a ser desenvolvido.


Vale ressaltar que para cada implementação a ser realizada no projeto, evite utilizar a ***branch main*** para realizar a colaboração afim de evitar conflitos com os outros integrantes. Para cada nova implementação crie uma issue e uma branch nova associada, e por fim abra um ***pull request*** para que seja feito um ***merge*** no repositório remoto.



