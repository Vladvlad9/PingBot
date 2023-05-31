from pydantic import BaseModel
from decimal import Decimal


class BotSchema(BaseModel):
    TOKEN: str
    ADMINS: list[int]


class ConfigSchema(BaseModel):
    BOT: BotSchema
    DATABASE: str
    PING: Decimal
