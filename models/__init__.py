#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage/DBStorage
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique DBStorage/FileStorage instance for all models"""
storage.reload()
