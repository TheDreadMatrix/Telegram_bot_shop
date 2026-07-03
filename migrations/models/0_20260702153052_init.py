from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "telegram_id" BIGINT UNIQUE,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "role" VARCHAR(20) NOT NULL DEFAULT 'user',
    "password" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "last_seen" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl11v2jAUhv8KylUndRUNpLDdAetWphWmlm5TqyoyiQlWHTu1nbao6n+fj0nIB4SBxP"
    "oh9S55z3uScx4n8cmjFXIfU3lwIbGwPtceLYZCrA8K+n7NQlGUqSAoNKbGGGuHUdBYKoE8"
    "pcUJohJrycfSEyRShDOtsphSELmnjYQFmRQzchtjV/EAq6kp5Opay4T5+AHL9DS6cScEU7"
    "9QJ/Hh3kZ31SwyWp+pr8YIdxu7HqdxyDJzNFNTzhZuwhSoAWZYIIXh8krEUD5Ul7SZdjSv"
    "NLPMS8zl+HiCYqpy7W7IwOMM+OlqpGkwgLt8tA+brWa7cdRsa4upZKG0nubtZb3PEw2Bwc"
    "h6MnGk0NxhMGbcFKY4ECh0VwHskqCSYSnx3zBTdDmaCavnhvnJthuNll1vHLWdZqvltOsL"
    "qsuhdXi7/W9AWBu4fuLn70GKPEMMb4Y5XuLbmyKxmm4+p4RWN7QB2ud/UEP04FLMAjXVp0"
    "59DbZfnbPeSedsz6l/KLIbJBHbhIoUBadbEUz9u6GXChm+7NuW8jOLZu2KoL0JQbuaoL1E"
    "MEJS3nOx4j2vppjPeT6Su3wSD+ubgNSuSpImVkTpCQwtu0gtw/yiI4qEeDXQYmYJqZ+kHq"
    "QHrxSw7sEfMjpLviJr+I76p8fno87pT+gklPKWGkSd0TFEbKPOSureUWkpFhep/e6PTmpw"
    "WrscDo4NQS5VIMwdM9/o0oKaUKy4y/i9i/zcBy9VUzCFhaVIKldizLZd10Li+7K+6LKa4m"
    "FSnNzkZh4Qxsi7uUfCd5ci3OZV3uVQaIdlBTEUmFUBtlBlMjh3sCDe1FoxUieRtUM1yjzv"
    "U/Ubmqrv9L8QlLTFTptLeZsbre04m0wsjlM9skCsuNHCq7EFxMT+NgH+n0mFM4XZijHl+/"
    "lwUDGiZCklkBdMN3jlE0/t1yiR6vp1Yl1DEbou7FkpvL3Tzp8y196PYbe8GcEFuprxi24v"
    "T38BOSyfgA=="
)
