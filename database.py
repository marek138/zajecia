from sqlalchemy import create_engine


engine = create_engine("sqlite:///movies_database.db", echo=True)

