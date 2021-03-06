
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_USERNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    SECRET_KEY: str
    DATABASE_HOSTNAME: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    DATABASE_PORT: int

    class Config:
        env_file = '.env'

settings = Settings()

