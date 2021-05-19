# Insight Local 
aplicação responsável pela comunicação entre o banco de dados Oracle e a aplicação web Insight
# Informações para Teste

Para facilitar os testes, você pode apontar o `pip` para o arquivo `requirements.txt` e instalar as dependências do projeto:

```
# pip install -r requirements.txt
```

Para testar se a conexão com o banco está funcionando corretamente, basta tentar aplicar uma migração na pasta do projeto:

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

Depois criar um superusuário:

```
$ python manage.py createsuperuser 
```

Adiciona as informações, e quando tudo estiver ok:

```
$ python manage.py runserver
```

O Django irá rodar o servidor embutido no projeto e rodará no localhost de sua máquina, se tudo estiver ok, é só acessar a aplicação. =)
