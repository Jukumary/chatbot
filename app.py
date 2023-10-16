from flask import Flask, request, jsonify
from models import db, Data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # puedes cambiar esto según tus necesidades

db.init_app(app)

@app.route('/data', methods=['POST'])
def add_data():
    # Aquí irá el código para agregar datos
    pass

if __name__ == '__main__':
    app.run(debug=True)
