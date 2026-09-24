from auth_database import Base, engine
import models  # Import models to ensure they are registered with SQLAlchemy

Base.metadata.create_all(bind=engine)