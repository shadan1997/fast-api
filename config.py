# TODO use env file to load settings
class Settings:

    MONGODB_URL: str = "mongodb://localhost:27017"
    NEO4J_URI: str = ""  # dev
    NEO4J_USER: str = ""
    NEO4J_PASSWORD: str = ""  # dev

    DEV_NEO4J_URI: str = ""
    DEV_NEO4J_USER: str = "neo4j"
    DEV_NEO4J_PASSWORD: str = ""


settings = Settings()
