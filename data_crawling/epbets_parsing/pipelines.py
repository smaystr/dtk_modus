from app.pg_db.models import Position, db
from app import main


class EpbetsPipeline:

    def open_app(self):
        db.app = main
        db.init_app(main)

    def close_app(self):
        db.close_all_sessions()

    def validate_data(self, item):
        process_value = lambda value: value if value else None
        return {item: process_value(value) for item, value in item.items()}

    def process_item(self, item):
        dict_to_insert = self.validate_data(item)
        position_item = Position(**dict_to_insert)

        try:
            db.session.add(position_item)
            db.session.commit()

        except Exception as e:
            print(f"Error raised {e}")
            db.session.rollback()
        return item
