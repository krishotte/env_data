import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_string = 'postgresql+psycopg2://pk:herkules@localhost/env_data_db'
# db_string = 'postgresql+psycopg2://pk:herkules@10.147.20.112:5432/env_data_db'
Base = declarative_base()
engine = create_engine(db_string, echo=True)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'User(id={self.id}, name={self.name})'


class DemoData(Base):
    __tablename__ = 'demo_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    battery = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)

    def __repr__(self):
        return f'data: {self.timestamp}; '


User.__table__

Base.metadata.create_all(engine)

session = Session()
user1 = User(name='oliver')
session.add(user1)

us_ = session.query(User).all()
print('users: ', us_)
#db.connect()

session.commit()
session.close()



