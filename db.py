import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


db_string = 'postgresql+psycopg2://pk:herkules@localhost/env_data_db'
# db_string = 'postgresql+psycopg2://pk:herkules@10.147.20.112:5432/env_data_db'
Base = declarative_base()
engine = create_engine(db_string, echo=True)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    """
    def __repr__(self):
        # return f'User(id={self.id}, name={self.name})'
        return {"id": str(self.id), "name": self.name}
    """


class DemoData(Base):
    __tablename__ = 'demo_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    battery = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)

    """
    def __repr__(self):
        return f'data: {self.timestamp}; '
    """


User.__table__

Base.metadata.create_all(engine)

session = Session()
"""
user1 = User(name='oliver')
session.add(user1)
"""
us_ = session.query(User).all()
print('users: ', us_)
#db.connect()

session.commit()
session.close()


def read_users():
    session = Session()
    users = session.query(User).all()
    # session.commit()
    session.close()

    users_list = []
    for user in users:
        users_list.append({"id": user.id, "name": user.name})

    return users_list


def add_user(name):
    session = Session()
    user1 = User(name=name)
    session.add(user1)
    session.commit()
    session.close()


def add_demo_data(battery, temperature, humidity):
    session = Session()
    data1 = DemoData(
        timestamp=datetime.utcnow(),
        battery=battery,
        temperature=temperature,
        humidity=humidity
    )
    session.add(data1)
    session.commit()
    session.close()
