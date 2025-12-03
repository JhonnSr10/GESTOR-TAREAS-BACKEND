from pydantic import BaseModel


class Settings(BaseModel):
    DATABASE_URL: str = "sqlite:///./dev.db"
    SECRET_KEY: str = "change-me"
    ENV: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

