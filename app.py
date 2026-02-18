# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# CONFIGURA TU CORREO AQUÍ
TU_CORREO = "catalina.cornejo01@gmail.com"
TU_PASSWORD = "eead itod uuhp xqdx"

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
        msg = EmailMessage()
        msg["Subject"] = "Nueva solicitud desde CostaTrip"
        msg["From"] = TU_CORREO
        msg["To"] = TU_CORREO
        msg.set_content(mensaje)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(TU_CORREO, TU_PASSWORD)
            server.send_message(msg)

        # Recarga la página limpia
        return redirect(url_for("inicio"))

    except Exception as e:
        return f"Error al enviar: {e}"

if __name__ == "__main__":
    app.run()

