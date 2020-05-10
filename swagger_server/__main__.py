#!/usr/bin/env python3

import connexion
from flask_sqlalchemy import SQLAlchemy
from swagger_server import encoder

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'CollabWrite'}, pythonic_params=True)
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/CollabWrite'
    db = SQLAlchemy(app.app)
    app.run(port=8080)

if __name__ == '__main__':
    main()
