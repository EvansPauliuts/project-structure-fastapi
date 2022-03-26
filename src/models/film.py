import orjson

from pydantic import BaseModel


class Film(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson.dumps
