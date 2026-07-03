from tortoise import fields
from tortoise.models import Model   


class User(Model):
    id = fields.IntField(pk=True)

    telegram_id = fields.BigIntField(null=True)

    username = fields.CharField(max_length=50, unique=True)

    role = fields.CharField(max_length=20, default="user")

    password = fields.CharField(max_length=100)

    created_at = fields.DatetimeField(auto_now_add=True)

    last_seen = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"