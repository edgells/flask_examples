from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import MySQLdb


import eventlet.db_pool


# 不传递将使用默认值
url_args = {

}

url = "mysql+mysqldb://dev001:dev002@192.168.110.128:3306/flask"
conn = eventlet.db_pool.ConnectionPool(MySQLdb, **url_args).create
engine = create_engine(url, creator=conn,
                       pool_size=15, max_overflow=10, pool_timeout=10, pool_recycle=3600)

Session = scoped_session(sessionmaker(bind=engine))
db = Session()

