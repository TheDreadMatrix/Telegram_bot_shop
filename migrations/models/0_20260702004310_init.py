from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "telegram_id" BIGINT NOT NULL UNIQUE,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "full_name" VARCHAR(100),
    "role" VARCHAR(20) NOT NULL DEFAULT 'user',
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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
    "eJztll1v2jAUhv8KyhWTuooGAmx3gbGVacDU0m1qVUUmMcHCsWnitEUV/30+JiEkIQw22K"
    "i0u/g974nPeRJ/vGgedzANzm8C7GvvSy8aQx6WDyn9rKSh2SxRQRBoRJUxlA6loFEgfGQL"
    "KY4RDbCUHBzYPpkJwplUWUgpiNyWRsLcRAoZeQixJbiLxUQVcncvZcIc/IyDeDibWmOCqZ"
    "Oqkzgwt9ItMZ8prcvER2WE2UaWzWnoscQ8m4sJZys3YQJUFzPsI4Hh9cIPoXyoLmoz7mhZ"
    "aWJZlriW4+AxCqlYa3dHBjZnwE9WE6gGXZjlrX5Ra9Sa1XqtKS2qkpXSWCzbS3pfJioC/a"
    "G2UHEk0NKhMCbcBKbY9ZFnbQLYIm4hw0zir2HG6E6A5jtdr1YbeqVabxq1RsNoVlZY86Ft"
    "fFvdT4BYGrj85ZcLIWaeMIaloZ5zgNsT5G/Gu56TYSsbOkm2Hnq2KGaumMihUdmC7Zt51b"
    "40r8pG5U2aXT+K6CqUpjiWs1r7Ykwl/RbHiNIKY2xJOCa73DFAXlR2ISldhShVLM3S53Qv"
    "jLH/MH/iLgjVAtAOBVHfhaFejFDPEbR9DB1bSOQ5fpARQTy8mWU6M0PUiVLP44dj8f3DX1"
    "T24AwYnUcLZAvdYbfXuR6ava/QiRcED1QhMocdiOhKnWfUcj3zJVYvKX3vDi9LMCzdDvod"
    "RZAHwvXVjIlveKtBTSgU3GL8yULO2o4XqzGYBdwqxtO18xGEEbKnT8h3rFyE67zImw95up"
    "dVEEOu+iwAF8qMLlkm9ok92XT9iiJbL2Ao8fy/gb2iG9ijvDdDSXtsx2spf29HPuShphvG"
    "LhuyYRTvyBBLb8mwNPaAGNlfJ8Cj3ArkjAKzDQfa5+tBv+AwS1IyIG+YbPDOIbY4K1ESiP"
    "vTxLqFInSdOrRieOWe+SPLtf1l0MqeRvCClmT8T4+XxU/ImQmW"
)
