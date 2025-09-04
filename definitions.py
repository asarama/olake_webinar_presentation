from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    S3_BUCKET_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_REGION: str = "us-west-2"
    LAKEKEEPER_CATALOG_URL: str
    LAKEKEEPER_WAREHOUSE: str


settings = Settings.model_validate({})

S3_BUCKET_NAME = settings.S3_BUCKET_NAME
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
AWS_S3_REGION = settings.AWS_S3_REGION

LAKEKEEPER_CATALOG_URL = settings.LAKEKEEPER_CATALOG_URL
LAKEKEEPER_WAREHOUSE = settings.LAKEKEEPER_WAREHOUSE

