# Backend para hacer consultas con un LLM a tu base de datos

Inicia el ambiente virtual

```
$ python -m venv venv
$ source venv/bin/activate
```

Instala las dependencias

```
pip install -r requirements.txt
```

Setea las variables de entorno. Renombra el archivo `.env.example` a `.env` y adentro reemplaza tu api key de openai, y tu string de conexión a tu base de datos.

```
OPEN_AI_API_KEY=apikey-de-openai
DATABASE_URL=url-de-conexion-a-la-base-de-datos
SERVER_URL=url-del-servidor-donde-alojar-el-backend
```

El string de conexión va a depender de tu base de datos, o de como te conectas a tu base de datos. Quizás no necesitas esta variable y todo lo haces desde el código.
El SERVER_URL se usa al inicializar fast api y es para generar la especificación open api para pegarla en el GPT, no es necesario para que el backend funcione.

## Ejecución

Si quieres correr el backend de forma local puedes usar ngrok: https://ngrok.com/, siga las instrucciones del sitio para que tu localhost se pueda acceder desde la internet.

Luego ejecuta la app:

```
$python main.py
```

Deberías ver algo como esto:

```
INFO:     Started server process [18128]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### GPT

Ahora puedes ir a crear un GPT, pegar las instrucciones del archivo de instrucciones, y el schema dentro de las actions.
