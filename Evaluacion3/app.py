from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    try:
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Rangos
        if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100):
            return "Valores fuera del rango permitido", 400

        # Calcular el promedio de las notas
        promedio = (nota1 + nota2 + nota3) / 3

        # Determinar estado (APROBADO o REPROBADO)
        if promedio >= 50 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    except ValueError:
        return "Datos inválidos", 400


# Ruta para el formulario del ejercicio 2
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/procesar_formulario2', methods=['POST'])
def procesar_formulario2():
    try:
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encontrar el nombre con más caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)


        return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad_caracteres=cantidad_caracteres)

    except ValueError:
        return "Datos inválidos", 400


if __name__ == '__main__':
    app.run(debug=True)

