# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)

# Lee la API Key desde Render (Environment Variable)
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():

    nombre = request.form["nombre"]
    contacto = request.form["contacto"]
    pasajeros = request.form["pasajeros"]
    destino = request.form["destino"]
    salida = request.form["salida"]
    llegada = request.form["llegada"]

    mensaje = f"""
Nuevo mensaje desde la web:

Nombre: {nombre}
Contacto: {contacto}
Pasajeros: {pasajeros}
Destino: {destino}
Salida: {salida}
Llegada: {llegada}
"""

    try:
        message = Mail(
            from_email="andrea.costatrip@gmail.com",
            to_emails="andrea.costatrip@gmail.com",
            subject="Nueva solicitud desde CostaTrip",
            plain_text_content=mensaje,
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)

        return redirect(url_for("inicio"))

    except Exception as e:
        return f"Error al enviar: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
