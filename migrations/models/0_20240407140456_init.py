from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "profanityfilterprovidersettings" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "max_relative_distance" DOUBLE PRECISION NOT NULL  DEFAULT 0.3,
    "censor_whole_words" BOOL NOT NULL  DEFAULT True
);
CREATE TABLE IF NOT EXISTS "wordlist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "word" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "value" TEXT NOT NULL,
    "word_list_id" INT NOT NULL REFERENCES "wordlist" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
