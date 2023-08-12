from app import db_file, init_db, _

def insert():
  init_db()
  filename = input(_('filename'))