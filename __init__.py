#ChatBot inteligente con WhatsApp en Python
from flask import Flask, jsonify, request
app = Flask(__name__)
#CUANDO RECIBA LAS PETICIONES EN ESTA RUTA
@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    #SI HAY DATOS RECIBIDOS VIA GET
    if request.method == "GET":
        #SI EL TOKEN ES IGUAL AL QUE RECIBO
        if request.args.get('hub.verify_token') == "QigongValencia":
            #ESCRIBO EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return request.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES SE DEVUELVE UN MENSAJE DE ERROR
          return "Error de autentificacion."
    #RECIBO TODOS LOS DATOS ENVIADOS VIA JSON
    data=request.get_json()
    #EXTRAIGO EL NUMERO DE TELEFONO Y EL MANSAJE
    telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    #EXTRAIGO EL TELEFONO DEL CLIENTE
    mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    #EXTRAIGO EL ID DE WHATSAPP DEL ARRAY
    idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
    #EXTRAIGO EL TIEMPO DE WHATSAPP DEL ARRAY
    timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
    #ESCRIBO EL NUMERO DE TELEFONO Y EL MENSAJE EN EL ARCHIVO TEXTO
    #SI HAY UN MENSAJE
    if mensaje is not None:
      from rivescript import RiveScript
      #INICIALIZO RIVESCRIPT Y CAMBIO CONVERSACION
      bot = RiveScript()
      bot.load_file('chatbot.rive')
      bot.sort_replies()
      #OBTENGO LA RESPUESTA
      respuesta = bot.reply("localuser", mensaje)
      respuesta = respuesta.replace("\\n","\\\n")
      respuesta = respuesta.replace("\\","")
       #CONECTO A LA BASE DE DATOS
      import mysql.connector
      mydb = mysql.connector.connect(
          host = "DIRECCION HOST",
          user = "USUARIO BASE DE DATOS",
          password = "CONTRASEÑA BASE DE DATOS",
          database='NOMBRE BASE DE DATOS')
      mycursor = mydb.cursor()
      query="SELECT count(id) AS cantidad FROM registro WHERE id_wa='" + idWA + "';"
      mycursor.execute("SELECT count(id) AS cantidad FROM registro WHERE id_wa='" + idWA + "';")
      cantidad, = mycursor.fetchone()
      cantidad=str(cantidad)
      cantidad=int(cantidad)
      if cantidad==0 :
        sql = ("INSERT INTO registro"+ 
        "(mensaje_recibido,mensaje_enviado,id_wa      ,timestamp_wa   ,telefono_wa) VALUES "+
        "('"+mensaje+"'   ,'"+respuesta+"','"+idWA+"' ,'"+timestamp+"','"+telefonoCliente+"');")
        mycursor.execute(sql)
        mydb.commit()
        enviar(telefonoCliente,respuesta)
      #RETORNO EL STATUS EN UN JSON
      return jsonify({"status": "success"}, 200)
def enviar(telefonoRecibe,respuesta):
  from heyoo import WhatsApp
  #TOKEN DE ACCESO DE FACEBOOK
  token='EAADFmKPVdXgBO3JzqBeJykeKMUldZCW6s9P07rOR0dQTOu3b1xKzVSUJpZC7mVCkJsszuq69twlehUYYVeMwjY8l4JLZArAZCNWqL7ZA9i2cMuelEs400ufCHWwhn9Kz2kFMzeQvkesXzGdgIZA0ZBB7hTdg1o6SX5vkZAqmucD3opedLHVivBdagYbZAReUbGCFs8wvWZAqb2l9uLdFgWaZAsLg24R2WSb'
  #IDENTIFICADOR DE NÚMERO DE TELÉFONO
  idNumeroTeléfono='138300759355557'
  #INICIALIZO ENVIO DE MENSAJES
  mensajeWa=WhatsApp(token,idNumeroTeléfono)
  telefonoRecibe=telefonoRecibe.replace("521","52")
  #ENVIO UN MENSAJE DE TEXTO
  mensajeWa.send_message(respuesta,telefonoRecibe)
#INICIO FLASK
if __name__ == "__main__":
  app.run(debug=True)
