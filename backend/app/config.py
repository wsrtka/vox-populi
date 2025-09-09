from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    sejm_api_base: str

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
