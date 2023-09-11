##  INSTRUCCIONES
Código Python para crear chatbot en Whatsapp, utilizando la librería rivescript.

ChatBot inteligente con WhatsApp en Python, con la plataforma oficial de WhatsApp (WhatsApp cloud API). Al trabajar con la plataforma oficial de Whatsapp, la información que recibiremos y enviaremos será completamente encriptada y fiable. Tan solo tenemos que seguir estos pasos:
- Creamos una app en Facebook
- Configuramos el API de WhatsApp (Añadir telefono de pruebas y verificarlo, añadir URL de devolución de llamada Webhook, junto con el token de verificación deseado que se especifique en el código y verificar con API,<img width="960" alt="imagen" src="https://github.com/DanMkAg/chatbot-whatsapp/assets/43437599/32fd48d6-5ee1-467e-8539-994d277b83a3"> y en el apartado de Webhook, hacemos click en Administrar y nos suscribimos al servicio de mensajes de la API)
- Creamos una tabla en nuestra base de datos SQL (Adjunto codigo SQL en el archivo codigo_tabla_sql.sql)
- Modificamos el archivo __init__.py (Token verificación deseado, host, user, password y database) Por otro lado, introducir el token de acceso que nos facilita Facebook, y el identificador del número de teléfono que nos proporciona Facebook.<img width="960" alt="imagen2" src="https://github.com/DanMkAg/chatbot-whatsapp/assets/43437599/b5766325-6880-4abb-8cf1-33ae1565420f">

- Subimos los códigos con los archivos __init__.py y chatbot.rive, a nuestro host
- Instalamos las dependencias desde el SSH del hosting, de las librerias rivescript, mysql-connector-python, y heyoo

##  FUNCIONALIDAD
El archivo chatbot.rive es un texto plano, al cual llamaremos desde el código __init__.py, donde se muestran palabras patrones y disparadores de respuestas, que cuando el usuario diga cualquier palabra clave o patrón, automáticamente saltarán las respuestas que hayamos configurado como disparadores, creando así una inteligencia conversacional a nuestra medida.
