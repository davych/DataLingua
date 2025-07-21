import os
from langchain_community.utilities import SQLDatabase

db_path = os.path.join(os.path.dirname(__file__), "Chinook.db")
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")