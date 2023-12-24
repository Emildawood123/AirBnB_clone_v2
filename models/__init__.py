#!/usr/bin/python3
"""import storage engines"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
