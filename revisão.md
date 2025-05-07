# Revisão

## 🚢 Navegando entre diretórios
- Diretório abaixo: `./`
- Diretório acima: `../`

## 🔤 Primeiros passos com HTML
- Estrutura básica do HTML: `! + tab`
- Vincular um css externo: 
    - dentro do `head` insira `<link rel="stylesheet" href="../css/style.css">` 
    - ou digite `link + tab`

## 🎨 CSS
A estilização pode ser feita de forma externa, interna ou inline em relação ao html.

### CSS externo
CSS externos são definidos pela tag `<link>` dentro do `head` do HTML. 
Exemplo de arquivo .css:
```
body {
  background-color: lightblue;
}

h1 {
  color: navy;
  margin-left: 20px;
}
```
### CSS interno
CSS internos são desenvolvidos dentro do código html, representados pela tag `<style>`.
Exemplo de css interno:
```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  margin-left: 40px;
}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

```
### CSS inline
CSS inline é utilizado para aplicar um estilo a um único elemento.
Exemplo de css inline:
```
<!DOCTYPE html>
<html>
<body>

<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>

</body>
</html>
```
## Flexbox x Grid
TODO: explicar quando usar cada um e atributos de cada

### Flexbox

### Grid
No arquivo .css use `display: grid` para atribuir ao elemento e aos seus filhos essa configuração.
Opções para criar número de colunas:
- `grid-template-columns: auto auto auto`: cria três colunas de tamanhos iguais;
- `grid-template-columns: 1fr 2fr 1fr`: cria três colunas, sendo a segunda 2x maior do que as primeira e terceira;
- `grid-template-columns: 20% auto auto`: cria três colunas, com a primeira fixada em 20% e as demais ajustam automaticamente a área disponível;
- `grid-column: 1/3`: elemento inicia na linha 1 de coluna e termina na linha 3 de coluna
- `grid-column: 1/span 2`: elemento inicia na linha um e termina em mais duas linhas

Para linhas a lógica é a mesma, só altere o comando de `column` para `row`;

### Exemplo desenvolvido
![alt text](image.png)

## Usando o Flask
Abra o terminal `(ctrl + ")`
Crie a estrutura de organização padrão do Flask.
``` 
|-- static
|   |-- style.css
|
|-- templates
|   |--index.html
|
|-- app.py
```
### app.py
```
from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")
```

### Instalação do Flask
1. Verifique se tem o python instalado: `python --version`
2. Crie um ambiente virtual: `python -m venv venv`
📢 A pasta venv não deve ser subida no repositório. Para isso, adicione ao .gitignore.
3. Ative o ambiente virtual: `.\venv\Scripts\activate`
📢 Caso o SO não execute o script por questões de segurança, entre no powershell no modo administrador e altere a política de segurança do SO.
4. Para desativar o ambiente virtual: `deactivate`
5. Com o ambiente virtual ativado, instale a biblioteca do Flask: `pip install flask`
6. Uma vez instalado é possível ver os itens com `pip freeze`
7. Gere um arquivo .txt com os requisitos para o funcionamento do projeto: `pip freeze > requirements.txt`
8. Caso você esteja usando um projeto que já possui o arquivo requirements.txt faça a instalação no ambiente virtual ativado com: `pip install -r .\requirements.txt`

## AWS
📢 Acesse a conta de estudante pelo link do e-mail.

### Serviço de computação EC2
 É um serviço de computação em nuvem que permite aos usuários alugarem computadores virtuais (instâncias) para rodar seus próprios aplicativos. 

 #### Executando uma nova instância
 1. Dê um nome a instância;
 2. Selecione a imagem e SO;
 3. Selecione o tipo de instância. 1GB é suficiente para rodar o Flask;
 4. A comunicação entre a sua máquina e a AWS é feita via terminal (cli) através do protocolo SSH (Secure Shell) que usa por padrão a porta 22/TCP. Então crie um par de chaves para conectar-se a instância;
 5. Em configurações de rede selecione todas as checkboxs.
 6. Configure o armazenamento para no mínimo 25GB. A versão gratuita permite até 30GB;
 7. Execute a instância.

 #### Conecte à instância
1.  No Windows Powershell navegue até o diretório que contém o arquivo .pem.
2. No navegador, clique na instância desejada, copie o comando na aba 'Cliente SSH' e cole no powershell com o botão direito. Depois digite `yes` para permitir.
3. Caso de erro, baixe o `Bitvise SSH Client` (Solução para Windows).
 - Após a instalação, copie o `Endereço IPv4 público` da instância e cole no campo `Host`.
 - Port: 22
 - Username: ubuntu
 - Initial method: publickey
 - Selecione ´Cliente key manager` > import > selecione o arquivo .pem e importe a chave.
 Clique em Log in para iniciar, aceita e salva.

 ## Criando um projeto com Flask na instância da AWS
No Powershell, conecte-se a instância.
- `pwd`: exibe o caminho do diretório atual
- `git clone <link-do-repositorio>`: clona o repositório do projeto
- `cd <nome-da-pasta>`: navega para a pasta do projeto
- `sudo su`: altera para usuário root identificado pela `#` (administrador)
- `exit`: sai do modo usuário root
- `sudo apt update`: atualiza os pacotes
- `python3 --version`: verifica versão do Python
- `python3 -m venv venv`: cria a máquina virtual
- `sudo apt install python3.12-venv`: instala pacote para criação da venv
- `history`: exibe o histórico de comandos
- `!<número-da-linha>`: executa novamente o comando
- `mkdir <nome-da-pasta>`: cria uma nova pasta
- `ls`: exibe os itens do diretório
- `touch <nome-do-arquivo>`: cria novo arquivo (pode ser combinado para ser criado já dentro do repositório desejado ex.: touch templates/index.html cria um arquivo .html dentro da pasta templates)
- `source venv/bin/activate`: ativa máquina virtual
- `deactivate`: desativa máquina virtual
- `pip3 install flask pymysql`: instala o flask (com a MV ativada!) e o mySQL.
- `pip3 freeze > requirements.txt`: retorna um arquivo .txt com as dependencias instaladas na MV
- `pip3 install -r requirements.txt`: instala as bibliotecas do arquivo .txt
- `nano templates/index.html`: edita o arquivo .html no nano
- `cat ../<nome-da-pasta>/<nome-da-outra-pasta>/<arquivo-x.html> > /home/ubuntu/flask/templates/index.html`: copia o arquivo-x.html para o index.html
- `echo "from flask import Flask" > app.py`: retorna uma saída de texto no arquivo app.py
