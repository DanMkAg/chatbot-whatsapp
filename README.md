# chatbot-whatsapp
##  INSTRUCCIONES
Codigo Python para crear chatbot en Whatsapp, utilizando la libreria rivescript
crear un ChatBot inteligente con WhatsApp en Python totalmente gratis y con la plataforma oficial de WhatsApp (WhatsApp cloud API). La ventaja que tenemos al trabajar con la plataforma oficial es que la información que recibiremos y enviaremos será completamente fiable. Solo debemos seguir estos pasos:
- Creamos una app en Facebook
- Configuramos el Api de WhatsApp (Añadir telefono de pruebas y verificarlo, añadir URL de devolución de llamada Webhook, junto con el token de verificacion deseado que se especifique en el código y verificar con API,<img width="960" alt="imagen" src="https://github.com/DanMkAg/chatbot-whatsapp/assets/43437599/32fd48d6-5ee1-467e-8539-994d277b83a3"> y en el apartado de Webhook, clicamos en Administrar y nos suscribimos al servicio de mensajes de la API)
- Creamos una tabla en nuestra base de datos SQL
- Modificamos el archivo __init__.py (Token verificacion deseado, host, user, password y database)
- Subimos los códigos con los archivos __init__.py y chatbot.rive, a nuestro host
- Instalamos dependencias desde SSH, de las librerias rivescript, mysql-connector-python, y heyoo

##  FUNCIONALIDAD
El archivo chatbot.rive es un texto plano, al cual llamaremos desde el codigo __init__.py, y donde se muestran palabras patrones y disparadores de respuestas, que cuando el usuario diga cualquier palabra clave o patron, automaticamente saltaran las respuestas que hayamos configurado como disparadores, creando asi una inteligencia conversacional a nuestra medida.
