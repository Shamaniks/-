from abstract_db import AbstractDatabase
from tinydb import TinyDB, Query
from config import tdb_file

class TinyDatabase(AbstractDatabase):
    def __init__(self):
        self._db = TinyDB(tdb_file)

    def find_templates(self, fields: dict[str, str]) -> list[str]:
        template = Query()
        filt = None
        for field, field_type in fields.items():
            if filt is None: filt = (template[field] == field_type) | (template[field] == "text")
            else: filt = filt | (template[field] == field_type) | (template[field] == "text")
        return [form["name"] for form in self._db.search(filt)]
