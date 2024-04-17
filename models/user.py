from typing import List, Document


class User(Document):
    user_id: int
    name: str
    password: str
    any: List[int]
