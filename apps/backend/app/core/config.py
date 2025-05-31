from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Guia de Bares SP"
    VERSION: str = "1.0.0"

    DATABASE_URL: str
    POSTGRES_DB: str = "guia_bares"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: str = "5432"

    REDIS_HOST: str = "redis"
    REDIS_PORT: str = "6379"

    SECRET_KEY: str = "super-secret"

    class Config:
        env_file = ".env"

settings = Settings()