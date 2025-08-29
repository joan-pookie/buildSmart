from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Shared Base for all models
Base = declarative_base()

# SQLite database
engine = create_engine("sqlite:///buildsmart.db", echo=True)


def init_db():
    """
    Import all model files so they register with Base,
    then create the database tables.
    """
    import lib.models.client
    import lib.models.project
    import lib.models.worker
    import lib.models.project_assignment

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
