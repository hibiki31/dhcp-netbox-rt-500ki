from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host_address: str | None = Field(default=None)
    host_username: str | None = Field(default=None)
    host_password: str | None = Field(default=None)
    netbox_url: str | None = Field(default=None)
    netbox_token: str | None = Field(default=None)
    netbox_dhcpprefix: str | None = Field(default=None)

    class Config:
        env_file = ".env"
        case_sensitive = False

sts = Settings()