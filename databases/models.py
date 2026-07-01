from tortoise import fields
from tortoise.models import Model   


class User(Model):
    id = fields.IntField(pk=True)

    age = fields.IntField(null=True)

    telegram_id = fields.BigIntField(unique=True)

    username = fields.CharField(max_length=50, unique=True)

    full_name = fields.CharField(max_length=100, null=True)

    role = fields.CharField(max_length=20, default="user")

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"