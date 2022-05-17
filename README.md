# Primera Entrega del trabajo final - CoderHouse

Repositorio en GitHub del proyecto para el curso de Python en CoderHouse.

Pasos que se siguieron para el desarrollo de la web (programación)


El usuario interactúa con DJANGO a través de las URL, estas URL desde nuestro PATH (url.py)
se conecta con las VISTAS (views.py). Estas vistas puede tomar datos de un modelo (o no) y 
las muestra en el template (renderiza). Este template tiene links o botones que van a 'pegarle' a otra
URLs formando el ciclo.


Creamos el primer VIEW, dentro del proyecto creamos el archivo 'views.py', importamos ahí el 'HttpResponse'.
Hacemos el viwe como si fuera una función. (def - request y return)
Luego creamos la dirección, un path, en urls.py.
Importamos desde las vistas las direcciones a mostrar.

Se pueden agregar parámetros o acciones a estas vistas, por ejemplo que devuelva mensajes específicos al ingresar
un comando, realizar una búsqueda o ingresar a una url distinta.

También asignamos parámetros a las URL definiendo desde la view los parámetros del path.

Luego es necesario ir agregando las plantillas. Para eso se crea la carpeta 'templates' y dentro de esta carpeta
creamos el primer html. Aquí se empieza a utilizar el lenguaje HTML para darle formato a la página.
A esta plantilla la renderizamos con un contexto (este es el lugar desde donde los templates reciben los datos).

Las variables de contexto se escriben entre dos llaves '{{}}' todo esto es código DJANGO.
(También se pueden cargar plantillas desde DJANGO utilizando el loader para optimizar las vistas).

Importante es crear una App (se puede realizar desde la terminal o desde el navegador de direcciones de VSC)
Un proyecto se compone de varias aplicaciones, puede haber varias aplicaciones dentro del mismo proyecto, esto
ayuda a ordenar las cosas.

Dentro de AppCoder creamos los distintos MODELOS ---> models.py
Importamos desde django los modelos y creamos las distintas clases con sus datos y atributos particulares.

Para que la app corra sin problema se debe indicar el nombre en el apartado de 'apps' en settings.py

Luego hay que subir estos modelos a la base de datos, para eso utilizamos en la terminal el siguiente comando:

python manage.py makemigrations
python manage.py migrate

Se suben las vistas y se agrega la url correspondiente.
