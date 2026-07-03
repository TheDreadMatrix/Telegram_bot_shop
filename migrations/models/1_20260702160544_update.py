from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_users_telegra_ab91e9";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_users_telegra_ab91e9" ON "users" ("telegram_id");"""


MODELS_STATE = (
    "eJztl11v2jAUhv8KylUndRUNpLDdQdetTCtMLd2mVlVkEhOsOnZqO6Wo6n+fj0nIB4SBxP"
    "oh9S55z3uScx47+PBohdzHVB5cSiysz7VHi6EQ64uCvl+zUBRlKggKjagxxtphFDSSSiBP"
    "aXGMqMRa8rH0BIkU4UyrLKYURO5pI2FBJsWM3MXYVTzAamIKub7RMmE+fsAyvY1u3THB1C"
    "/USXx4t9FdNYuM1mPqqzHC20aux2kcsswczdSEs4WbMAVqgBkWSGF4vBIxlA/VJW2mHc0r"
    "zSzzEnM5Ph6jmKpcuxsy8DgDfroaaRoM4C0f7cNmq9luHDXb2mIqWSitp3l7We/zREOgP7"
    "SeTBwpNHcYjBk3hSkOBArdVQC7JKhkWEr8N8wUXY5mwmoBM7VkNLMdtFOcn2y70WjZ9cZR"
    "22m2Wk67vuC6HFoHuNv7Boy1ges9P/8SUugZZPg2zPUS4eMJEqv55nNKcHVDG8B9/q0aog"
    "eXYhaoib516muw/eqcH592zvec+ociu34SsU2oSFFwuhXB1L8bepvsTbNo1q4I2psQtKsJ"
    "2ksEIyTllIsVX3o1xXzO85Hc5U48rG8CUrsqSZpYEaUnMLTsIrUM84uOKBLi1UCLmSWkfp"
    "J6kF68UsC6B3/A6Cz5FVnDd9g7O7kYds5+QiehlHfUIOoMTyBiG3VWUveOSkuxeEjtd294"
    "WoPb2tWgf2IIcqkCYd6Y+YZXFtSEYsVdxqcu8nM/eKmagiksLEVSuRJjtu26FhLfl/VFl9"
    "UUD7Pi+DY39YAwQt7tFAnfXYpwm1d5l0OhHZYVxFBgVgXYQpXJ6NzBgngTa8VQnUTWjtUo"
    "87zP1W9orr7X/4agpC1O2lzK2zxobcfZZGJxnOqRBWLFgxY+jS0gJva3CfD/TCqcKcxWjC"
    "nfLwb9ihElSymBvGS6wWufeGq/RolUN68T6xqK0HXhzErh7Z11/pS5Hv8YdMuHETygqxm/"
    "6PHy9Be7Q6AW"
)
