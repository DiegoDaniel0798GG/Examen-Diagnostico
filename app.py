from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    edad = request.form.get("edad")
    sexo = request.form.get("sexo")
    peli_fav = request.form.get("peli-fav")
    comida_fav = request.form.get("comida-fav")
    animal_fav = request.form.get("animal-fav")
    ocupacion = request.form.get("ocupacion")
    expectativas = request.form.get("expectativas")
    respuesta = request.form.getlist("respuesta")  # Puede devolver varias respuestas
    comentarios = request.form.get("comentarios")

    # Guardar en un archivo de texto
    with open("respuestas.txt", "a", encoding="utf-8") as file:
        file.write(f"Nombre: {nombre} {apellidos}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Sexo: {sexo}\n")
        file.write(f"Película Favorita: {peli_fav}\n")
        file.write(f"Comida Favorita: {comida_fav}\n")
        file.write(f"Animal Favorito: {animal_fav}\n")
        file.write(f"Ocupación: {ocupacion}\n")
        file.write(f"Expectativas: {expectativas}\n")
        file.write(f"Orgulloso/a: {', '.join(respuesta)}\n")
        file.write(f"Comentarios: {comentarios}\n")
        file.write("=" * 30 + "\n")

    return "Datos guardados correctamente"

if __name__ == "__main__":
    app.run(debug=True)
