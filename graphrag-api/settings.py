from pydantic_settings import BaseSettings
import yaml

class Settings(BaseSettings):
    GRAPHRAG_CLAIM_EXTRACTION_ENABLED: bool
    INPUT_DIR: str
    COMMUNITY_LEVEL: int

    class Config:
        env_file = ".env"
        

def load_settings_from_yaml(yaml_file_path: str) -> Settings:
    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        config_dict = yaml.safe_load(file)
    return Settings(**config_dict)
