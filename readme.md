# Site de para Criação de Documentos
Projeto e area de TESTES feito com Django 2.2.9 , Weasyprint e outros. 
- Projeto FOCADO em BackEnd.
- Vai ter um modulos e codes em testes.
- Rederização em PDF na maioria dos documentos.


## O que contém o Projeto:
- Criação de Usuario Personalizado (Confirmação de Senha e outros);
- Login por Email;
- Personalização de alertas no sites (Testes de Respostas Django e Bootstrap);
- Testes de CRUD personalizados;
- Teste de bancos de dados salvos no SQLite;
- Uploads de Fotos;
- Compactação das fotos para otimização do Servidor;
- Testes de Mask Jquery (data,telefone);
- Testes JavaScript (Animações);
- Render para PDF (Testes de Renderização com imagens para os servidores);

## Para uma boa instalação e testes siga a ordem abaixo.

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
python manage.py migrate accounts
python manage.py makemigrations accounts
python manage.py migrate ninth_app
python manage.py makemigrations ninth_app
python manage.py migrate doctag
python manage.py makemigrations doctag
python manage.py migrate
python manage.py makemigrations
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