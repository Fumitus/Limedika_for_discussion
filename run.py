from Limedika_for_discussion.app import app
from Limedika_for_discussion.db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
