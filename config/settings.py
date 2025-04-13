import environ

from pathlib import Path

env = environ.Env()
env.read_env(".env")


BASE_DIR = Path(__file__).resolve().parent.parent

# Database Configuration
DATABASE_HOST = env.str("DATABASE_HOST", default="localhost")
DATABASE_PORT = env.int("DATABASE_PORT", default=5432)
DATABASE_NAME = env.str("DATABASE_NAME", default="postgres")
DATABASE_USER = env.str("DATABASE_USER", default="postgres")
DATABASE_PASSWORD = env.str("DATABASE_PASSWORD", default="password")

DATABASE_URL_ASYNC = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


# JWT configuration for Authentication
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30
SECRET_KEY = env.str("SECRET_KEY")
ALGORITHM = "HS256"
