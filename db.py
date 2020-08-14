import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from ini import Ini2

default_config = {
    'token': '',
    'db_string': '',
}

loaded_config = Ini2().read('conf.json')

config = {**default_config, **loaded_config}
print(f'config: {config}')

db_string = config['db_string']

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


class EnvData(Base):
    __tablename__ = 'env_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    battery = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)

    """
    def __repr__(self):
        return f'data: {self.timestamp}; '
    """


# User.__table__

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


def add_env_data(battery, temperature, humidity, pressure):
    session = Session()
    data1 = EnvData(
        timestamp=datetime.utcnow(),
        battery=battery,
        temperature=temperature,
        humidity=humidity,
        pressure=pressure
    )
    session.add(data1)
    session.commit()
    session.close()


def env_data_stat():
    session = Session()
    env_datas = session.query(EnvData).all()
    # session.commit()
    session.close()

    first_timestamp = env_datas[0].timestamp
    last_timestamp = env_datas[-1].timestamp

    stats = {
        'start_time': first_timestamp,
        'stop_time': last_timestamp,
        'data_length': len(env_datas),
    }

    return stats
