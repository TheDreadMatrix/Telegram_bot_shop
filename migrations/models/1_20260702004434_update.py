from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "age" INT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "age";"""


MODELS_STATE = (
    "eJztl21v2jAQx78KyismdRUNBNjeAWMr04CppdvUqopMYoKFY9PEWYsqvvt8JiFPhEFHB5"
    "P2LvnfXXz3wz4fz5rLbUz98xsfe9r70rPGkIvlQ0o/K2loPo9VEAQaU+UYSA+loLEvPGQJ"
    "KU4Q9bGUbOxbHpkLwplUWUApiNySjoQ5sRQw8hBgU3AHi6lK5O5eyoTZ+An70et8Zk4Ipn"
    "YqT2LD2ko3xWKutB4TH5UjrDY2LU4Dl8XO84WYcrb2JkyA6mCGPSQwfF54AaQP2YVlRhWt"
    "Mo1dVikmYmw8QQEViXJ3ZGBxBvxkNr4q0IFV3uoXtUatWa3XmtJFZbJWGstVeXHtq0BFYD"
    "DSlsqOBFp5KIwxNyS/vzu40Pv35CJOCXQhmDW5yCVGF2+XU2IXsxKYYsdDrrlps7WJU4gt"
    "E/gifMfaee90vVpt6JVqvWnUGg2jWVljzJu28Wz3PgFS6cBle1g1jTxjaCPqOQe4M0XeZr"
    "zJmAxbWdBJsnXRk0kxc8RUvhqVLdi+ta46l62rslF5k2Y3CC26MqUpTuSq5r4YU0Ev4niE"
    "I54CeVHZhaT0KkSpbGmWHqd7YYz8D7MTd0GoDoB2KIj6Lgz1YoR6jqDlYajYRCLP8YO0CO"
    "LizSzTkRmidhh6Hj28Ft8/3KKyBnvI6CI8IFvojnr97vWo1f8Klbi+/0AVotaoCxZdqYuM"
    "Wq5nfon1R0rfe6PLEryWboeDriLIfeF4asXYb3SrQU4oENxk/NFEdqLjRWoEZgkT2GSWmC"
    "VAGCNr9og828xZuM6LfPMmV3ezCmJy5rBDuJBmOJC2sEesqbZhVA0tW4dVFPv8n1ZPbuIq"
    "nlZ/yv8YkNIe7TgR8vc68iEvNd0wdmnIhlHckcGWbslwNPaAGLr/mwBfZSqQKwrMNlxon6"
    "+Hg4LLLA7JgLxhssA7m1jirESJL+5PE+sWilB16tKK4JX7rR9Zrp0vw3b2NoIPtCXjo14v"
    "y18Zbmbv"
)
