
# Django - tutorial

Referências:
https://docs.djangoproject.com/en/4.2/intro/tutorial01/


## Projeto

Comando para iniciar o projeto

  django-admin startproject todo_list fold


Em que `todo_list` é o nome do projeto
E *fold* é a pasta em que o projeto vai ser criado. Para usar o diretório atual pode-se usar $\cdot$

```bash
➜  fold tree -L 3
.
├── manage.py
└── todo_list
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


```

Para executar

  python manage.py runserver

Pode ser que:

  python manage.py migrate


## App

Para criar um app:

  python manage.py startapp notes

Pode-se deixar rodando:

  python manage.py runserver

Para rodar na interface física e outros computadores da rede local poderem rodar:

  python manage.py runserver 0.0.0.0:8000


### Acesso

Daí pode-se acessar:

  localhost:8000/notes

Ou o nome do app, se for outro


### Visibilidade do app

Adicionar os apps a no arquivo settings.py principal:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes.apps.NotesConfig'
]
```

### PAra gerar os modelos de dadosÇ

python manage.py makemigrations notes


Editar a URL no projeto principal para apontar para a app:

  urlpatterns = [
      path('admin/', admin.site.urls),
      path("notes/", include("notes.urls")),
  ]


Dentro do App:

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


Templates

Criar settings.py local


## Form

Lembrar do {% url 'insert_post_it'}

```html
<div class="post-it">
    <form method="POST" action="{% url 'insert_post_it' %}">
      {% csrf_token %}
      <label for="title">Title:</label>
      <input type="text" id="title" name="title"><br>

      <label for="content">Content:</label>
      <textarea id="content" name="content"></textarea><br>

      <input type="submit" value="Add Post-it">
    </form>
  </div>

```

## Form que trata o POST

CSRF exempt:

  from django.views.decorators.csrf import csrf_exempt



## Admin

A página `admin` já está no ar:

http://127.0.0.1:8000/admin/

Para criar admin:

  python manage.py createsuperuser


## Rota raw

Definir o método  definir a rota no urls.py/urlpatterns

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('raw', views.raw, name='raw'),

]

## Criar modelo

```python
from django.db import models


class PostIt(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

```

### Gerar migrações

python manage.py makemigrations notes


### Ver sql gerado

python manage.py sqlmigrate polls 0001

### Migrar

python manage.py migrate

### Brincar com objetos

python manage.py shell


>>> from notes.models import PostIt
>>> PostIt.objects.all()
<QuerySet []>


### Inserindo objetos no banco

nota = PostIt(title=title, content=content)
nota.save()

### Mostrando objetos na tela

from .models import PostIt

for nota in PostIt.objects.all():
    data["data"].append({"title": nota.title, "content": nota.content})

return render(request, "notes/index.html", data)
