# guithub-api
guithub-api lab

terminal:


### Clone o projeto: 

`
git clone git@github.com:andrequeiroz2/guithub-api.git
`
## Raiz do projeto:

### instale seu ambiente virtual: 

`
python3 -m venv venv ou python -m venv venv`

### Inicie seu ambiente virtual: 

`
source venv/bin/activate
`

### Instale suas dependencias:

`
pip install -r requirements.txt
`

### Localize a variavel GUITHUB_TOKEN dentro do arquivo .env, coloque seu token do github.com

ex:
`
GUITHUB_TOKEN=asdasdasasdadwerwrrw
`

### Na pasta src/ inicie o app:

`
uvicorn main:app --reload --port 5000
`

## Endpoints:

### Lista todos os repositorios do usuario logado:

params Query: 
- alphabetical=boolean

`
request:
http://127.0.0.1:5000/all/?alphabetical=false
`

### Lista dados do repositorio do usuario logado:

params Query: 
- name=nome do repositorio

`
request:
http://127.0.0.1:5000/search/name/?name=boto3s3
`

### Lista repositorios por filtros:

params Query:
- sort = tipo(string); valores possiveis("stars", "forks", "updated"); valor padrao="updated".
- order = tipo(string); valores possiveis("asc", "desc"); valor padrao="asc".
- limit = tipo(inteiro); valor padrao=10.
- user = tipo(string); name do usuario.
- language = tipo(string); linguagem utilizada no repositorio.
- readme = tipo(string); palavra contida no readme.
- archived = tipo(boolean); valor padrao="false".
- alphabetical = tipo(boolean)
`
request:
http://localhost:5000/search/filters/?sort=updated&order=desc&limit=3&user=andrequeiroz2&language=python&readme=device&archived=false&alphabetical=true
`

## Util:

Na pasta utils/ segue copia dos testes dos endpoints feitos no Insominia