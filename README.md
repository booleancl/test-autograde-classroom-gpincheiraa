# Computación en la nube

## Instalación

```bash
pipenv install --dev
```

## Correr la aplicación

Crea un archivo `.env` con la siguiente información:

```bash
FLASK_APP="src/app.py"
FLASK_DEBUG=1
```

y luego correr el siguiente comando:
```bash
pipenv run flask run
```

## Correr pruebas automatizadas

```bash
pipenv run pytest
```
## Actividad 1

Sube este proyecto a GitHub, luego crearse una cuenta de [https://render.com](https://render.com), crear un "Web Service" y vincular este repositorio con el servicio. 

Selecciona en el panel del lado derecho la opción "Connect GitHub", selecciona la organización "ADO-Boolean" y selecciona la opción "Only selected repositories", luego envía la solicitud para agregar Render. Espera la aprobación y continua el proceso.

Luego cuando se te soliciten las configuraciones para la aplicación, procura utilizar lo siguiente:

```
Branch: main
Build Command: pipenv install
Start Command: gunicorn src.app:app
```

Es posible que obtengas un error dado que render por defecto utiliza Python 3.7.

Para solucionarlo debes ir a la opción "Environment" en el panel de la izquierda y luego crea una variable llamada `PYTHON_VERSION` y dale el valor `3.10.8`.

Si todo sale bien, debería publicarse el servicio y puedes acceder la URL dada por render.

### Agrega tu URL

Actualiza el archivo `assigment-url` con la dirección de tu aplicación y sube tus cambios.

## Actividad 2

Abre el archivo `app.py` y modifica la ruta `/info` y edita la variable `api_url` procurando interpolar el valor leído desde los query parameters disponible bajo `request.args`.

Antes de echar a correr la aplicación, fijémonos en el archivo `.env` para entender que hacen las variables ya configuradas.

Ahora correr tu aplicación y luego haz algunas pruebas sobre la ruta `/info` pasando los query params por ejemplo `?country_code=cl`.

Modifica el template `info.html` con algunos componentes de BootStrap para darle un mejor estilo procurando mantener el formato de la información intacto y así no afectar las pruebas automatizadas.

## Actividad 3

Haz algunas pruebas sobre la ruta `/login` escribiendo información en el formulario y mejorando el diseño de la página `login.html`.

Revisa la información enviada por el formulario y fijate que sucede cuando agregamos el atributo `method="POST"` en el formulario HTML.

Agrega los elementos `<input>` y `<label>` correspondientes para crear 2 campos como sigue:

```
label: Nombre de usuario, type: email, name: username
label: Password, type: password, name: password
```

donde `label` es el valor de texto que se le debe agregar a la etiqueta `<label>` y `type` y `name` son los atributos de la etiqueta `<input>`.

Procura observar con detalle la importancia del atributo `name` y como se relaciona con la URL en la caso de un formulario tipo `GET` y tipo `POST`.

## Finalizar Actividades

Sube los cambios y valida que tanto las pruebas automatizadas en GitHub están OK y que se actualizó el proyecto en render.com con los últimos cambios agregados.
