from flask import Flask
from Controller import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    """
    Ejecuta la aplicación Flask en modo de depuración si se ejecuta como script principal.
    """
    app.run(debug=True)
