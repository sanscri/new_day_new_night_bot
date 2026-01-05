from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  BOT_TOKEN: str
  ADMINS: str
  GROUP_LINK: str
  GROUP_ID: int

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()