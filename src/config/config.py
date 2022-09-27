import os
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings, root_validator
from functools import lru_cache

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    """
    Cria objeto com todas as variaveis
    """
    API_TITLE = os.getenv("API_TITLE")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    DEBUG: bool = os.getenv("DEBUG")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


@lru_cache
def get_api_settings() -> Settings:
    """
    Faz cache das configuracoes
    :return: Configuracoes armazenadas no cache
    """
    return Settings()


settings = get_api_settings()
