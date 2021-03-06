# Read the environment variables
import json
import os
import logging

dotcloud_env = {
        'DOTCLOUD_DB_SQL_LOGIN': '',
        'DOTCLOUD_DB_SQL_PASSWORD': '',
        'DOTCLOUD_DB_SQL_HOST': 'localhost',
        'DOTCLOUD_DB_SQL_PORT': '5432',
        }

try:
    dotcloud_env_file_path = os.path.expanduser('~/environment.json')
    with open(dotcloud_env_file_path) as f:
      dotcloud_env.update(json.load(f))
except Exception as e:
    logging.exception('unable to load {0}'.format(dotcloud_env_file_path))

# Flask setup
from flask import Flask
app = Flask(__name__)

# PostgreSQL connection
import psycopg2
conn = psycopg2.connect(database="test",
                        user=dotcloud_env['DOTCLOUD_DB_SQL_LOGIN'],
                        password=dotcloud_env['DOTCLOUD_DB_SQL_PASSWORD'],
                        host=dotcloud_env['DOTCLOUD_DB_SQL_HOST'],
                        port=int(dotcloud_env['DOTCLOUD_DB_SQL_PORT']))
cur = conn.cursor()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
