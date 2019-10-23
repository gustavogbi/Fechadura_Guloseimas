# Fechadura Guloseimas
 Projeto da EJ.
A organização dos commits devem acompanhar o seguinte [padrão](https://gist.github.com/gustavogbi/fcc50f61620ce572fd107ad33fde544f "padrão").

## Configurando a VirtualEnv
https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais


- `virutalenv env` para criar a VirtualEnv de nome "env"
- `source env/bin/activate` para ativar a VirtualEnv no Linux
- `env\Scripts\activate` para ativar a VirtualEnv no Windows
- Caso dê problemas no PowerShell do, executar este comando:
- `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser`
- `deactivate` para sair da VirtualEnv

## Instalando Dependências
Dentro da VirtualEnv, instalar o Django:
- `pip install django`

## Rodar o servidor
- `python manage.py makemigrations` para verficiar as alterações dos models
- `python manage.py migrate` para criar as tabelas do banco de dados listados em INSTALLED_APPS em guloseimas/settings.py
- `python manage.py runserver`
