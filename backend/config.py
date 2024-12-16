from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    database_url_notasync: str
    jwt_secret: str
    jwt_lifetime: int

    class Config:
        env_file = ".env"

settings = Settings()