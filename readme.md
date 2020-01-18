# Site de para Criação de Documentos
Projeto feito com Django , Weasyprint e outros.
Siga as ordem.

## Criar Conda Config Django
- Primeiro Configure cmd [Configurar Conda Env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- Digite: 
```bash
activate base
```
- Crie um Env no cmd: 
```bash
conda create -n MyDjangoEnv python
```
- Ative:
```bash
 activate MyDjangoEnv
 ```
- Instale os Modulos:
```bash
 pip install -r requirements.txt
 ```
## Config Django
```bash
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Teste no Celular - Windows
- Abra cmd 
- Digite 
```bash
ipconfig
``` 
- Abra no projeto settings.py - digite o ip encontrado no ipconfig
```bash 
- ALLOWED_HOSTS = ['ip-address']
``` 
- Digite o camando 
```bash 
python manage.py runserver 0.0.0.0:8000
```
- digite no Browser di seu celular o ip encontrado - 'http://ip-address:8000'