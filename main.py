from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/Inicio.html")

@app.route('/inf')
def inf():
    return render_template("/Info.html")

@app.route('/formula')
def Form():
    return render_template("/Formulario.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=3000, debug=True)



