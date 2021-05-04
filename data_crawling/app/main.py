import os

from flask import Flask, request, jsonify
from app.pg_db.models import db, Position
from app.utilities import set_up_logging, load_env

web_app = Flask(__name__)
web_app.config.from_object(os.environ['APP_SETTINGS'])
web_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(web_app)

with web_app.app_context():
    db.create_all()


@web_app.route('/app/v1/statistics', methods=['GET'])
def get_count():
    count = Position.query.count()
    return jsonify({'count_positions': count})


@web_app.route('/app/v1/record', methods=['GET'])
def get_records():
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    query = Position.query
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)

    positions = query.all()
    positions = [item.as_dict() for item in positions]
    return jsonify({'positions': positions})


if __name__ == '__main__':
    load_env()
    set_up_logging(os.getenv('LOG_FILE'), bool(os.getenv('VERBOSE')))
    web_app.run(host=web_app.config['HOST'], port=web_app.config['PORT'])
